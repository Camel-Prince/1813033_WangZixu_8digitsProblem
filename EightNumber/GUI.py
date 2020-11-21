from main import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
root = Tk()
root.title("tkinter and matplotlib")
f = Figure(figsize=(10, 10), dpi=100)#figsize定义图像大小，dpi定义像素
f_plot = f.add_subplot(111)#定义画布中的位置

Button(root, text='pic', command=perform_plot_BFS(root_matrix, dest_matrix)).pack()
Button(root, text='pic2').pack()
Button(root, text='pic3').pack()
canvs = FigureCanvasTkAgg(f, root)#f是定义的图像，root是tkinter中画布的定义位置
canvs.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
root.mainloop()