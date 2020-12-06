#!/bin/bash

for IP in {1..254}
do
ping -c 1 192.168.1.$IP >> ping_sweep.txt &
#ping -c 1 192.168.1.$IP | grep "bytes from" >> ping_sweep.txt &
done
