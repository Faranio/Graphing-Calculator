from tkinter import *

from graph import *


def graph():
	equation = entry.get()
	draw_function(equation)


window = Tk()
window.title('Graphing Calculator')

Label(window, text='Type equation here:').pack()

entry = Entry(window)
entry.pack()

graph_button = Button(window, text='Graph', width=25, command=graph)
graph_button.pack()

window.mainloop()
