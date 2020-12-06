#!/usr/bin/env python3

import sys

file_name = sys.argv[1]

with open(file_name, 'r') as f:
	counter_dictionary = {}
	for line in f:
		name = line.strip()
		if name not in counter_dictionary:
			counter_dictionary[name] = 1
		else:
			counter_dictionary[name] +=1
	print(counter_dictionary)

for key, value in sorted(counter_dictionary.items()):
	print(f'{key} - {value}')
