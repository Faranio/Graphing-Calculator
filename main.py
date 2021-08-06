from math import *

import matplotlib.pyplot as plt
import numpy as np


def get_input():
	equation = str(input())
	return equation


def draw_function(equation):
	x_values = np.linspace(-10, 11, 1000)
	y_values = []
	
	for x in x_values:
		y = eval(equation)
		y_values.append(y)
		
	plt.plot(x_values, y_values)
	plt.show()


def main():
	equation = get_input()
	draw_function(equation)
	

if __name__ == "__main__":
	main()
