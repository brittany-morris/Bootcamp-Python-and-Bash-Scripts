#!/usr/bin/env python3

import sys

file_name = sys.argv[1]

with open(file_name, 'r') as f:
	contents = f.read()
	message = []
	split_contents = contents.split('. ')
	for sentence in split_contents:
		words = sentence.split(' ')
		message.append(words[0])
	print(' '.join(message))

