###############################################################################
# Project: 	 Hill Climb Programs
# Author: 	 Stephanie Athow
# Date: 	 11 February 2015
# Professor: Dr. McGough
# Class: 	 Natural Computing
###############################################################################

# Import relevant libraries
import numpy as np
import random
import math

###############################################################################
# 						Simple Hill Climb (alg 3.1)
# initialize x 
# loop:
# 	x'= delx + x
# 	if x' is better than x, x = x'
###############################################################################
def simple_climb( xtry ):
	xbest1 = 1.01	# xbest1, 2, 3 are used to calculate xavg
	xbest2 = 1.01
	xbest3 = 1.01
	xavg = 1.00		# calculate avg
	delx = 0.01		# perterb x
	
	ybest = 0.0		# initialize ybest for comparison

	i = 0			# loop counter

	# stop at 1000 iterations or no significant improvement is made
	while (i < 1000) and (xavg > 0.1) :
		
		# evaluate x
		ytry = 2.0 ** (-2.0 * ( ( xtry - 0.1 ) / 0.9 ) ** 2.0) * math.sin( 5.0 * math.pi *xtry ) ** 6.0
	
		# if it's better, remember that and make record new 'bests'
		if ytry > ybest:
			ybest = ytry
			xbest3 = xbest2
			xbest2 = xbest1
			xbest1 = xtry
			xavg = ( xbest1 + xbest2 + xbest3 ) / 3.0
		
		xtry = xtry + delx
		i += 1
	
	return xbest1

# initialize x
xtry = random.random()

# run hill climb
xbest1 = simple_climb( xtry )

print 'Simple Hill Climb', '\n', 'X = ', xbest1

###############################################################################
# 						Iterated Hill Climb (alg 3.1)
# initialize best
# loop:
#	initialize x
#	eval(x) via simple hill climb
# 	if x' is better than best, best = x
###############################################################################

best = 0.0	# initialize best
i = 0		# loop counter

besteval = 2.0 ** ( -2.0 * ( ( best - 0.1 ) / 0.9 ) ** 2.0 ) * math.sin( 5.0 * math.pi * best ) ** 6.0

while (i < 1000) :
	# initialize x
	x = random.random()
	
	# run hill climb on x
	x = simple_climb( x )
	
	# evaluate x
	xeval = 2.0 ** ( -2.0 * ( ( x - 0.1 ) / 0.9 ) ** 2.0 ) * math.sin( 5.0 * math.pi * x ) ** 6.0
	
	# if xeval is better than best, store xeval as best
	if( xeval > besteval ):
		best = x
		besteval = xeval
	
	i += 1

print '\n', 'Iterated Hill Climb', '\n', 'X = ', best

###############################################################################
# 						Stochastic Hill Climb (alg 3.3)
# initialize x
# eval x
# loop:
#	x'= random delx + x
#	eval x'
# 	if random[0,1) < ( 1 / ( 1 + exp[ ( eval x - eval x' ) / T] ) ), 
#		x = x'
###############################################################################

x = random.random()		# initialize x
i = 0					# loop counter

# evaluate x
xeval = 2.0 ** ( -2.0 * ( ( x - 0.1 ) / 0.9 ) ** 2.0 ) * math.sin( 5.0 * math.pi * x ) ** 6.0

while (i < 1000) :
	# randomly perturb x'
	xp = x + np.random.normal( 0, 0.2 )
	
	# check x', must stay between 0 and 1
	while not ( xp <= 1 and xp >= 0 ):
		xp = x + np.random.normal( 0, 0.2 )	
	
	# evaluate x'
	xpeval = 2.0 ** ( -2.0 * ( ( xp - 0.1 ) / 0.9 ) ** 2.0 ) * math.sin( 5.0 * math.pi *xp ) ** 6.0
	
	# calculate probability of accepting x'
	p = 1.0 / ( 1.0 + math.exp( (xeval - xpeval) / 0.01 ) )
	
	if random.random() < p :
		x = xp
		xeval = xpeval
		
	i += 1
	
print '\n', 'Stochastic Hill Climb', '\n', 'X = ', x