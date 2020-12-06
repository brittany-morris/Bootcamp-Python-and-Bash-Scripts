#!/usr/bin/env python3

import sys

filename = sys.argv[1]

counts = {}
counts['good'] = 0
counts['bad'] = 0

with open(filename, 'r') as f:
	for line in f:
		line = line.strip()
		words = line.split()
		status = words[-1]
		counts[status] += 1
print(f'Naughty list has {counts["bad"]} people!')
print(f'Nice list has {counts["good"]} people!')
