#
# Program Title: Pi Estimation
# Program Author: Mathieu Landretti
# Creation Date: 29 November, 2019
#

# INTRODUCTION
# ------------

#
# This program utilizes the Monte-Carlo method of probability analysis
# The Monte-Carlo method uses randomly generate data to approximate or forcast a result
# Monte-Carlo medthod requirements:
#	1. Set simulations domain/parameters
#	2. Generate and map random points over the defined domain
#	3. The more uniform the distribution of random data, the more accurate
#	4. Preform deterministic computation of inputs (If inputs are the same, output is the same)
#	5. Aggregate results
# For estimating pi, we use the above method to create a limit that approaches pi.
# To construct this we use geometry. We know that circles have a direct relationship with pi.
#
# We know that:
# pi = circumference / diameter
# Circle Area = pi*(radius**2)
#
# Thus, we can infer that if radius = 1, then the area of the circle is = pi
# We then know that if we fill the circle completeley with data points, we will approach the value of pi
# We can construct a diagram by placing a circle with a radius of 1 inside of a 2 x 2 square
# Using the random module, we generate a series of (x,y) points within that 2 x 2 square
# We then plot the points on the diagram. If the point falls within the square it is counted. 
#
# We can use this data to estimate the value of pi by using this formula:
# pi approximate = 4 * (points in circle / number of points generated)
#
# What we are doing is multiplying the area of the square by the ratio of points in the circle and the total points
# Note that the more points (trials) generated, the more accurate the approximation  will be
# What we have created is a limit. As the points generated approaches infinity, the approximate will approach pi.
#

# Program utilizes John Zelle's grapics module
# Program utilizes my simple statistics modeule
import math, random, statistics, graphics

def piViz():
	""" Estimates the value of pi by generating random points within a 
	range within a 2 x 2 square on a cartesian graph. Within that square
	lies a circle with an area of exactly pi (i.e radius of 1)
	If the randomly generated point falls with in the circle, it is counted.
	Pi is estimated by the following formula:

	4 * (hit_counts / trials) = approximate_pi

	hit_counts == the amount of points that fall  in the circle
	trials == the amount of points generated
	4 is the area of the square

	This fucnction will then plot each point on the graph.
	Points that fall in the circle are red and points that
	fall outside of the circle are blue."""

	win = graphics.GraphWin('Mapping Pi',650,650)
	# set x axis to length of 3
	x_axis = graphics.Line(graphics.Point(0,0),graphics.Point(0,3))
	x_axis.setArrow('last')
	# set y axis to length of 3
	y_axis = graphics.Line(graphics.Point(0,0),graphics.Point(3,0))
	y_axis.setArrow('last')	
	# Draw a circle with a radius of 1
	ref_circle = graphics.Circle(graphics.Point(1,1),1)
	# Draw the radius of the circle to the diagram
	radius = graphics.Line(graphics.Point(1,1),graphics.Point(1,2))
	# boundries of the square enclosing circle
	box1 = graphics.Line(graphics.Point(0,2),graphics.Point(2,2))
	box2 = graphics.Line(graphics.Point(2,0),graphics.Point(2,2))
	# Trials run in visulization 
	# More than 3000 trials takes too long
	trials = 3000
	i = 0
	# Hit count for everytime it falls within circle
	hcount = 0
	mcount = 0

	while i < trials: # generate random points 

		x = random.uniform(0.0,2.0)
		y = random.uniform(0.0,2.0)
		hit = graphics.Point(x,y)
		d = math.sqrt(((x-1)**2)+ ((y-1)**2))
		if d <= 1: # if point falls within circle, plot it in red
			hit.setFill('Red')
			hit.draw(win)
		else: # if point falls outside of the circle, plot it in blue
			hit.setFill('Blue')
			hit.draw(win)
		i = i + 1
	
	i = 0
	while i < 3: # create dash marks on the y axis

		y_dash = graphics.Line(graphics.Point(0,i),graphics.Point(-0.05,i))
		y_dash.setFill('Black')
		y_dash.draw(win)
		i = i + 0.5

	i = 0
	while i < 3: # create dash marks on the x axis

		x_dash = graphics.Line(graphics.Point(i,0),graphics.Point(i,-0.05))
		x_dash.setFill('Black')
		x_dash.draw(win)
		i = i + 0.5

	i = 0
	while i < 3: # Lable each dash mark on the x axis
		x_inc = graphics.Text(graphics.Point(i, -0.09), str(i))
		x_inc.setSize(9)
		x_inc.draw(win)
		i = i + 0.5


	i = 0
	while i < 3: # Lable each dash mark on the y axis
		y_inc = graphics.Text(graphics.Point(-0.12, i), str(i))
		y_inc.setSize(9)
		y_inc.draw(win)
		i = i + 0.5
	

	xl = graphics.Text(graphics.Point(0,3.1), 'y')
	yl = graphics.Text(graphics.Point(3.1,0), 'x')

	# Informational text plotted on graph 	
	graph_key = graphics.Text(graphics.Point(3,1.5), ' * The area inside the circle is π \n * The red dots approximate π \n * The Circles radius is 1 \n * Area of the square is 4')
	border_top = graphics.Line(graphics.Point(1.5,3.8),graphics.Point(3.5,3.8))
	border_bottem = graphics.Line(graphics.Point(1.5,3.2),graphics.Point(3.5,3.2))
	title = graphics.Text(graphics.Point(1.5,3), 'Pi Approximation Visualization')

	# Set the coordinates to a maximum of 4
	win.setCoords(-0.2,-0.2,4,4)
	win.setBackground('White')
	# Draw the above logic to the window
	title.draw(win)
	graph_key.draw(win)
	ref_circle.draw(win)
	radius.draw(win)
	box1.draw(win)
	box2.draw(win)
	x_axis.draw(win)
	y_axis.draw(win)
	xl.draw(win)
	yl.draw(win)
	win.getMouse()

