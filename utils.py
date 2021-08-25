def get_ranges(x_range, y_range):
	x_start, x_end = x_range[0].get(), x_range[1].get()
	y_start, y_end = y_range[0].get(), y_range[1].get()
	
	x_start = -1 if len(x_start) == 0 else float(x_start)
	x_end = 1 if len(x_end) == 0 else float(x_end)
	y_start = -1 if len(y_start) == 0 else float(y_start)
	y_end = 1 if len(y_end) == 0 else float(y_end)
	
	return [x_start, x_end], [y_start, y_end]
