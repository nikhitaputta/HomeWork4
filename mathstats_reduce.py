#!/usr/bin/env python

import sys
import string

sumN=0
cntNum=0
cntPrime=0

for w in sys.stdin:
	(key,val) = w.strip().split('\t',1)
	if key=='sum':
		sumN+=int(val)	
	elif key=='count':
		cntNum+=int(val)
	else:
		cntPrime+=int(val)
print '%s\t%s' % ('sum of Numbers',sumN)
print '%s\t%s' % ('count of Numbers',cntNum)
print '%s\t%s' % ('count of prime numbers',cntPrime)
