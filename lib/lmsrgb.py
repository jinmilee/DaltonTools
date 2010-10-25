#
#  lmsrgb.py
#  
#
#  Created by Jinmi Lee on 5/7/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#



def rgb2lms (r, g, b):
	l = 17.8824*r + 43.5161*g + 4.11935*b
	m = 3.45565*r + 27.1554*g + 3.86714*b
	s = 0.0299566*r + 0.184309*g + 1.46709*b
	return l, m, s
	
def lms2rgb (l, m, s):
	r = 0.080944*r_ - 0.130504*g_ + 0.116721*b_
	g = -0.0102485*r_ + 0.0540194*g_ - 0.113615*b_
	b = -0.000365294*r_ -0.00412163*g_ + 0.693513*b_
	return r, g, b
