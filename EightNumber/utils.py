import copy
import collections

'''搜索并记录路径'''
directions = ["up", "down", "left", "right"]
pre_map = []  # 回溯链条
path_stack = collections.deque()


def get_father(son_matrix):
    father_matrix = None
    for item in pre_map:
        if is_same(item['son'], son_matrix):
            father_matrix = item['father']
    return father_matrix


def fill_path_stack(dest_matrix):
    father = get_father(dest_matrix)
    if is_same(father, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        return
    path_stack.append(father)
    fill_path_stack(father)


def show(matrix):
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end=" ")
            if j == 2:
                print(end="\n")


def get_position(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                return [i, j]


def up(father_mtx):
    i, j = get_position(father_mtx)
    if i == 0:
        return father_mtx
    else:
        son_mtx = copy.deepcopy(father_mtx)
        other = son_mtx[i - 1][j]
        son_mtx[i - 1][j] = 0
        son_mtx[i][j] = other
        return son_mtx


def down(father_mtx):
    i, j = get_position(father_mtx)
    if i == 2:
        return father_mtx
    else:
        son_mtx = copy.deepcopy(father_mtx)
        other = son_mtx[i + 1][j]
        son_mtx[i + 1][j] = 0
        son_mtx[i][j] = other
        return son_mtx


def left(father_mtx):
    i, j = get_position(father_mtx)
    if j == 0:
        return father_mtx
    else:
        son_mtx = copy.deepcopy(father_mtx)
        other = son_mtx[i][j - 1]
        son_mtx[i][j - 1] = 0
        son_mtx[i][j] = other
        return son_mtx


def right(father_mtx):
    i, j = get_position(father_mtx)
    if j == 2:
        return father_mtx
    else:
        son_mtx = copy.deepcopy(father_mtx)
        other = son_mtx[i][j + 1]
        son_mtx[i][j + 1] = 0
        son_mtx[i][j] = other
        return son_mtx


"""
move按照参数对矩阵中的0进行移动
若无法移动则返回原矩阵
"""


def move(direction, mtx):
    if direction == "up":
        return up(mtx)
    elif direction == "down":
        return down(mtx)
    elif direction == "left":
        return left(mtx)
    elif direction == "right":
        return right(mtx)


def matrix_to_string(matrix):
    result = ""
    for i in range(3):
        for j in range(3):
            result += str(matrix[i][j])
    return result


def is_same(mtx_A, mtx_B):
    for i in range(3):
        for j in range(3):
            if mtx_A[i][j] != mtx_B[i][j]:
                return False
    return True



"""
plot_matrix: 用来画出矩阵；
matrix为二维列表； 
block表示是否会被阻塞（True为阻塞，画图的线程阻塞们必须等待该线程释放资源后才能继续）
plt为画笔，即：import matplotlib.pyplot as plt
"""


def plot_matrix(matrix, block, plt):
    plt.subplots(figsize=(4, 4))
    rows = len(matrix)
    columns = len(matrix[0])
    plt.xlim(0, 3*rows)
    plt.ylim(0, 3*columns)
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != 0:
                # 画出一个3*3的矩形，其中左下角坐标为：(3 * j, 6 - 3 * i)，并填充颜色， 0和其他的要有区分；
                plt.gca().add_patch(plt.Rectangle((3 * j, 6 - 3 * i), 3, 3, color='#7AC7F8', alpha=1))
            else:
                plt.gca().add_patch(plt.Rectangle((3 * j, 6 - 3 * i), 3, 3, color='#93C760', alpha=1))
            plt.text(3 * j + 1.5, 7.5 - 3 * i, str(matrix[i][j]), fontsize=30, horizontalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.show(block=block)
    plt.pause(1)
    plt.close()
