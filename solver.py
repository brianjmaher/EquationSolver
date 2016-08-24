# A simple numerical equation solver.
# NOTE: it assumes that there is only one solution on the specified interval

import math, random, sys

# USER INPUT PARAMETERS. EDIT AS DESIRED

# the left and right side of the equation should be represented as lambda functions
l_expression = lambda x: math.gamma(x+1)
r_expression = lambda x: math.exp(x)

# input upper and lower bounds to find a solution on
lower = 4
upper = 6
# will find a solution to within the specified toleranmce
tolerance = 10 ** (-6)

# DO NOT EDIT BEYOND HERE
# maximum number of intervals to evaluate before assuming there is no solution
max_depth = 100

# number of values evaluated per test interval
per_interval = 10
# formula for difference between left and right sides of equation
# when difference is approx. equal to 0, a solution has been found
difference = lambda x: l_expression(x) - r_expression(x)

for _ in range(max_depth):
	if upper - lower > tolerance:
		pairs = []
		# calculate the difference value for a number of points on the interval
		for i in range(per_interval+1):
			val = lower + (upper - lower) * (i / float(per_interval))
			pairs.append( (abs(difference(val)), val) )
		# sort the difference-value pairs by absolute value of difference
		pairs.sort()
		# set the new upper and lower based on the smallest values of difference
		# found, the solution is probably on that interval
		bounds = (pairs[0][1], pairs[1][1])
		lower = min(bounds)
		upper = max(bounds)
	else:
		# Average final upper and lower bounds to approximate solution and exit
		print "Estimated solution: %f" % ((lower + upper) / 2.)
		sys.exit()
else:
	print "No solution found."
