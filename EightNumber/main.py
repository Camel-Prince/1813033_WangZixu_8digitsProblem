
from BFS import *
from DFS import *
from A_Star import *
root_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# dest_matrix = [[8, 2, 1], [3, 4, 0], [7, 5, 6]]
# dest_matrix = [[7, 4, 3], [0, 2, 1], [8, 5, 6]]
dest_matrix = [[1, 5, 2], [0, 4, 3], [7, 8, 6]]
# perform_plot_BFS(root_matrix, dest_matrix)
perform_plot_A_Star(root_matrix, dest_matrix)
# perform_plot_DFS(root_matrix, dest_matrix)