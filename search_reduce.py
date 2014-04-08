#!/usr/bin/env python

import sys
import string
import pickle


bloomFilter=[0]*1000000

for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	bloomFilter[int(val)]=1

print '%s' % (pickle.dumps(bloomFilter))
