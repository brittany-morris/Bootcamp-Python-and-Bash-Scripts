#!/usr/bin/env python3

import requests

url = 'http://shell.fullstackacademy.com:5592/flag'

headers = {'user-agent' : 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

r = requests.get(url, headers=headers)

print(r.text)
