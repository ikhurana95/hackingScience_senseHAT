#!/usr/bin/env bash
pkill -9 python

python /home/pi/Go4Code/interface/sayBye.py

python /home/pi/Go4Code/interface/homeScreen.py &
