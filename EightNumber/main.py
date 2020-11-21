from utils import *
import matplotlib.pyplot as plt
from BFS import bfs
from DFS import dfs
from A_Start import A_star
root_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
dest_matrix = [[7, 3, 1], [2, 4, 6], [8, 0, 5]]


def perform_plot_DFS(root_matrix, dest_matrix):
    '''搜索并记录路径'''
    """DFS as bellow """
    dfs(root_matrix, dest_matrix)
    print("DFS Done!")
    fill_path_stack(dest_matrix)

    '''打印路径、动态地画出图'''
    i = 0
    while path_stack.__len__() != 0:
        print("Step {}".format(i))

        the_matrix = path_stack.pop()
        show(the_matrix)
        plot_matrix(the_matrix, block=False, plt=plt, title="DFS", step=str(i))
        i += 1
    print("Step {}".format(i))
    show(dest_matrix)
    plot_matrix(dest_matrix, block=True, plt=plt, title="DFS", step=str(i))


def perform_plot_BFS(root_matrix, dest_matrix):
    """BFS as bellow"""
    bfs(root_matrix, dest_matrix)
    for item in pre_map:
        print(item)
    print("BFS Done!")
    print("{} items in pre_map".format(len(pre_map)))
    fill_path_stack(dest_matrix)

    '''打印路径、动态地画出图'''
    i = 0
    while path_stack.__len__() != 0:
        print("Step {}".format(i))
        the_matrix = path_stack.pop()
        show(the_matrix)
        plot_matrix(the_matrix, block=False, plt=plt,
                    zero_color="#E8A250", another_color="#F2CF60",
                    title="BFS", step=str(i))
        i += 1
    print("Step {}".format(i))
    show(dest_matrix)
    plot_matrix(dest_matrix, block=True, plt=plt,
                zero_color="#E8A250", another_color="#F2CF60",
                title="BFS", step=str(i))


def perform_plot_A_Star(root_matrix, dest_matrix):
    """A* as bellow"""
    A_star(root_matrix, dest_matrix)
    print("A* Done!")
    print("{} items in pre_map".format(len(pre_map)))
    fill_path_stack(dest_matrix)
    print("A* needs {} steps".format(len(path_stack)))

    '''打印路径、动态地画出图'''
    i = 0
    while path_stack.__len__() != 0:
        print("Step {}".format(i))
        the_matrix = path_stack.pop()
        show(the_matrix)
        plot_matrix(the_matrix, block=False, plt=plt,
                    zero_color="#FFC050", another_color="#1D4946",
                    title="A* Algorithm", step=str(i))
        i += 1
    print("Step {}".format(i))
    show(dest_matrix)
    plot_matrix(dest_matrix, block=True, plt=plt,
                zero_color="#FFC050", another_color="#1D4946",
                title="A* Algorithm", step=str(i))

