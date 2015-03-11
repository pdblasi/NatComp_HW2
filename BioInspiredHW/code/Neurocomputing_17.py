###############################################################################
# Project: 	 Pg 199 #17 - ANN
# Author: 	 Stephanie Athow
# Date: 	 9 March 2015
# Professor: Dr. McGough
# Class: 	 Natural Computing
# Problem Statement:
#	Apply the MLP network trained with the back-propagation learning algorithm
#	to solve the character recognition task of section 4.4.2.
#
#	Determine a suitable network architecture and then test the resultant
#	network sensitivity to noise in the test data. Test different noise levels,
#	from 5% to 50%.
###############################################################################

# Algorithm from book:
'''
def backprop( max_it, min_err, alpha, X, D ):
	for m from 1 to M:
		init W^m 	# small random values
		init b^m	# small random values
		
	t = 1
	while t < max_it and MSE > min_err:
		vet_permute <- randperm( N )		# permutations of N
		
		for j from 1 to N:					# for all input patters
			# select index i of pattern Xi to be presented
			i <- vet_permute( j )			# present patterns randomly
			
			# forward propagation of the functional signal
			# eq 4.37: y^0 = x
			
			for m from 0 to M-1:
				# eq 4.36: y(m+1) = f(M+1) * ( W(m+1)*y(m) + b(m+1) )
				
			# backprop of sensitivitites
			# eq 4.65: del(M) = -2*Fdot(m) * u(m) * ( d - y)
			
			for m from M-1 to 1:
				# eq 4.60: Fdot(m) * u(m) * W(m+1)^T * del(m+1)
			
			# update weights and biases
			for m from 1 to M:
				# eq 4.52: W(m)[t+1] = W(m)[t] - alpha*del(m)*(y(m-1))^T
				# eq 4.53: b(m)[t+1] = b(m)[t] - alpha*del(m)
				
			# calculate the error for pattern i
			# E(i) <- e(i)^T * e(i) = ( d(i)-y(i) )^T * ( d(i)- y(i) )
		
		MSE <- 1 / N.sum( Ei )		# Mean Square Error
		t += 1

	# end
'''

# import necessary libraries
import numpy as np
import math

# will want to use np.matlib and np.matrix

# initial values
max_it = 1000
min_err = 1
alpha = 1

# load training images (10 of them, 0-9)