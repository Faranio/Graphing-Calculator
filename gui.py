import tkinter

from graph import *

window = tkinter.Tk()
window.title('Graphing Calculator')
calc_button = tkinter.Button(window, text='Calculate', width=25, command=draw_function)
calc_button.pack()
window.mainloop()
