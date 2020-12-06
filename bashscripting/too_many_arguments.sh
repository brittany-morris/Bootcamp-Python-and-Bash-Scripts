#!/bin/bash

# if < 6 arguments are present, print need more arguments
# else, print FS{1s_Th1s_H0w_Th3y_D1d_1t?}

if [ "$#" -lt 6 ]; then
	echo "You need more arguments"
fi
if [ "$#" -ge 6 ]; then
	echo "FS{1s_Th1s_H0w_Th3y_D1d_1t?}"
fi
