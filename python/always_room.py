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


	while text.startswith('add 1 to me:'):
		promptnumber = int(text.split('add 1 to me:')[-1])
		promptnumber += 1
		newnum = str(promptnumber) + '\n'
		encodednewnum = newnum.encode()
		sock.send(encodednewnum)


		response = sock.recv(1024)
		text = response.decode()

	answer = str(text.split('for your trouble: ')[-1])
	print(answer)