def piStat(trials):

	""" Estimates the value of pi by generating random points within a 
	range of 2 x 2. Within that range lies a circle with an area 
	of exactly pi (i.e radius of 1). If the randomly generated point falls with 
	in the circle, it is counted. Pi is estimated by the following formula:

	4 * (hit_counts / trials) = approximate_pi

	This statistics experiment then proceeds to run the above
	600 times and appeneds each approximation of pi to a list labled
	pi_trials. 

	*Note: the user entered trials returns one value of pi. The program 
	will proceed to run and additional 600 iteration. Thus, the user
	will end up with 600 estimated values of pi. 

	**Note: Do not pass negative numbers as agruments.

	Program returns list: pi_trials"""

	k = 0
	pi_trials = []
	while k < 600: # runs the below experiment 600 times
		i = 0
		hcount = 0
		while i < trials: # Estimates pi based on user inputted trials
			# uses unifrom
			x = random.uniform(0.0,2.0) # set domain between 0 and 2
			y = random.uniform(0.0,2.0) # set range between 0 and 2
			d = math.sqrt(((x-1)**2)+ ((y-1)**2)) # find distance from center point

			if d <= 1.0: # if distance is less than or equal to 1 it is inside the circle
				value = True
			else:
				value = False
	
			if value == True: # count if it falls within circle
				hcount = hcount +1

			i = i + 1
			# calculate approximate of pi
			pi = 4 * (hcount / trials) 
		# append approximate of pi to list
		pi_trials.append(pi)
		# advance loop
		k = k +1
	# returns list of 600 estimated values of pi
	return pi_trials

def programWelcome():
	""" Welcomes user to the program"""
	print('Pi Estimator Program')
	print(format('-','-<65'))
	print('This program models a the classic "Pi dartboard approximation"\n or the Monte-Carlo method')
	print('\n')
	print('This program randomly scatters points on a circle with an area of pi')
	print('The trails or "darts" throw at the board are broken down as follows:')
	print(' *1 \n *10 \n *100 \n *1,000 \n *10,000 \n *50,000 \n *100,000')
	print('Please give the program a moment to run all 161,111 trials')
	print(format('-','-<65'))

# Introduce program purpose to user
programWelcome()

# STATISTICAL ANALYSIS 
# --------------------

# Running series of experiments 
pi_trials_1 = piStat(1)
pi_trials_10 = piStat(10)
pi_trials_100 = piStat(100)
pi_trials_1000 = piStat(1000)
pi_trials_10000 = piStat(10000)
pi_trials_50000 = piStat(50000)
pi_trials_100000 = piStat(100000)

