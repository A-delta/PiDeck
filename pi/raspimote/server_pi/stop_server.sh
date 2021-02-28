#!/bin/bash
pid=`ps ax | grep wsgi_cheroot.py | awk '{split($0,a," "); print a[1]}' | head -n 1`
if [ -z "$pid" ];
then
  echo "No server from RaspiMote found"
else
  kill $pid
  echo "killed RaspiMote cheroot server"
fi