#!/usr/bin/env python3

import sys

string1 = sys.argv[1]

if  len(string1) < 2:
	print('')
else:
	print(string1[:2] + string1[-2:])






