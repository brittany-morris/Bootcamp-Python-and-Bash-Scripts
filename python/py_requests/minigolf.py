#!/usr/bin/env python3

import requests

url = 'http://shell.fullstackacademy.com:3776/'

r = requests.put(url)

print(r.text)
