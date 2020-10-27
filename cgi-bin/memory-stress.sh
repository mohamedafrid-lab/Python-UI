#!/bin/bash
time=0
while [ $time -le 10 ]
do
  sudo free -m
  echo ""
  sleep 1s
  time=`expr $time + 1`
done
