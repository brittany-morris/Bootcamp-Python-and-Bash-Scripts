#!/usr/bin/env python3

import requests

url = 'http://shell.fullstackacademy.com:24673/'

r = requests.delete(url)

print(r.text)
