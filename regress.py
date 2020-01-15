#
# Program Title: Linear Regression 
# Program Author: Mathieu Landretti
# Course: CSCI 1523-02
# Date Created: 29 October, 2019
#

#
#
# INTRODUCTION 
# ------------
#
# This program is designed to create a simple linear regression model for a series of (x,y) coordinates
# A regression line is a linear function that best fits a data data set when plotted on a cartesian graph
#
# Data Source: This program is desinged to import the (x,y) coordinates from a comma delimited .dat file
# This programs default uses a test file named Regression.dat
#
# NOTES ABOUT GRAPHICS
# --------------------
# 
# This program utilizes the graphics module by John Zelle
# Program renders a 650x650 pixel window
# Program graphs the (x,y) coordinates, error bars, and regression lines in black
# Error bars are labled in red with its y value
# The x,y axis will be labled by increments of 5 in black
# 
# FORMULAS USED
# -------------
#
# The regression line will take the standard form y = mx + b in R^2
# Where 'm' denotes the slope
# Where 'b' denotes the y intercept
# Where 'x' denotes the independant variable
# Where 'y' denotes the dependant variable
# 
# The R**2 correlation coefficient exists in the range -1 <= R**2 <= 1
# When R**2 == +1 this indicates a strong positive correlation
# When R**2 == -1 this indicates a strong negative correlation
# When R**2  == 0 this indicates no correlation
# R**2 value is an indicator of the 'Goodness to fit' of a linear function to a scatter plot
#
# Formula used for calculating standard deviation (stdv)
# Where 'x_bar' denotes the mean of x coordinates of data set
# Where 'n' denotes the size of the dataset 
#
# stdv_x = sqrt(Σ(xi-x_bar)**2/n)
# For stdv_y, replace xi and x_bar with y
#
# Formula used for calculating R**2
# R**2 = {(1/n)*Σ[xi-x_bar]*[yi-y_bar]/(stdv_x*stdv_y)}**2
#
# Formula used for calculating 'm' or slope:
# m = Σ [(xi - x_bar)(yi - y_bar)] / Σ [(xi - x_bar)**2]
#
# Formula used to find the 'y' intercept:
# b = y_bar -(m*x_bar)
# 
# TESTING
# -------
#
# To make sure the program works properly the following should be outputtd:
# Regerssion Line: y =  1.34 x +  11.43
# R**2 Coefficent: 0.56
# Suggested chart size: 35x35
#
#


import math
# graphics module by John Zelle 
import graphics

# GRAPHICS FUNCTION
# -----------------

