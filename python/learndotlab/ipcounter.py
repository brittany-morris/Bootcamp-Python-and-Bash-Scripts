#!/usr/bin/env python3

import sys

filename = sys.argv[1]
counts = {}

with open(filename, 'r') as f:
	for line in f:
		fields = line.split()
		ip_addr = fields[0]
		if ip_addr in counts:
			counts[ip_addr] += 1
		else:
			counts[ip_addr] = 1
for ip_addr in sorted(counts.keys()):
	print(f'{ip_addr} - {counts[ip_addr]}')

