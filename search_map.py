#!/usr/bin/env python

import sys
import string
import hashlib


for w in sys.stdin:
	word_line = w.strip().lower().translate(None,string.punctuation).split()

	for word in word_line:

		hash1=hashlib.md5(word+'abc')
		hash1_out=hash1.hexdigest()
		out=int(hash1_out,16)%1000000
		print '%s\t%s' % ('bloomFilter',out)

		hash2=hashlib.md5(word+'xyz')
		hash2_out=hash2.hexdigest()
		out=int(hash2_out,16)%1000000
		print '%s\t%s' % ('bloomFilter',out)

		hash3=hashlib.md5(word+'pqr')
		hash3_out=hash3.hexdigest()
		out=int(hash3_out,16)%1000000
		print '%s\t%s' % ('bloomFilter',out)
		
