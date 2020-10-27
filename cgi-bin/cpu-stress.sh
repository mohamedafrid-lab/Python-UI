#!/bin/bash
time=0
while [ $time -le 10 ]
do
  uptime
  sleep 1s
  time=`expr $time + 1`
done
