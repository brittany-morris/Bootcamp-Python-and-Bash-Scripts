#!/usr/bin/env python3

import requests

url = 'http://get-that-request.runcode.ninja/'

r = requests.get(url)

start_index = r.text.find('RCN{')
end_index = r.text.find('}', start_index)
print(r.text[start_index:end_index +1])
