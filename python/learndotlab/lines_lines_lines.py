#!/usr/bin/env python3

import sys

file = sys.argv[1]
output = ''

with open(file, 'r') as f:
	for line in f:
		line = line.strip()
		output += line
		if len(line) > 0:
			output += ' '
print(output)
