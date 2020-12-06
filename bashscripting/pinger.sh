#!/bin/bash

#perform the command

#touch ping_sweep.txt

RESULTS=ping_sweep.txt

for NUM in {1..24} 
do
HOST="10.0.0.$NUM"
ping -c 1 $HOST >> $RESULTS
done