def main(x,y,b,m,range_axis, errorList):
	"""Please note that since datasets vary in scale, in the future, 
	I would like to give the user more control over the display.
	Currently, the only power they have is setting the axis range.
	Elements such as title, axis padding, spacing, etc. are all
	proportional to the entered "range_axis".

	Formal Parameters:
	x == x points 
	y == y points
	b == y intercept of regression line
	m == slope of regression line
	range_axis == the max range of x and y axis
	errorList == a list containing the y values that lie on regress line"""

	# max_x and max_y are used to make the x and y axis
	max_x = range_axis  
	max_y = range_axis 
	# regress variable is the y coordinate of the regression line
	regress = ((range_axis/2)*m) + b

	# x and y axis denoted by vertical lines
	y_axis = graphics.Line(graphics.Point(0,0),graphics.Point(0,range_axis))
	y_axis.setArrow('last')

	x_axis = graphics.Line(graphics.Point(0,0),graphics.Point(range_axis,0))
	x_axis.setArrow('last')

	# Plot the regression line
	regress_line = graphics.Line(graphics.Point(0,b),graphics.Point((range_axis/2), regress))
	regress_line.setFill(graphics.color_rgb(0,0,0))

	# set the color of x and y axis
	x_axis.setFill(graphics.color_rgb(0,0,0))
	y_axis.setFill(graphics.color_rgb(0,0,0))

	# Set the size of the window 
	win = graphics.GraphWin('Regression Plot', 700,700)
	
	# Set the coordinate range
	win.setCoords(-range_axis/4,-range_axis/4,range_axis+(range_axis/4),range_axis+(range_axis/4))
	win.setBackground(graphics.color_rgb(255,255,255))
	
	
	i = 0
	while len(x) > i: # This loop plots data points
		
		k = x[i] # store x value at index i
		z = y[i] # store y value at index i
		data = graphics.Point(k, z) # store as point
		data.setFill(graphics.color_rgb(0,0,0)) # set point color
		data.draw(win) # draw the point on the window
 
		i = i + 1
	
	i = 0
	while i < range_axis: # Loop sets dash mark on y axis

		y_dash = graphics.Line(graphics.Point(0,i),graphics.Point(-range_axis/(range_axis*4),i))
		y_dash.setFill(graphics.color_rgb(0,0,0))
		y_dash.draw(win)
		i = i + 1
	
	i = 0
	while i < range_axis: # Loop sets dash mark on x axis

		x_dash = graphics.Line(graphics.Point(i,0),graphics.Point(i,-range_axis/(range_axis*4)))
		x_dash.setFill(graphics.color_rgb(0,0,0))
		x_dash.draw(win)
		i = i + 1

	i = 0
	while  i < len(y):	# Plots the error bars from points to line

		err_line = graphics.Line(graphics.Point(x[i],y[i]),graphics.Point(x[i],errorList[i]))
		err_line.setFill(graphics.color_rgb(0,0,0))
		# iterates over the y values and compares them to the y values of the regression line
		if y[i] <= errorList[i]: # Graphs the error lable above the regression line if y point is above the line
			err_lable = graphics.Text(graphics.Point(x[i],y[i] -range_axis/(range_axis*2)), str(y[i]))
			err_lable.setSize(7)
			err_lable.setFill(graphics.color_rgb(255,0,0))
			err_lable.draw(win)
		else: # Graphs the error lable above the regression line if y point is below the line
			err_lable = graphics.Text(graphics.Point(x[i],y[i]+range_axis/(range_axis*2)), str(y[i]))
			err_lable.setSize(7)
			err_lable.setFill(graphics.color_rgb(255,0,0))
			err_lable.draw(win)	

		err_line.draw(win)
		i = i + 1

	i = 0
	while i < range_axis: # Lables the x axis counting by 5
		if i/5 == int(i/5):
			x_inc = graphics.Text(graphics.Point(i, -range_axis/50), str(i))
			x_inc.setSize(9)
			x_inc.draw(win)
			i = i + 1
		else: # if i is not divisible by 5, we skip the lable
			i = i + 1

	i = 0
	while i < range_axis: # Lables the y axis counting by 5
		if i/5 == int(i/5):
			y_inc = graphics.Text(graphics.Point(-range_axis/50, i), str(i))
			y_inc.setSize(9)
			y_inc.draw(win)
			i = i + 1
		else: # if i is not divisible by 5, we skip the lable
			i = i + 1

	# style of x axis lable 
	x_axisLable = graphics.Text(graphics.Point(range_axis + 1, 0), 'x')
	x_axisLable.setStyle('italic')
	x_axisLable.setFace('times roman')
	x_axisLable.setSize(14)

	# style of y axis lable
	y_axisLable = graphics.Text(graphics.Point(0, range_axis + 1), 'y')
	y_axisLable.setStyle('italic')
	y_axisLable.setFace('times roman')
	y_axisLable.setSize(14)

	# Title of graph
	title_graphic = graphics.Text(graphics.Point((range_axis/2),range_axis+(range_axis/8)),'Linear Regression Model')

	key_graphic = graphics.Text(graphics.Point(range_axis/2, -range_axis/8), '* Error Lables indicate y values of inputted data (labled in red)\
	\n* Graph scale based on user input (rescale if window does not fit data)')	
	key_graphic.draw(win)

	# Draw above to the window
	title_graphic.draw(win)
	y_axisLable.draw(win)
	x_axisLable.draw(win)
	x_axis.draw(win)
	y_axis.draw(win)
	regress_line.draw(win)

	#Closes window and exits programs
	win.getMouse()
	win.close()

# FUNCTIONS
# ---------

