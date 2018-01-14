import os
import paramiko
import sys
hostname = "host-ip" #hostip
idrac = "idrac-ip" #idracip
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
    ssh.connect("192.168.1.219", port=22, username="root", password="calvin", look_for_keys=False)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('racadm serveraction powerup')
    print('Starting SuperPi') 
  else: #if idrac is down
     sys.exit() 
     print('iDrac down!')
