import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from math import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


EQUATIONS = {}
INDEX = 1
WIDTH, HEIGHT = 640, 760


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
	new_x_values = []
	y_values = []
	
	for x in x_values:
		try:
			y = eval(function)
		except (NameError, SyntaxError):
			listbox_error.place_forget()
			equation_entry_error.place(border=OUTSIDE, x=185, y=490)
			return -1
		except ValueError:
			continue
			
		new_x_values.append(x)
		y_values.append(y)
	
	try:
		plt.plot(new_x_values, y_values, label=function)
	except TypeError:
		listbox_error.place_forget()
		equation_entry_error.place(border=OUTSIDE, x=185, y=490)
		return -1
	
	equation_entry_error.place_forget()
	return 1
	

def graph_function(function):
	global EQUATIONS, INDEX
	
	add = False
	function = function.lower()
	listbox_error.place_forget()
	
	if len(EQUATIONS) == 0 or function not in EQUATIONS.values():
		EQUATIONS[INDEX] = function
		add = True
		
	plt.clf()
	
	X_RANGE, Y_RANGE = get_ranges()
	x_values = np.linspace(*X_RANGE, 1000)
	
	plt.xlim(*X_RANGE)
	plt.ylim(*Y_RANGE)
	plt.grid(True)
		
	for function in EQUATIONS.values():
		result = plot_in_interval(function, x_values)
		
		if result == -1:
			for k, v in EQUATIONS.items():
				if v == function:
					del EQUATIONS[k]
					break
			return
		
	if add:
		listbox.insert(INDEX, function)
		INDEX += 1
	
	plt.legend()
	plt.axhline(0, color='black')
	plt.axvline(0, color='black')
	fig.canvas.draw()
	
	
def remove():
	listbox_error.place_forget()
	equation_entry_error.place_forget()
	
	try:
		anchor = listbox.get(listbox.curselection())
	except Exception:
		listbox_error.place(border=OUTSIDE, x=185, y=490)
		return
	
	for k, v in EQUATIONS.items():
		if v == anchor:
			del EQUATIONS[k]
			break
	
	listbox.delete(ANCHOR)
	plt.clf()
	
	if len(EQUATIONS) == 0:
		fig.canvas.draw()
		return
	
	X_RANGE, Y_RANGE = get_ranges()
	x_values = np.linspace(*X_RANGE, 1000)
	
	plt.xlim(*X_RANGE)
	plt.ylim(*Y_RANGE)
	plt.grid(True)
	
	for function in EQUATIONS.values():
		plot_in_interval(function, x_values)
	
	plt.legend()
	plt.axhline(0, color='black')
	plt.axvline(0, color='black')
	fig.canvas.draw()
	
	
def clear():
	global EQUATIONS, INDEX
	
	listbox_error.place_forget()
	equation_entry_error.place_forget()
	EQUATIONS = {}
	listbox.delete(0, INDEX)
	INDEX = 1
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
window.geometry(f'{WIDTH}x{HEIGHT}')
window.title('Graphing Calculator')

canvas = FigureCanvasTkAgg(fig, master=window)
plot_widget = canvas.get_tk_widget()
plot_widget.pack()

equation_label = Label(window, text='Type equation here:')
equation_label.pack()
equation_label.place(border=OUTSIDE, y=480)
equation_entry = Entry(window)
equation_entry.pack()
equation_entry.place(border=OUTSIDE, y=501)

equation_entry_error = Label(window, text='ERROR! Incorrect equation!\nUse only x variable.', fg='red')
equation_entry_error.pack_forget()

listbox_error = Label(window, text='ERROR! Please choose an\nequation to remove.', fg='red')
listbox_error.pack_forget()

equation_label = Label(window, text='Plotted equations:')
equation_label.pack()
equation_label.place(border=OUTSIDE, x=400, y=480)
listbox = Listbox(window, height=7)
listbox.pack()
listbox.place(border=OUTSIDE, x=400, y=501)

x_range_label_start = Label(window, text='X range start:')
x_range_label_start.pack()
x_range_label_start.place(border=OUTSIDE, y=535)
x_range_entry_start = Entry(window)
x_range_entry_start.pack()
x_range_entry_start.place(border=OUTSIDE, y=555)

x_range_label_end = Label(window, text='X range end:')
x_range_label_end.pack()
x_range_label_end.place(border=OUTSIDE, x=185, y=535)
x_range_entry_end = Entry(window)
x_range_entry_end.pack()
x_range_entry_end.place(border=OUTSIDE, x=185, y=555)

y_range_label_start = Label(window, text='Y range start:')
y_range_label_start.pack()
y_range_label_start.place(border=OUTSIDE, y=589)
y_range_entry_start = Entry(window)
y_range_entry_start.pack()
y_range_entry_start.place(border=OUTSIDE, y=609)

y_range_label_end = Label(window, text='Y range end:')
y_range_label_end.pack()
y_range_label_end.place(border=OUTSIDE, x=185, y=589)
y_range_entry_end = Entry(window)
y_range_entry_end.pack()
y_range_entry_end.place(border=OUTSIDE, x=185, y=609)

graph_button = Button(window, text='Graph', width=77, command=graph)
graph_button.pack()
graph_button.place(border=OUTSIDE, y=640)

remove_button = Button(window, text='Remove', width=77, command=remove)
remove_button.pack()
remove_button.place(border=OUTSIDE, y=670)

clear_button = Button(window, text='Clear', width=77, command=clear)
clear_button.pack()
clear_button.place(border=OUTSIDE, y=700)

exit_button = Button(window, text='Exit', width=77, command=close)
exit_button.pack()
exit_button.place(border=OUTSIDE, y=730)

window.mainloop()
