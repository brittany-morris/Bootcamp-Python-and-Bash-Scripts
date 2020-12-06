#!/usr/bin/env python3

import requests

url = 'http://shell.fullstackacademy.com:22631/'

r = requests.get(url)

print(r.cookies['flag'])


