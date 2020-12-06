#!/usr/bin/env python3

import sys

def parse_file():
	f = open('quack2.txt', 'r')
	text = f.read()
	return text

def count_quacks(s):
	total = 0
	lines = s.split('\n')
	for line in lines:
		words = line.split(' ')
		for word in words:
			if word == 'quack'
				total += 1
	print(count)

def main():
#	phrase = sys.argv[1]
#	print(phrase)
	data = parse_file()
	count_quacks(data)

main()
