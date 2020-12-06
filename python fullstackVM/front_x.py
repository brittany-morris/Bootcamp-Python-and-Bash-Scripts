#!/usr/bin/env python3

import sys

strings = sys.argv[1:]

list_1 = []
list_2 = []


for elem in strings:
        if elem[0] == "x":
                list_1.append(elem)
        else:
                list_2.append(elem)

sorted_list_1 = sorted(list_1)
sorted_list_2 = sorted(list_2)

print(sorted_list_1 + sorted_list_2)


