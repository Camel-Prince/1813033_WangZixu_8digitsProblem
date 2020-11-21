from utils import *


class Matrix:
    dest_matrix = None

    @classmethod
    def set_dest_matrix(cls, matrix):
        cls.dest_matrix = matrix

    def __init__(self, matrix, father_Matrix):
        if is_same(matrix, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
            self.father_Matrix = None
            self.depth = -1
        else:
            self.father_Matrix = father_Matrix  # 这是个Object
            self.matrix = matrix  # 这是个列表
            self.depth = self.father_Matrix.depth + 1
            self.f = self.depth + self.h()

    def h(self):
        result = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] != Matrix.dest_matrix[i][j]:
                    result += 1
        return result


# 存放的是Matrix对象
open_list = []
closed_list = []


def search_Matrix_list(Matrix_list, the_matrix):
    for element in Matrix_list:
        if is_same(element.matrix, the_matrix):
            return element
    return None


def f_cmp(ele):
    return ele.f


def get_least_cost_matrix(matrix_list, cmp):
    sorted_matrix_list = sorted(matrix_list, key=cmp)
    return sorted_matrix_list[0]


def A_star(root_matrix, dest_matrix):
    Matrix.dest_matrix = dest_matrix
    Root_Father = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]], father_Matrix=None)
    Root = Matrix(root_matrix, father_Matrix=Root_Father)

    open_list.append(Root)
    pre_map.append({'son': Root.matrix, 'father': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]})
    # print({'son': Root.matrix, 'father': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]})
    while open_list.__len__() != 0:
        new_Matrix = get_least_cost_matrix(open_list, f_cmp)
        open_list.remove(new_Matrix)
        closed_list.append(new_Matrix)
        if is_same(new_Matrix.matrix, dest_matrix):
            return True
        for direction in directions:
            moved_Matrix = Matrix(move(direction, new_Matrix.matrix), father_Matrix=new_Matrix)
            old_Matrix_in_open_list = search_Matrix_list(open_list, moved_Matrix.matrix)
            old_Matrix_in_closed_list = search_Matrix_list(closed_list, moved_Matrix.matrix)
            if old_Matrix_in_open_list is not None:  #
                if moved_Matrix.f < old_Matrix_in_open_list.f:
                    pre_map.append({'son': moved_Matrix.matrix, 'father': new_Matrix.matrix})
                    # print({'son': moved_Matrix.matrix, 'father': new_Matrix.matrix})
                    old_Matrix_in_open_list.f = moved_Matrix.f
            if old_Matrix_in_closed_list is not None:
                if moved_Matrix.f < old_Matrix_in_closed_list.f:
                    pre_map.append({'son': moved_Matrix.matrix, 'father': new_Matrix.matrix})
                    # print({'son': moved_Matrix.matrix, 'father': new_Matrix.matrix})
                    old_Matrix_in_closed_list.f = moved_Matrix.f
                    closed_list.remove(old_Matrix_in_closed_list)
                    open_list.append(old_Matrix_in_closed_list)
            if old_Matrix_in_closed_list is None and old_Matrix_in_open_list is None:
                pre_map.append({'son': moved_Matrix.matrix, 'father': new_Matrix.matrix})
                # print({'son': moved_Matrix.matrix, 'father': new_Matrix.matrix})
                open_list.append(moved_Matrix)

