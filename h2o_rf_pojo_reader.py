#================================================
# H2O Pojo RF Model interpreter
# The code is annotated with commented tree
# that shows the depth and location of
# the current random if condition
#================================================
#! /usr/bin/env python
import os, sys

if len(sys.argv) < 3 or len(sys.argv) > 3:
	print "Usage:\n",sys.argv[0],"filename.pojo","output.txt"
	sys.exit()

def parse_rf_pojo(in_pojo,out_pojo):
	sys.stdout = outfile
	l_count = 0
	for line in in_pojo:
		for letter in line:
			if letter == "(":
				l_count +=1
			if letter == ")":
				l_count -=1
		print "/*","I"*l_count,"\t",l_count,"*/",line,
	return

f = open(sys.argv[1])
outfile = open(sys.argv[2],"w")
try:
	parse_rf_pojo(f,outfile)
finally:
	f.close()
	outfile.close()
