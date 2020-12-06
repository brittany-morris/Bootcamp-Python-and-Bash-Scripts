#!/usr/bin/env python3

import sys

strings = sys.argv[1:]

result = 0

for elem in strings:
	if len(elem) >= 2 and elem[0] == elem[-1]:
		result += 1

print(result)
