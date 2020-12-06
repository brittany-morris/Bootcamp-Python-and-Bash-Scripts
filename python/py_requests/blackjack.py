#!/usr/bin/env python3

import requests
import sys

url = sys.argv[1]
trueURL = url + '/bj.php'
data = {'do_what': 'deal'}
data2 = {'do_what': 'stay'}

s = requests.Session()
s1 = s.get(url)

flag = False

while flag == False:
	r1 = s.post(trueURL, params=data)
	if 'RCN{' in r1.text:
		flag = True
		flag_startIndex = r1.text.find('RCN{')
		flag_endIndex = r1.text.find('}', flag_startIndex)
		print(r1.text[flag_startIndex:flag_endIndex+1])
	else:
		r2 = s.post(trueURL, params = data2)
