#!/usr/bin/env python3

import sys
import ast

# Reads in a file and returns a dictionary
def parse_file(filename):
    # Dictionary for holding the parts of the haiku
    haiku_parts = {}

    # Read the contents of the file into the dictionary
    with open(filename, 'r') as f:
        # Read the entire text of the file
        words = f.read()
        # Change the text from the file into a dictionary
        # https://docs.python.org/3/library/ast.html#ast.literal_eval
        haiku_parts = ast.literal_eval(words)

    return haiku_parts


# Prints the values in a dictionary, after sorting the keys
def print_haiku(haiku):
    # Words on the current line
    line = []

    # Iterates through the dictionary after sorting the keys as integers
    for key in sorted(haiku, key=int):
        word = haiku[key]

        if word == '\n':
            # If the current word is a newline, print the words in the line
            # separated by a space, and then clear all words from the line.
            print(' '.join(line))
            line = []
        else:
            line.append(word)


def main():
    # Get the filename provided on the command line
    filename = sys.argv[1]

    haiku = parse_file(filename)
    print_haiku(haiku)


if __name__ == '__main__':
    main()
