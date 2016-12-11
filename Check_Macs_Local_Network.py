#Code from: http://rpihome.blogspot.com.es/2015/02/checking-devices-connected-to-lan.html

import subprocess

counter=0 #Counter for Disconnected phones
status=0 #Status of connection
mac="00:00:00:00:00:00"

var=0

while (var < 10000):

        print "Buscando..."
        
        result=subprocess.check_output("sudo nmap -sn 192.168.0.1-200", shell=True)
        
        if (mac in result) and (status==0): # At the first connection sends a welcome message Answer("Welcome back!")
            status=1
            print "hola que tal, como estamos?..."
            
            
        if (mac in result) and (status==1): # If phone connected keeps the counter reset
           counter=0

           print "conectado"
           
        if (mac not in result) and (status==1): # If phone is not connected increase the counter
           counter=counter+1

           print "no conectado"
           
        if (status==1) and (counter>4): # Wait for the phone to stay disconnected for a while
           status=0
           counter=0

           print "esperando"

        print result
        


