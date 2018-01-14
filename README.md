# idrac-startup
Start iDrac enabled machine after UPS shutdown

This script is has been designed to be used on an SBC such as a Raspberry Pi. 

If you have an server with an iDrac that has been gracefully shut down when on UPS power, this script will start it back up again once mains power has been restored to the UPS.

Install:

Simply copy this into a file on your Pi named whateveryoulike.py

Make it run at startup:

For simplicity, I have made it a cronjob.
@reboot /usr/bin/python  /path/to/your/script.py

Hardware config:

Make sure the pi is not attached to the UPS, that way it will power on and off with power outages which is vital.
Use ethernet connections where possible.


Dependencies:

You need to install paramiko for this to work http://www.paramiko.org/installing.html 
