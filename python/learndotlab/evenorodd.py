#!/usr/bin/env python3

import sys

list = sys.argv[1]

with open(list, 'r') as f:

	for num in f:
		num = num.strip()
		value = int(num)
		if value % 2 == 0:
			print(num, True)
			# True means number is Even
		else:
			print(num, False)
			# False means number is Odd


