import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from math import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


def get_ranges():
	x_start, x_end = x_range_entry_start.get(), x_range_entry_end.get()
	y_start, y_end = y_range_entry_start.get(), y_range_entry_end.get()
	
	if len(x_start) == 0:
		x_start = -1
	else:
		x_start = float(x_start)
	
	if len(x_end) == 0:
		x_end = 1
	else:
		x_end = float(x_end)
		
	if len(y_start) == 0:
		y_start = -1
	else:
		y_start = float(y_start)
		
	if len(y_end) == 0:
		y_end = 1
	else:
		y_end = float(y_end)
		
	return [x_start, x_end], [y_start, y_end]
	

def draw_function(function):
	X_RANGE, Y_RANGE = get_ranges()
	
	x_values = np.linspace(*X_RANGE, 1000)
	y_values = []
	
	for x in x_values:
		y = eval(function)
		y_values.append(y)
	
	plt.xlim(*X_RANGE)
	plt.ylim(*Y_RANGE)
	plt.grid(True)
	plt.plot(x_values, y_values)
	plt.axhline(0, color='black')
	plt.axvline(0, color='black')
	fig.canvas.draw()
	
	
def clear():
	equation_entry.delete(0, 'end')
	x_range_entry_start.delete(0, 'end')
	x_range_entry_end.delete(0, 'end')
	y_range_entry_start.delete(0, 'end')
	y_range_entry_end.delete(0, 'end')
	plt.clf()
	fig.canvas.draw()


def graph():
	equation = equation_entry.get()
	draw_function(equation)


matplotlib.use('TkAgg')
fig = plt.figure(1)

window = Tk()
window.title('Graphing Calculator')

canvas = FigureCanvasTkAgg(fig, master=window)
plot_widget = canvas.get_tk_widget()
plot_widget.pack()

Label(window, text='Type equation here:').pack()
equation_entry = Entry(window)
equation_entry.pack()

Label(window, text='X range start:').pack()
x_range_entry_start = Entry(window)
x_range_entry_start.pack()

Label(window, text='X range end:').pack()
x_range_entry_end = Entry(window)
x_range_entry_end.pack()

Label(window, text='Y range start:').pack()
y_range_entry_start = Entry(window)
y_range_entry_start.pack()

Label(window, text='Y range end:').pack()
y_range_entry_end = Entry(window)
y_range_entry_end.pack()

clear_button = Button(window, text='Clear', width=25, command=clear)
clear_button.pack()

graph_button = Button(window, text='Graph', width=25, command=graph)
graph_button.pack()

window.mainloop()
