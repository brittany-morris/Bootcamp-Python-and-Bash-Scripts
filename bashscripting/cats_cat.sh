#!/bin/bash

# get the input filename ($1)
#read that file (while loop)
#in the loop, cat the file

FILENAME=$1

touch results.txt
while read LINE
do
cat $LINE >> results.txt
done < $FILENAME
