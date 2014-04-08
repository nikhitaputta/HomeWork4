#!/usr/bin/env python

import sys
import string
import math

sumNum=0
countNum=0
countPrime=0

def prime(num):
		if num%2 == 0 and num>2:
			return False
		return all(num % i for i in range(3,int(math.sqrt(num))+1,2))

for line in sys.stdin:
	number=int(line)
	sumNum+=number
	countNum+=1
	
	
	if prime(number):
		countPrime+=1
	
	
print '%s\t%s' % ('sum',sumNum)
print '%s\t%s' % ('count',countNum)
print '%s\t%s' % ('prime',countPrime)
		
