from utils import *
import matplotlib.pyplot as plt

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
            self.f = self.depth + self.h_plus()

    def h(self):
        result = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] != Matrix.dest_matrix[i][j]:
                    result += 1
        return result

    def h_plus(self):
        result = 0
        for i in range(3):
            for j in range(3):
                ele = self.matrix[i][j]
                [m, n] = get_position(self.dest_matrix, ele)
                result += (abs(i-m)+abs(j-n))
        return result

    def show_Matrix(self):
        show(self.matrix)
        print("H(): {}\nG(): {}\nF(): {}".format(self.h(), self.depth, self.f))

# 存放的是Matrix对象
open_list = []
closed_list = []


def search_Matrix_list(Matrix_list, the_matrix):
    for element in Matrix_list:
        if is_same(element.matrix, the_matrix):
            return element
    return None


def get_least_cost_matrix(Matrix_list):
    temp_matrix = Matrix_list[0]
    for i in range(1, len(Matrix_list)):
        if Matrix_list[i].f < temp_matrix.f:
            temp_matrix = Matrix_list[i]
    return temp_matrix


def A_star(root_matrix, dest_matrix):
    Matrix.dest_matrix = dest_matrix
    Root_Father = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]], father_Matrix=None)
    Root = Matrix(root_matrix, father_Matrix=Root_Father)
    open_list.append(Root)
    pre_map.append({'son': Root.matrix, 'father': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]})
    # print({'son': Root.matrix, 'father': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]})
    loop_times = 0
    while open_list.__len__() != 0:
        loop_times += 1
        new_Matrix = get_least_cost_matrix(open_list)  # 当前研究的Matrix对象
        new_matrix = new_Matrix.matrix  # 当前研究的Matrix对象的matrix属性；
        open_list.remove(new_Matrix)
        closed_list.append(new_Matrix)
        if is_same(new_Matrix.matrix, dest_matrix):
            print("Loop Times: {}".format(loop_times))
            return True
        for direction in directions:
            moved_matrix = move(direction, new_matrix)
            if not is_same(moved_matrix, new_matrix):
                moved_Matrix = Matrix(moved_matrix, father_Matrix=new_Matrix)
                old_Matrix_in_open_list = search_Matrix_list(open_list, moved_matrix)
                old_Matrix_in_closed_list = search_Matrix_list(closed_list, moved_matrix)
                if old_Matrix_in_open_list is not None:  #
                    if moved_Matrix.depth < old_Matrix_in_open_list.depth:
                        old_Matrix_in_open_list.father_Matrix = new_Matrix
                        pre_map.append({'son': moved_matrix, 'father': new_matrix})
                        # print({'son': moved_Matrix.matrix, 'father': new_Matrix.matrix})
                        old_Matrix_in_open_list.depth = moved_Matrix.depth
                        old_Matrix_in_open_list.f = old_Matrix_in_open_list.depth+old_Matrix_in_open_list.h()
                if old_Matrix_in_closed_list is not None:
                    if moved_Matrix.depth < old_Matrix_in_closed_list.depth:
                        old_Matrix_in_closed_list.father_Matrix = new_Matrix
                        pre_map.append({'son': moved_matrix, 'father': new_matrix})
                        # print({'son': moved_Matrix.matrix, 'father': new_Matrix.matrix})
                        old_Matrix_in_closed_list.depth = moved_Matrix.depth
                        old_Matrix_in_closed_list.f = old_Matrix_in_closed_list.depth + old_Matrix_in_closed_list.h()
                        closed_list.remove(old_Matrix_in_closed_list)
                        open_list.append(old_Matrix_in_closed_list)
                if old_Matrix_in_closed_list is None and old_Matrix_in_open_list is None:
                    pre_map.append({'son': moved_Matrix.matrix, 'father': new_Matrix.matrix})
                    # print({'son': moved_Matrix.matrix, 'father': new_Matrix.matrix})
                    open_list.append(moved_Matrix)


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
