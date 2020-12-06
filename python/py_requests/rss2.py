#!/usr/bin/env python3

import requests

url = 'http://shell.fullstackacademy.com:57859/'

payload = {'handle' : 'cyrose', 'movie' : 'mrrobot', 'command' : 'clear'}

response = requests.post(url, json = payload)

print(response.text)
