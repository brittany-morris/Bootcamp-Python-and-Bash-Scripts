 #!/usr/bin/env python3

import sys

file_name = sys.argv[1]

with open(file_name, 'r') as f:
	for line in f:
		if line.split() == line[::-1].split():
			print(True)
		else:
			print(False)