def programWelcome():
	"""Welcomes user to program and informs them of program requirements """

	print('Welcome to my linear regression program')
	print(format('-','-<40'))
	print('Please make sure the data set you would like analyzed has the following: ')
	print( '1. (x,y) coordinates are comma delimited \n2. File is in same directory as program \n3. File has .dat extension')
	print(format('-','-<40'),'\n')

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
	""" Finds the R**2 Correlation Coefficent 
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

	return y_points

# EXTRACTING AND FORMATTING DATA 
# ------------------------------

# Display the program welcome informs user about program use and parameters
programWelcome()

# We assign a variable with the external .dat file containing (x,y) coordiantes
# Set the argument to 'r' since we will need to read the data
regression_data = input('Please input file name: ')
valid = False
while not valid:
	try:
		regression_data = open(regression_data)
		valid = True
	except IOError:
		print('The file could not be found. Make sure it is in the right directory or is spelled correctly.')
		regression_data = input('\nPlease input file name: ')

# Below are two empty lists that will contain (x,y)
# This list will hold the 'x' values
x_values = []
# This list will hold the 'y' values
y_values = []
# empy string is used to determine when the program should stop reading the .dat file
empty_str= ''
# boolean flag used to break while loop
end_of_file = False

# while loop will iterate through all the data file until end_of_file is True
while not end_of_file:
	# program will read the .dat file line by line
	# .dat file is is formatted as follows:
	# x,y 
	xy_line = regression_data.readline()

	# When the the readline() has nothing to read, it will break the loop.
	# A list containing only x values will be printed
	# A list containing only y values will be printed
	if xy_line == empty_str:

		end_of_file = True
		

	else:
		# xy_line will hold both (x,y) coordinates and store them as a list with a length of 
		# Both (x,y) coordinates are held as string values
		# We will store these independant values in all_values
		all_values = xy_line.strip().split(',')
		
		# Here, we iterate over all_values
		# Each line is held in a list with len of 2
		# Thus index values are [0] and [1] (we are in R^2)
		# Note that we convert from string to float value
		for k in all_values:
			#if index is [0] it is stored as an 'x' value
			if k == all_values[0]:
				x_values.append(float(k))
			# if index is [1] it is stored as an 'y' value
			else:
				y_values.append(float(k))

#REGRESSION CALCULATION
#----------------------

# x_bar is the mean of all 'x' values
# formula (1/n)*Σx
x_bar = meanBar(x_values)

# y_bar is the mean of all 'y' values
# formula (1/n)*Σy
y_bar = meanBar(y_values)

m = slope(x_values, y_values, x_bar, y_bar)

stdev_x = stDev(x_values, x_bar)
stdev_y = stDev(y_values, y_bar)

# Calculate the R^2 correlation coefficent
R = rCorr(x_values, y_values, x_bar,y_bar,stdev_x,stdev_y)

# Calculate the y intercept
b = y_intercept(x_bar, y_bar, m)

# Calcualate all of  the y values on the line to be used to plot error bars
errorList = errorPoints(x_values, b, m)

# USER DISPLAY
# ------------

# Ask user if they would like to continue with program or go back and edit data
proceed = input('Would you like to proceed? [y/n] ')
# Boolean flag to kill loops
boolean = True

while boolean == True:

	if proceed == 'y':

		
		#Display the regression line in y = mx + b form and R^2 correlation coefficent
		print('\nBelow is the regression line in y = mx + b format (rounded to 2 decimal places) :\n ')
		print('y = ',format(m, '.2f'),'x + ',format(b, '.2f'))
		print('With an R^2 correlation coefficent', format(R, '.2f'))
		boolean = False
		# Ask user if they would like to see a regression chart
		graphic = input('\nWould you like to see a graphic? [y/n] ')
		boolean_2 = True # New boolean flag to break following loops

		while boolean_2 == True:

			if graphic == 'y':
				print('The maxium x value is ',max(x_values),'The maxium y value is ',max(y_values))
				# ask user to set the range of  the x,y plot using the largest value in dataset
				print('For the best view, set the range to the largest number in your dataset')
				range_axis = float(input('Please set the range of the x,y plot (e.g 5 yields a 5 x 5 chart): '))
				# Call the 'main' function to display the chart
				main(x_values,y_values, b,m, range_axis, errorList)
				boolean_2 == False
			# Exit the program
			elif graphic == 'n': 
				boolean_2 = False
				print('See you around!')
				

			else:
				print("That ain't a valid option bucko")
				graphic = input('\nWould you like to see a graphic? [y/n]')

	elif proceed == 'n': # Tells user to reformat data and try again
		print('Well I hope you can format your data right')
		print('See ya later')
		boolean = False

	else: # if user fails to input [y/n] ask again 
		print('Sorry ',proceed,'could not be understood')
		proceed = input('Would you like to proceed? [y/n] ')
