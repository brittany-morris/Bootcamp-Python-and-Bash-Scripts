#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
	line = f.read().splitlines()
	for num in line:
		subNumList = sum([float(x) for x in num.split()])
		print(subNumList)

# printing result
#print(str(res))
