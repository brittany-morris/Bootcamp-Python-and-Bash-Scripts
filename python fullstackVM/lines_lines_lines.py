#!/usr/bin/env python3

import sys

def main():
	input_file = sys.argv[1]
	output = ''

	with open(input_file, 'r') as f:
		for line in f:
			text = line.strip()
			if len(text) > 0:
				output += text + ' '
	print(output)

if __name__ == '__main__':
	main()
