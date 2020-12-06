#!/usr/bin/env python3

import requests

url = 'http://get-that-request.runcode.ninja/'

r = requests.get(url)


flag = False

while flag == False:
	if 'RCN{' in r.text:
		start_index = r.text.find('RCN{')
		end_index = r.text.find('}', start_index)
		print(r.text[start_index:end_index +1])
		flag = True
	else:
		print('Flag not found')
		break
	break
