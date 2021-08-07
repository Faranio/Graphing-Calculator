from math import *

import matplotlib.pyplot as plt
import numpy as np

X_RANGE = [-10, 11]
Y_RANGE = []


def get_input():
	equation = str(input())
	return equation


def draw_function(equation):
	x_values = np.linspace(*X_RANGE, 1000)
	y_values = []
	
	for x in x_values:
		y = eval(equation)
		y_values.append(y)
	
	Y_RANGE.append(min(y_values))
	Y_RANGE.append(max(y_values))
	
	plt.xlim(*X_RANGE)
	plt.ylim(*Y_RANGE)
	plt.grid()
	plt.plot(x_values, y_values)
	plt.show()


def main():
	equation = get_input()
	draw_function(equation)


if __name__ == "__main__":
	main()
