#
# Program Title: Basic Statisitcs Tools
# Program Author: Mathieu Landretti
# Date Created: 22 November, 2019  
#

import math, graphics, random

def meanBar(list_value):
	""" Calculates the x_bar or y_bar (mean) of given list
	Formal Parameters:
	list_value == list that you want to get the mean of"""

	var_bar = sum(list_value)/len(list_value)
	return var_bar

def stDev(list_value, mean):
	""" Finds the Standard Deviation of any inputted list
	Formal Parameters:
	list_value == list of values to be calculated
	mean == the mean of the list being calculated"""

	n = len(list_value)
	dev = [((a - mean)**2)/n for a in list_value]
	stdev = math.sqrt(sum(dev))
	return stdev

def slope(list_value1, list_value2, mean1, mean2):
	"""Find the slope (m) of Regression line
	Formal Parameters:
	list_value1 == x values
	list_value2 == y values
	mean1 == x bar
	mean2 == y bar"""

	a =[(k - mean1) for k in list_value1]
	b = [(k - mean2) for k in list_value2]
	c = []

	i = 0
	while i < len(a):

		z = a[i] * b[i]
		c.append(z)
		i = i + 1

	sum1 = sum(c)
	d = [(k - mean1)**2 for k in list_value1]
	sum2 = sum(d)
	slope = sum1 / sum2

	return slope

def rCorr(list_value1,list_value2,mean1,mean2,stDev1,stDev2):
	""" Finds the R**2 Correlation Coefficent in 2 dimensions
	Formal Parameters:
	list_value1 == x points
	list_value2 == y points
	mean1 == mean of x values
	mean2 == mean of y values
	stDev1 == standard deviation of x values
	stDev2 == standard deviation of y values"""
	
	n = len(list_value1)
	a =[(k - mean1) for k in list_value1]
	b = [(k - mean2) for k in list_value2]
	c = []

	i = 0
	while i < len(a):

		z = a[i] * b[i]
		c.append(z)
		i = i + 1

	c = [k/(stDev1*stDev2) for k in c ]
	sum1 = sum(c)

	Rsqr = ((1/n)*sum1)**2 
	return Rsqr

def y_intercept(x_bar,y_bar,slope):
	""" Returns the y intercept of regression line
	Formal Parameters:
	x_bar == mean of x values
	y_bar == mean of y values
	slope == m value of regression line"""
	y_intercept = y_bar -(x_bar*slope)
	return y_intercept

def errorPoints(x_points,y_intercept,slope):
	"""Makes a list of the y values that lie on the regerssion line that 
	correspond with the x values 
	Formal Parameters:
	x_points == x values of dataset
	y_intercept == b value of the regerssionline
	slope == m value of the regerssion line"""
	y_points = []
	
	i = 0
	while i < len(x_points):
		y = (x_points[i]*slope) + y_intercept
		y_points.append(y)
		i = i + 1

	return y_point

def curveSketch(x_list,y_list,x_scale,y_scale,plot_title = 'Curve Sketch'):
	"""Will render a simple x,y plot in R^2. Program takes two
	equally sized lists (one representing x values and the other 
	y values) and plots them on the chart. It will then draw a line
	between every point, and if the points construct a curve, it will
	be approximatly represented on the chart.

	Formal parameters:
	x_list == list of x points 
	y_list == list of y points
	x_scale == user set range of x and y axis
	plot_title == user given title (defaults to 'Scatter Plot')"""

	win = graphics.GraphWin(plot_title,650,650)
	# Set the coordinates proportinal to the entered scale
	win.setCoords(-x_scale-(x_scale/4),-x_scale-(x_scale/4),x_scale+(x_scale/4),y_scale+(y_scale/4))
	# Set backgrount to white
	win.setBackground(graphics.color_rgb(255,255,255))
	# Plot the x and y axis to make a 4 quadrent graph
	x_axis = graphics.Line(graphics.Point(-x_scale,0),graphics.Point(x_scale,0))
	y_axis = graphics.Line(graphics.Point(0,-y_scale),graphics.Point(0,y_scale))

	# Draw arrow to each end of graph
	x_axis.setArrow('both')
	y_axis.setArrow('both')
	# Draw onto window
	x_axis.draw(win)
	y_axis.draw(win)

	# Render dash marks on the x axis
	i = -x_scale + 1
	while i < x_scale:

		x_dash = graphics.Line(graphics.Point(i,0),graphics.Point(i,-x_scale/70))
		x_dash.draw(win)
		i = i + 1

	# Render dash marks on the y axis
	i = -y_scale + 1
	while i < y_scale:

		y_dash = graphics.Line(graphics.Point(0,i),graphics.Point(-x_scale/70,i))
		y_dash.draw(win)
		i = i + 1

	# lable the x axis
	i = -x_scale + 1
	while i < x_scale:

		if i == 0: # do not lable 0 it is implied (plotted at point of intersection will look messy)
			i = i + 1
		else:
			x_lable = graphics.Text(graphics.Point(i,-x_scale/30), str(i))
			x_lable.setSize(7)
			x_lable.draw(win)
			i = i + 1

	# lable the y axis
	i = -y_scale + 1
	while i < y_scale:

		if i == 0:  # do not lable 0 it is implied (plotted at point of intersection will look messy)
			i = i + 1
		else:
			y_lable = graphics.Text(graphics.Point(-x_scale/30,i), str(i))
			y_lable.setSize(7)
			y_lable.draw(win)
			i = i + 1

	x_mark = graphics.Text(graphics.Point(x_scale + x_scale/50, 0), 'x')
	x_mark.draw(win)

	y_mark = graphics.Text(graphics.Point(0, -y_scale - y_scale/50), 'y')
	y_mark.draw(win)

	# Plotting of the points
	if len(x_list) == len(y_list):
		i = 0

		while i < len(x_list): # stop loop when you get to the end of list

			# Plot every point onto the chart
			point = graphics.Point(x_list[i],y_list[i])
			point.draw(win)
			point.setFill('Red')
			if i + 1 < len(x_list): # draw line segment from current point to next point in list
			# does not incldue last point of list because program draws the next point and range error will be thrown
				viz = graphics.Line(graphics.Point(x_list[i],y_list[i]),graphics.Point(x_list[i+1],y_list[i+1]))
				viz.setFill('Blue') # Color each line segment blue
				viz.draw(win)

			i = i + 1
	else: # if the lists are not the same lenth an error message will be displayed
		print('lists not of same length')
	# Title of chart set by user defaults to curve sketch
	title = graphics.Text(graphics.Point(0,y_scale+y_scale/8), plot_title)
	title.draw(win)

	win.getMouse()

