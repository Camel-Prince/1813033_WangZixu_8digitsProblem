from utils import*
import matplotlib.pyplot as plt


def dfs(root_matrix, dest_matrix):
    matrix_set = {matrix_to_string(root_matrix), }
    pre_map.append({'son': root_matrix, 'father': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]})
    stack = [root_matrix, ]
    loop_times = 0
    while stack.__len__() != 0:
        loop_times += 1
        father = stack[len(stack)-1]
        available_son_num = 0
        son = None
        for direction in directions:
            moved = move(direction, father)
            moved_string = matrix_to_string(moved)
            if moved_string not in matrix_set:
                available_son_num += 1
                son = moved
                break
        if available_son_num == 0:
            stack.remove(father)
        else:
            stack.append(son)
            matrix_set.add(matrix_to_string(son))
            pre_map.append({'son': son, 'father': father})
            if is_same(son, dest_matrix):
                print("Loop Times: {}".format(loop_times))
                return True
    return False


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
