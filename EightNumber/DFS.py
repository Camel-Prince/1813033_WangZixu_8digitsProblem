from utils import*


def dfs(root_matrix, dest_matrix):
    matrix_set = {matrix_to_string(root_matrix), }
    pre_map.append({'son': root_matrix, 'father': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]})
    print({'son': root_matrix, 'father': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]})
    stack = [root_matrix, ]
    while stack.__len__() != 0:
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
            print({'son': son, 'father': father})
            if is_same(son, dest_matrix):
                return True
    return False

