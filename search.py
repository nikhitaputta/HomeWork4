#!/usr/bin/env python

import sys
import string
import pickle
import hashlib


file_name=sys.argv[1]
f=open(file_name,'r')
s=f.read()
f.close()

bloomFilter=pickle.loads(s)

print "enter the search word"
while True:
	word=raw_input().lower()
	
	if(word.lower() == "exit"):
		break
	else:
		hash1=hashlib.md5(word+'abc')
		hash1_out=hash1.hexdigest()
		word1=int(hash1_out,16)%1000000
		
		hash2=hashlib.md5(word+'xyz')
		hash2_out=hash2.hexdigest()
		word2=int(hash2_out,16)%1000000
		
		hash3=hashlib.md5(word+'pqr')
		hash3_out=hash3.hexdigest()
		word3=int(hash3_out,16)%1000000

		if bloomFilter[word1] == 1 and bloomFilter[word2] == 1 and bloomFilter[word3] == 1:
			print "Found!! :-)"
		else:
			print "Not Found :-("

