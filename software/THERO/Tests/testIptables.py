
from time import sleep
import os
import subprocess


mode =1
stop =False

   

if mode==1:

    print "mode1_Iptables en modo TOR"

    os.system("sudo bash ~/Desktop/THERO/iptables_script.sh")
    sleep(1)

if mode==2:

   print "mode2_Iptables en modo Normal"

   os.system("sudo bash ~/Desktop/THERO/iptables_web_script.sh")
   sleep(1)
    
