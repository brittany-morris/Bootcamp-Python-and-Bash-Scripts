#!/usr/bin/env python3

import sys

string = sys.argv[1]

#if letter is equal letter at start of string replace with *

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '*')
  str1 = char + str1[1:]

  return str1

print(change_char(string))
