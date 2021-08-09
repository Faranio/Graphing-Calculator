import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from math import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

X_RANGE = [-10, 11]
Y_RANGE = []


def draw_function(function):
	global Y_RANGE
	plt.clf()
	x_values = np.linspace(*X_RANGE, 1000)
	y_values = []
	
	for x in x_values:
		y = eval(function)
		y_values.append(y)
	
	Y_RANGE.append(min(y_values))
	Y_RANGE.append(max(y_values))
	
	plt.xlim(*X_RANGE)
	plt.ylim(*Y_RANGE)
	plt.grid()
	plt.plot(x_values, y_values)
	fig.canvas.draw()
	
	Y_RANGE = []


def graph():
	equation = entry.get()
	draw_function(equation)


matplotlib.use('TkAgg')
fig = plt.figure(1)

window = Tk()
window.title('Graphing Calculator')

canvas = FigureCanvasTkAgg(fig, master=window)
plot_widget = canvas.get_tk_widget()
plot_widget.pack()

Label(window, text='Type equation here:').pack()

entry = Entry(window)
entry.pack()

graph_button = Button(window, text='Graph', width=25, command=graph)
graph_button.pack()

window.mainloop()