def histogram(values,x_scale,plot_title = 'Histogram'):
	""" In development"""
	
	win = graphics.GraphWin(plot_title,650,650)

	
	win.setBackground(graphics.color_rgb(255,255,255))
	x_axis = graphics.Line(graphics.Point(0,0),graphics.Point(x_scale,0))
	y_axis = graphics.Line(graphics.Point(0,0),graphics.Point(0,x_scale))


	x_axis.setArrow('last')
	y_axis.setArrow('last')

	x_axis.draw(win)
	y_axis.draw(win)

	v = []
	for k in values:
		z = k
		for i in z:
			v.append(i)

	hist_range = max(v) - min(v)
	sample_size = len(v)
	intervals = int(math.sqrt(sample_size))
	class_width = hist_range / intervals

	#find frequency 
	values.sort()
	unique = []
	frequency = []
	for k in values:
		num_reps = len(k)
		unq = k[0]
		unique.append(unq)
		frequency.append(num_reps)

	#mean = sum(unique)/len(unique)
	#n = len(unique)
	#dev = [((a - mean)**2)/n for a in unique]
	#inc = math.sqrt(sum(dev))

	i = 0
	while i < x_scale:

		x_dash = graphics.Line(graphics.Point(i,0),graphics.Point(i,-x_scale/70))
		x_dash.draw(win)
		i = i + class_width

	i = 0
	while i < x_scale:

		y_dash = graphics.Line(graphics.Point(0,i),graphics.Point(-x_scale/70,i))
		y_dash.draw(win)
		i = i + 1


	i = 0
	while i < x_scale:

		y_lable = graphics.Text(graphics.Point(-x_scale/30,i), str(i))
		y_lable.setSize(7)
		y_lable.draw(win)
		i = i + 1
	k = 0
	i = 0
	while k < x_scale:

		x_lable = graphics.Text(graphics.Point(i,-x_scale/30), str(k))
		x_lable.setSize(7)
		x_lable.draw(win)
		i = i + class_width
		k = k + 1

	x_mark = graphics.Text(graphics.Point(x_scale + x_scale/50, 0), 'x')
	x_mark.draw(win)

	y_mark = graphics.Text(graphics.Point(0, x_scale + x_scale/50), 'y')
	y_mark.draw(win)

	# Plotting of bars
	#bar = graphics.Rectangle(graphics.Point(class_width*(i-1),frequency[i-1]),graphics.Point(class_width*i,0))

	i = 0
	while i  < len(unique):

		bar = graphics.Rectangle(graphics.Point(class_width*(i+1),frequency[i]),graphics.Point(class_width*i,0))	
		bar.setFill('Blue')
		bar.draw(win)
		i = i + 1
	win.setCoords(-x_scale/4,-x_scale/4,class_width*len(unique),x_scale+(x_scale/4))
	title = graphics.Text(graphics.Point(x_scale/2,x_scale+x_scale/8), plot_title)
	title.draw(win)

	win.getMouse()
