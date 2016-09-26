#!/bin/bash

#goto current shell file dir
cd `dirname $0`

if [ -f "nohup.out" ]; then
  rm -f nohup.out
fi

if [ -f "pid" ]; then
  kill $(cat pid)
fi

nohup python bookDeploy.py prod &
echo "$!" > pid