# Mean of each experiment
mean_1 = statistics.meanBar(pi_trials_1)
mean_10 = statistics.meanBar(pi_trials_10)
mean_100 = statistics.meanBar(pi_trials_100)
mean_1000 = statistics.meanBar(pi_trials_1000)
mean_10000 = statistics.meanBar(pi_trials_10000)
mean_50000 = statistics.meanBar(pi_trials_50000)
mean_100000 = statistics.meanBar(pi_trials_100000)

# Standard deviation of each experiment
stDev_1 = statistics.stDev(pi_trials_1,mean_1)
stDev_10 = statistics.stDev(pi_trials_10,mean_10)
stDev_100 = statistics.stDev(pi_trials_100,mean_100)
stDev_1000 = statistics.stDev(pi_trials_1000,mean_1000)
stDev_10000 = statistics.stDev(pi_trials_10000,mean_10000)
stDev_50000 = statistics.stDev(pi_trials_50000,mean_50000)
stDev_100000 = statistics.stDev(pi_trials_100000,mean_100000)

# Store experiment means and standard deviations as lists
stDev = [stDev_1,stDev_10,stDev_100,stDev_1000,stDev_10000,stDev_50000,stDev_100000]
mean = [mean_1,mean_10,mean_100,mean_1000,mean_10000,mean_50000,mean_100000]
# the log base 10 of each sample size 
sample_size = [math.log10(1),math.log10(10),math.log10(100),math.log10(1000),math.log10(10000),math.log10(50000),math.log10(100000)]

# DISPLAY OF RESULTS
# ------------------

# Prints resutls of the analysis (It ain't pretty I know)
print('\n')
print('Mean at 1 Trial ',format(mean_1, '.5f'))
print('Mean at 10 Trials ',format(mean_10, '.5f'))
print('Mean at 100 Trials ',format(mean_100, '.5f'))
print('Mean at 1,000 Trials ',format(mean_1000, '.5f'))
print('Mean at 10,000 Trials ',format(mean_10000, '.5f'))
print('Mean at 50,000 Trials ',format(mean_50000, '.5f'))
print('Mean at 100,000 Trials ',format(mean_100000, '.5f'))
print('\n')
print('Standard Deviation at 1 Trial ',format(stDev_1, '.4f'))
print('Standard Deviation at 10 Trials ',format(stDev_10, '.4f'))
print('Standard Deviation at 100 Trials ',format(stDev_100, '.4f'))
print('Standard Deviation at 1,000 Trials ',format(stDev_1000, '.4f'))
print('Standard Deviation at 10,000 Trials ',format(stDev_10000, '.4f'))
print('Standard Deviation at 50,000 Trials ',format(stDev_50000, '.4f'))
print('Standard Deviation at 100,000 Trials ',format(stDev_100000, '.4f'))
print('\n')

# DATA VISUALIZATION
# ------------------

st_Dev = input('Would you like to see a graph of the standard deviations? [y/n] ')
boolflag = False
while not boolflag:
	if st_Dev == 'y':
		statistics.curveSketch(sample_size,stDev,6,3,'Standard Deviation')
		boolflag = True
	elif st_Dev == 'n':
		boolflag = True
	else:
		st_Dev = input('Would you like to see a graphic? [y/n] ')


piChart = input('Would you like to see a visual of pi? [y/n] ')

boolflag = False
while not boolflag:
	
	if piChart == 'y':
		piViz()
		boolflag = True
	elif piChart == 'n':
		print('See you later!')
		boolflag = True
	else:
		print('Cannot undersand input')
		piChart = input('Would you like to see a visual of pi? [y/n] ')



#Scrapped Code
# ------------

#boolflag = False
#while not boolflag:

#standard_dev = input('Would you like to see a chart of the standard dev? [y/n]')

#if standard_dev == 'y':
	#main()
	#boolflag = True
#elif standard_dev == 'n':
	#print('See ya later!')
	#boolflag = True
#else:
	#print('Cannot undersand input')
	#piChart = input('Would you like to see a graphic [y/n]')
	#boolflag = True


#def testPlot():
	#win = GraphWin('Pi Plot',650,650)
	#x_axis = Line(Point(0,0),Point(0,3))
	#x_axis.setArrow('last')
	#y_axis = Line(Point(0,0),Point(3,0))
	#y_axis.setArrow('last')	
	#pass 
#def hit(x,y):
	
	#if d <= 1.0:
		#return (True)
	#else:
		#return (False)
