#!/bin/bash
python /home/pi/Go4Code/interface/interfaceLights.py
python /home/pi/Go4Code/interface/homeScreen.py &

while true;
do 
	if [ -d /media/pi/USB_PI/ ];
	then
		cp /media/pi/*/*.py /home/pi/Go4Code/mainFiles

  
		sudo umount /dev/sda1
        sudo umount /dev/sda2
        sudo umount /dev/sda3


		sudo pkill -9 python

		{
			python /home/pi/Go4Code/interface/homeScreen.py &
		} || {
		
		continue	
		}
	fi

sleep 3

done
