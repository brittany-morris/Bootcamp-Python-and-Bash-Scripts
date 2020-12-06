#!/usr/bin/env python3

import requests
import sys

url = sys.argv[1]
trueURL = url + 'product/7'
r = requests.get(trueURL)

split = r.text.split('\n')
for line in split:
	if 'RCN' in line:
		flag = line.split('>')
		flag2 = flag[1].split('<')
		print(flag2[0])
		break
