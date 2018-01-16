#!/usr/bin/env python

import os
import paramiko
import sys
import time

hostname = "host-ip" #hostip
idrac = "idrac-ip" #idracip
idracUN = "youridracUN"
idracPW = "youridracPW"
waittime = "WaitTimeInSeconds"

#time.sleep(waittime) #Uncomment if you'd like a dealy to ensure power is stable
response = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1") #ping host
#check response
if response == 0: #host is up
  print("Host online")
  sys.exit()
else: #if host can't be pinged
  response = os.system("ping -c 1 -w2 " + idrac + " > /dev/null 2>&1") #ping idrac
  if response == 0: #idrac is up
    ssh = paramiko.SSHClient() #ssh into idrac
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("idracipaddr", port=22, username="idracUN", password="idracPW", look_for_keys=False)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('racadm serveraction powerup')
    print('Starting host') 
  else: #if idrac is down
     sys.exit() 
     print('iDrac down!')
