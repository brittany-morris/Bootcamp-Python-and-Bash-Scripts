#!/usr/bin/env python3

import requests

url = 'http://scrape-me.runcode.ninja/'

r = requests.get(url)

print(r.text)
