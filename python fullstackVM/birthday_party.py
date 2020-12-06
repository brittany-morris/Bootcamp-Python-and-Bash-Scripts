#!usr/bin/env python3

#use sys to get argument from command line (file to open)
import sys

file_name =  sys.argv[1]

# open that file
with open(file_name, 'r') as f:

# initialize a counter dictionary
	counter_dictionary = {}

# loop through the lines
	for line in f:
		name = line.strip()
# if name is not in dictionary...:
		if name not in counter_dictionary:
# dictionary set the value of that name to be 1
			counter_dictionary[name] = 1
# else add 1 to the value at that name
		else:
			counter_dictionary[name] +=1
# print the counter dictionary
	print(counter_dictionary)


for key, value in counter_dictionary.items():
	print(f'{key} - {value}')
