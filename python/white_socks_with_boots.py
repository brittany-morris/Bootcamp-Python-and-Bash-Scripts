#!/usr/bin/env python3

import sys

import socket

HOST = sys.argv[1]
PORT= int(sys.argv[2])   #We need to use int to change it to a number
text = ' '.join(sys.argv[3:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	text = text + '\n'
	data = text.encode()
	s.send(data)
	
	response_data = s.recv(1024)
	response_text = response_data.decode()
	response_text = response_text.strip()
	print(response_text)
