import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from math import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

import utils


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
	
	
class GraphingCalculator:
	def __init__(self, width=640, height=760, title='Graphing Calculator'):
		matplotlib.use('TkAgg')
		self.equations = {}
		self.index = 1
		self.width = width
		self.height = height
		
		self.equation_entry = None
		self.x_range_entry_start = None
		self.x_range_entry_end = None
		self.y_range_entry_start = None
		self.y_range_entry_end = None
		
		self.listbox = None
		
		self.equation_entry_error = None
		self.listbox_error = None
		
		self.fig = plt.figure(1)
		self.window = Tk()
		self.window.geometry(f'{self.width}x{self.height}')
		self.window.title(title)
		
		self.create_layout()
		self.window.mainloop()
		
	def create_layout(self):
		canvas = FigureCanvasTkAgg(self.fig, master=self.window)
		plot_widget = canvas.get_tk_widget()
		plot_widget.pack()
		
		self.create_labels()
		self.create_entries()
		self.create_buttons()
		self.create_listbox()
		self.define_errors()
		
	def create_labels(self):
		equation_label = Label(self.window, text='Type equation here:')
		equation_label.pack()
		equation_label.place(border=OUTSIDE, y=480)
		
		equations_label = Label(self.window, text='Plotted equations:')
		equations_label.pack()
		equations_label.place(border=OUTSIDE, x=400, y=480)
		
		x_range_label_start = Label(self.window, text='X range start:')
		x_range_label_start.pack()
		x_range_label_start.place(border=OUTSIDE, y=535)
		
		x_range_label_end = Label(self.window, text='X range end:')
		x_range_label_end.pack()
		x_range_label_end.place(border=OUTSIDE, x=185, y=535)
		
		y_range_label_start = Label(self.window, text='Y range start:')
		y_range_label_start.pack()
		y_range_label_start.place(border=OUTSIDE, y=589)
		
		y_range_label_end = Label(self.window, text='Y range end:')
		y_range_label_end.pack()
		y_range_label_end.place(border=OUTSIDE, x=185, y=589)
		
	def create_entries(self):
		self.equation_entry = Entry(self.window)
		self.equation_entry.pack()
		self.equation_entry.place(border=OUTSIDE, y=501)
		
		self.x_range_entry_start = Entry(self.window)
		self.x_range_entry_start.pack()
		self.x_range_entry_start.place(border=OUTSIDE, y=555)
		
		self.x_range_entry_end = Entry(self.window)
		self.x_range_entry_end.pack()
		self.x_range_entry_end.place(border=OUTSIDE, x=185, y=555)
		
		self.y_range_entry_start = Entry(self.window)
		self.y_range_entry_start.pack()
		self.y_range_entry_start.place(border=OUTSIDE, y=609)
		
		self.y_range_entry_end = Entry(self.window)
		self.y_range_entry_end.pack()
		self.y_range_entry_end.place(border=OUTSIDE, x=185, y=609)
		
	def create_buttons(self):
		graph_button = Button(self.window, text='Graph', width=77, command=self.graph)
		graph_button.pack()
		graph_button.place(border=OUTSIDE, y=640)
		
		remove_button = Button(self.window, text='Remove', width=77, command=self.remove)
		remove_button.pack()
		remove_button.place(border=OUTSIDE, y=670)
		
		clear_button = Button(self.window, text='Clear', width=77, command=clear)
		clear_button.pack()
		clear_button.place(border=OUTSIDE, y=700)
		
		exit_button = Button(self.window, text='Exit', width=77, command=close)
		exit_button.pack()
		exit_button.place(border=OUTSIDE, y=730)
		
	def create_listbox(self):
		self.listbox = Listbox(self.window, height=7)
		self.listbox.pack()
		self.listbox.place(border=OUTSIDE, x=400, y=501)
		
	def define_errors(self):
		self.equation_entry_error = Label(self.window, text='ERROR! Incorrect equation!\nUse only x variable.', fg='red')
		self.equation_entry_error.pack_forget()
		
		self.listbox_error = Label(self.window, text='ERROR! Please choose an\nequation to remove.', fg='red')
		self.listbox_error.pack_forget()
	
	def graph(self):
		function = self.equation_entry.get()
		
		add = False
		function = function.lower()
		self.listbox_error.place_forget()
		
		if len(self.equations) == 0 or function not in self.equations.values():
			self.equations[self.index] = function
			add = True
		
		plt.clf()
		
		X_RANGE, Y_RANGE = utils.get_ranges((self.x_range_entry_start, self.x_range_entry_end),
		                                    (self.y_range_entry_start, self.y_range_entry_end))
		x_values = np.linspace(*X_RANGE, 1000)
		
		plt.xlim(*X_RANGE)
		plt.ylim(*Y_RANGE)
		plt.grid(True)
		
		for function in self.equations.values():
			result = plot_in_interval(function, x_values)
			
			if result == -1:
				for k, v in self.equations.items():
					if v == function:
						del self.equations[k]
						break
				return
		
		if add:
			self.listbox.insert(self.index, function)
			self.index += 1
		
		plt.legend()
		plt.axhline(0, color='black')
		plt.axvline(0, color='black')
		self.fig.canvas.draw()
	
	def remove(self):
		self.listbox_error.place_forget()
		self.equation_entry_error.place_forget()
		
		try:
			anchor = self.listbox.get(self.listbox.curselection())
		except Exception:
			self.listbox_error.place(border=OUTSIDE, x=185, y=490)
			return
		
		for k, v in self.equations.items():
			if v == anchor:
				del self.equations[k]
				break
		
		self.listbox.delete(ANCHOR)
		plt.clf()
		
		if len(EQUATIONS) == 0:
			self.fig.canvas.draw()
			return
		
		X_RANGE, Y_RANGE = utils.get_ranges((self.x_range_entry_start, self.x_range_entry_end),
		                                    (self.y_range_entry_start, self.y_range_entry_end))
		x_values = np.linspace(*X_RANGE, 1000)
		
		plt.xlim(*X_RANGE)
		plt.ylim(*Y_RANGE)
		plt.grid(True)
		
		for function in self.equations.values():
			plot_in_interval(function, x_values)
		
		plt.legend()
		plt.axhline(0, color='black')
		plt.axvline(0, color='black')
		self.fig.canvas.draw()
