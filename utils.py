def get_ranges(x_range, y_range):
	x_start, x_end = x_range[0].get(), x_range[1].get()
	y_start, y_end = y_range[0].get(), y_range[1].get()
	
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
