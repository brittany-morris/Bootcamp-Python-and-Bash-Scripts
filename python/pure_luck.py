#!/usr/bin/env python3

import sys
import socket

HOST = sys.argv[1]
PORT = int(sys.argv[2])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	conn_info = (HOST, PORT)
	sock.connect(conn_info)

	prompt = sock.recv(1024)
	text = prompt.decode()
#	print(text)

	guess = 0
	while text.startswith('Pick a number'):
		my_guess = str(guess) + '\n'
		encoded_guess = my_guess.encode()
#		print('We are guessing ', my_guess)
		sock.send(encoded_guess)

		response = sock.recv(1024)
		text = response.decode()
		guess += 1
	
	print(text)

