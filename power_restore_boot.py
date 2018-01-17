#!/usr/bin/env python

import os
import paramiko
import sys
import time

hostname = "hostip"  # hostip
idrac = "idracip"  # idracip
idracUN = "YourUsername"
idracPW = "YourPassword"
waittime = "WaitTimeInSeconds"

# ping host
PingHOST = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")
# ping idrac
PingIDRAC = os.system("ping -c 1 -w2 " + idrac + " > /dev/null 2>&1")

# time.sleep(waittime) #Uncomment if you'd like a dealy
# check response
if PingHOST == 0:  # host is up
    print('Host online')
    sys.exit()
else:  # if host can't be pinged
    if PingIDRAC == 0:  # idrac is up
        # ssh into idrac
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            idrac,
            port=22,
            username=idracUN,
            password=idracPW,
            look_for_keys=False
            )
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
            'racadm serveraction powerup'
            )
        print('Starting host')
    else:  # if idrac is down
        print('iDrac down!')
        sys.exit()
