import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

from math import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


EQUATIONS = set()


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


def plot_in_interval(function, x_values):
	y_values = []
	
	for x in x_values:
		y = eval(function)
		y_values.append(y)
	
	plt.plot(x_values, y_values, label=function)
	

def graph_function(function):
	global EQUATIONS
	EQUATIONS.add(function)
	plt.clf()
	
	X_RANGE, Y_RANGE = get_ranges()
	x_values = np.linspace(*X_RANGE, 1000)
	
	plt.xlim(*X_RANGE)
	plt.ylim(*Y_RANGE)
	plt.grid(True)
		
	for function in EQUATIONS:
		plot_in_interval(function, x_values)
	
	plt.legend()
	plt.axhline(0, color='black')
	plt.axvline(0, color='black')
	fig.canvas.draw()
	
	
def clear():
	global EQUATIONS
	EQUATIONS = set()
	equation_entry.delete(0, 'end')
	x_range_entry_start.delete(0, 'end')
	x_range_entry_end.delete(0, 'end')
	y_range_entry_start.delete(0, 'end')
	y_range_entry_end.delete(0, 'end')
	plt.clf()
	fig.canvas.draw()
	
	
def close():
	sys.exit(0)


def graph():
	equation = equation_entry.get()
	graph_function(equation)


matplotlib.use('TkAgg')
fig = plt.figure(1)

window = Tk()
window.geometry('700x720')
window.title('Graphing Calculator')

canvas = FigureCanvasTkAgg(fig, master=window)
plot_widget = canvas.get_tk_widget()
plot_widget.pack()

Label(window, text='Type equation here:').pack()
equation_entry = Entry(window)
equation_entry.pack()

x_range_label_start = Label(window, text='X range start:')
x_range_label_start.pack()
x_range_label_start.place(border=OUTSIDE, x=215, y=530)
x_range_entry_start = Entry(window)
x_range_entry_start.pack()
x_range_entry_start.place(border=OUTSIDE, x=175, y=550)

x_range_label_end = Label(window, text='X range end:')
x_range_label_end.pack()
x_range_label_end.place(border=OUTSIDE, x=400, y=530)
x_range_entry_end = Entry(window)
x_range_entry_end.pack()
x_range_entry_end.place(border=OUTSIDE, x=360, y=550)

y_range_label_start = Label(window, text='Y range start:')
y_range_label_start.pack()
y_range_label_start.place(border=OUTSIDE, x=215, y=575)
y_range_entry_start = Entry(window)
y_range_entry_start.pack()
y_range_entry_start.place(border=OUTSIDE, x=175, y=595)

y_range_label_end = Label(window, text='Y range end:')
y_range_label_end.pack()
y_range_label_end.place(border=OUTSIDE, x=400, y=575)
y_range_entry_end = Entry(window)
y_range_entry_end.pack()
y_range_entry_end.place(border=OUTSIDE, x=360, y=595)

graph_button = Button(window, text='Graph', width=84, command=graph)
graph_button.pack()
graph_button.place(border=OUTSIDE, x=0, y=630)

clear_button = Button(window, text='Clear', width=84, command=clear)
clear_button.pack()
clear_button.place(border=OUTSIDE, x=0, y=660)

exit_button = Button(window, text='Exit', width=84, command=close)
exit_button.pack()
exit_button.place(border=OUTSIDE, x=0, y=690)

window.mainloop()
