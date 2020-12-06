#!/usr/bin/env python3

import sys

file_name = sys.argv[1]

with open(file_name, 'r') as f:
	for line in f:
		if int(line) % 2 == 0:
			print(line.strip() + ' True')
		else:
			print(line.strip() + ' False')


