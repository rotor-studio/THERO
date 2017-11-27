
from time import sleep
import os
import subprocess


mode =1
stop =False


if mode==0:

   print "mode0_Limpia Nat"
   os.system("sudo iptables -F")
   sleep(1)
   os.system("sudo iptables -t nat -F")
   sleep(1)
   

if mode==1 and stop==False:

    print "mode1_Iptables en modo TOR"

    os.system("sudo ./iptables_script.sh")
    sleep(1)

    stop=True
    print "no pasa"
   

if mode==2:

   print "mode2_Iptables en modo Normal"
   os.system(" ")
