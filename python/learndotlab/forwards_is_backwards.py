#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
	for line in f:
		if line.split() == line[::-1].split():
			print(True)
		else:
			print(False)
