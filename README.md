# Sense HAT interface
The interface used in hackingScience workshops

* User inserts USB containing python script.
* RPi copies script over and unmounts USB.
* User removes USB and selects file from Main Menu using joystick on Sense HAT.

interfaceControl.sh runs on startup
interfaceControl calls interfaceLights.py which makes the glittery start up lights.
interfaceControl calls homeScreen.py which runs the Main Menu. 
