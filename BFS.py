from utils import *
from queue import Queue
import matplotlib.pyplot as plt


def bfs(root_matrix, dest_matrix):
    pre_map.append({'son': root_matrix, "father": [[0, 0, 0], [0, 0, 0], [0, 0, 0]]})
    matrix_set = {matrix_to_string(root_matrix), }  # 已经搜索过的情况
    queue = Queue()
    queue.put(root_matrix)
    loop_times = 0
    while not queue.empty():
        loop_times += 1
        father = queue.get()  # 队首出队
        for direction in directions:
            son = move(direction, father)
            son_string = matrix_to_string(son)
            # if not is_same(son, father):
            if son_string not in matrix_set:  # 没有重复
                # print("Move 0 " + direction, end=":\n")
                pre_map.append({'son': son, 'father': father})
                if is_same(son, dest_matrix):
                    print("Loop Times: {}".format(loop_times))
                    return True
                else:
                    # show(son)
                    matrix_set.add(son_string)
                    queue.put(son)
    return False


def perform_plot_BFS(root_matrix, dest_matrix):
    """BFS as bellow"""
    bfs(root_matrix, dest_matrix)
    # for item in pre_map:
    #     print(item)
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
