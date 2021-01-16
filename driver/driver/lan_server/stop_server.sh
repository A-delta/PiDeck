#!/bin/bash
Port=9876
pid=`ps ax | grep gunicorn | grep $Port | awk '{split($0,a," "); print a[1]}' | head -n 1`
if [ -z "$pid" ]; then
  echo "no gunicorn deamon on port $Port"
else
  kill $pid
  echo "killed gunicorn deamon on port $Port"
fi