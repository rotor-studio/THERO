#!/usr/bin/python
#Enable or disable apache2 & write and erase iptables routes (blocking sites)
#THERO / Román Torre

 
import sys
import os
import subprocess

i = 1     

if(i==0):
  subprocess.call(["sudo","service","apache2","stop"])
  print "Apagamos Apache"

if(i==1):
  subprocess.call(["sudo","service","apache2","start"])
  print "Encendemos Apache"

if(i==2):
  subprocess.call(["sudo","iptables","-A","OUTPUT","-p","tcp","-m","tcp","-d","www.meneame.net","-j","DROP"])
  print "Añadimos bloqueo de conexiones"

if(i==3):
  subprocess.call(["sudo","iptables","-D","OUTPUT","1"])
  print "Quitamos bloqueo de conexiones"


