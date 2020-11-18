from utils import *
import matplotlib.pyplot as plt
from BFS import bfs
from DFS import dfs

# root_matrix = [[1, 2, 4], [6, 3, 0], [8, 5, 7]]
# dest_matrix = [[4, 2, 6], [1, 0, 7], [8, 3, 5]]
root_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
dest_matrix = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]

'''搜索并记录路径'''
dfs(root_matrix, dest_matrix)
print("DFS Done!")
fill_path_stack(dest_matrix)

'''打印路径、动态地画出图'''
i = 0
while path_stack.__len__() != 0:
    print("Step {}".format(i))
    i += 1
    the_matrix = path_stack.pop()
    show(the_matrix)
    plot_matrix(the_matrix, block=False, plt=plt)
print("Step {}".format(i))
show(dest_matrix)
plot_matrix(dest_matrix, block=True, plt=plt)


