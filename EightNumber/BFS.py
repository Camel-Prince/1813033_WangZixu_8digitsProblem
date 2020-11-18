from utils import *
from queue import Queue


def bfs(root_matrix, dest_matrix):
    pre_map.append({'son': root_matrix, "father": [[0, 0, 0], [0, 0, 0], [0, 0, 0]]})
    matrix_set = {matrix_to_string(root_matrix), }  # 已经搜索过的情况
    queue = Queue()
    queue.put(root_matrix)
    while not queue.empty():
        father = queue.get()  # 队首出队
        for direction in directions:
            son = move(direction, father)
            son_string = matrix_to_string(son)
            # if not is_same(son, father):
            if son_string not in matrix_set:  # 没有重复
                # print("Move 0 " + direction, end=":\n")
                pre_map.append({'son': son, 'father': father})
                if is_same(son, dest_matrix):
                    return True
                else:
                    # show(son)
                    matrix_set.add(son_string)
                    queue.put(son)
    return False

