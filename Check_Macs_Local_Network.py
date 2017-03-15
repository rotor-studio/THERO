#Code from: http://rpihome.blogspot.com.es/2015/02/checking-devices-connected-to-lan.html

#Now READ MAC


import subprocess

counter=0 #Counter for Disconnected phones
status=0 #Status of connection
mac= " "


var=0

while (var < 10000):

        file = open("/home/pi/Desktop/output.txt","r")

        x = []
        for line in file.readlines():
             y = [line.strip()]
             x.append(y)

        file.close()

        print "Buscando..."

        result=subprocess.check_output("sudo nmap -sn 192.168.0.190-200", shell=True)
        
        for i in range(1,len(x)):
                mac = x[i]
                print ", ".join(mac)          


                if (", ".join(mac) in result) and (status==0): # At the first connection sends a welcome message Answer("Welcome back!")
                    status=1
                    print "hola que tal, como estamos?..."
                    
                    
                if (", ".join(mac) in result) and (status==1): # If phone connected keeps the counter reset
                   counter=0

                   print "conectado"
                   
                if (", ".join(mac) not in result) and (status==1): # If phone is not connected increase the counter
                   counter=counter+1

                   print "no conectado"
                   
                if (status==1) and (counter>4): # Wait for the phone to stay disconnected for a while
                   status=0
                   counter=0

                   print "esperando"

                print result
        


