#!/usr/bin/env python3

import requests
import sys

# take url from command line (I need sys)
url = sys.argv[1]

# make get request to the root of the resource (I need python requests)
# make sessions to keep cookies (requests handles most of this for us)
with requests.Session() as s:
	response = s.get(url)
# push button (make post request To /bj.php AND with do_what=deal in the body)
	post_url = url + '/bj.php'
	payload = {'do_what': 'deal'}
	while not 'RCN{' in response.text:
		response = s.post(post_url, data=payload)

# read the response - look for flag
	start_index = response.text.find('RCN{')
	end_index = response.text.find('}', start_index)
	print(response.text[start_index:end_index + 1])
#	if flag : print flag
#	if not flag: keep hitting push (sounds like a while loop)


