# -*- coding: utf-8 -*-
from time import sleep
import sys
sys.path.append("..")
import RPi.GPIO as GPIO
from ax12 import ax12
import sys
import os
import subprocess
from pyOSC.OSC import OSCClient, OSCMessage

#GPIO SetUp
#GPIO.cleanup()


#GLOBAL VARIABLES
Apache = False
Tor= False
Run = True
servoUp = False
redPin=16
greenPin=20
bluePin=21
Position=0
red=0
green=0
blue=0
desplaza=0
desplazate=0
start=False
startMac=False
posStore=0
posCorta=False


#################

#SETUP GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.setup(12, GPIO.OUT)
GPIO.cleanup()
GPIO.setup(redPin, GPIO.OUT) 
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

##Test GPIO propouses
print("Test GPIO Led Rojo ON")
#GPIO.output(12, GPIO.HIGH)
#################


#READ MACS SETUP
counter=0 #Counter for Disconnected phones
status=0 #Status of connection
mac=" "
var=0
################


#RGB CODE LEDS 
def rgbLed(rojo,verde,azul):
      if(rojo==1):
        GPIO.output(redPin, GPIO.HIGH)
        #print("Rojo HIGH")
      else:
        GPIO.output(redPin, GPIO.LOW)

      if(verde==1):
        GPIO.output(greenPin, GPIO.HIGH)
        #print("Verde HIGH")
      else:
        GPIO.output(greenPin, GPIO.LOW)

      if(azul==1):
        GPIO.output(bluePin, GPIO.HIGH)
        #print("Azul HIGH")
      else:
        GPIO.output(bluePin, GPIO.LOW)


#Turn Off Rgb Led
rgbLed(0,0,0)
#Init Led Green
##rgbLed(1,0,0)
################
            

#SETUP SERVOS
def servoSetup():
      global servo
      servo = ax12.Ax12()
      servo.__init__()

      servo.setLedStatus(1, 1)

################

#INIT SERVO
def initServoPos(_start,Position):


      #Posición 0 Servo.

      if  _start == False:
            
          if Position > 510 and Position <520 :
                print("INIT!")
                servo.move(1,Position)
                sleep(1) 
                servo.setTorqueStatus(1,0)
                global start
                start=True

          if Position < 510 or Position > 520 :
                rgbLed(1,1,0)
                print "Go to 0 Position"
                servo.move(1,515)
                sleep(3)
                servo.setTorqueStatus(1,0)
                
            

if  servoUp== False:
    servoSetup()
    servoUp= True
    

#SETUP OSC
c = OSCClient()
c.connect( ("192.168.0.198", 40001) )
oscmsg = OSCMessage("/HOLA SOY THERO")
c.send(oscmsg)


#DETECT MAC WHITE LIST
def servoMacRun(pasa,corta,mov):
    
    if pasa == True:

        global desplazate
        
        if corta == False:
              posStore=mov
              print "POSICION GUARDADA: "+str(posStore)
              corta=True
              
        
              
        if mov > 0 or mov < 20:

            print "STOP MAC FX AT: "+str(mov)
            servo.setTorqueStatus(1,0)
            corta=False;
            pasa=False
            

        if mov == posStore:

            desplazate+=1
            print "VAMOS A LA POSICION HACI ADELANTE: "+str(posStore)
            servo.move(1,312)
            sleep(3)
            servo.setTorqueStatus(1,0)
    
         

def mode(mod):

      global Apache
      global tor
      
      if mod==0 and Apache==False:
           subprocess.call(["sudo","service","apache2","stop"])
           print ("Apagamos Apache")
           sleep(1)
           print ("Permitimos internet Wifi")

           oscmsg = OSCMessage("/APAGAMOS APACHE")
           c.send(oscmsg)
           
           Apache=True

      if mod==1 and Tor==False:
           print ("Configuramos tor")

           oscmsg = OSCMessage("/SETUP TOR")
           c.send(oscmsg)
           
           
      if mod==2 and Apache:
           subprocess.call(["sudo","service","apache2","start"])
           print ("Encendemos Apache")
           Apache=False
           sleep(1)
 
           oscmsg = OSCMessage("/BLACKOUT")
           c.send(oscmsg)
           
           print ("Desconectamos internet")
           
 

#GENERAL CODE
while Run:

       sleep(1)
       Position= servo.readPosition(1)
       sleep(1)
       print "Servo Position: "+ str(Position)

       sleep(1)
       initServoPos(start,Position) 

       if start==True:

          if Position >=0 and Position <=350:
              print("TOR MODE / COLOR AZUL")
              oscmsg = OSCMessage("/WIFI MODE / COLOR AZUL")
              c.send(oscmsg)
              rgbLed(0,1,0)
              mode(1)

          elif Position >=351 and Position <=650:

              print("WIFI MODE / COLOR ROJO")
              oscmsg = OSCMessage("/WIFI MODE / COLOR ROJO")
              c.send(oscmsg)
              rgbLed(0,0,1)
              mode(0)


              #CHECK MACS###############
              if (var < 10000):
                    
                    #OPEN FILE WITH MACS WHITE LIST
                    file = open("/home/pi/Desktop/THERO/readTxt/outputBlacklist.txt","r")

                    x = []
                    for line in file.readlines():
                         y = [line.strip()]
                         x.append(y)

                    file.close()

                    print ("Buscando...")
                    
                    result=subprocess.check_output("sudo nmap -sn 172.24.1.50-70", shell=True)
                  
                    for i in range(1,len(x)):
                            mac = x[i]
                            print (", ".join(mac))

                            if (", ".join(mac) in result) and (status==0): # At the first connection sends a welcome message Answer("Welcome back!")
                                 status=1
                               
                                 print ("hola que tal, como estamos?...")
                                 oscmsg = OSCMessage("/CLIENTE CONOCIDO CONECTADO")
                                 c.send(oscmsg)
                                 
                                 ale=Position
                                 pasa=True
                                 servoMacRun(pasa,False,ale)
                                 rgbLed(0,1,0)
                                
                  
                        
                            if (", ".join(mac) in result) and (status==1): # If phone connected keeps the counter reset
                                counter=0

                                print ("conectado")
                                oscmsg = OSCMessage("/CONECTADO")
                                c.send(oscmsg)

                       
                            if (", ".join(mac) not in result) and (status==1): # If phone is not connected increase the counter
                                counter=counter+1

                                print ("no conectado")
                                oscmsg = OSCMessage("/NO CONECTADO")
                                c.send(oscmsg)
                                
                       
                            if (status==1) and (counter>4): # Wait for the phone to stay disconnected for a while
                                status=0
                                counter=0

                                print ("esperando")

          else: 
               print("BLACKOUT / COLOR VERDE")
               oscmsg = OSCMessage("/BLACKOUT / COLOR VERDE")
               c.send(oscmsg)
               rgbLed(1,0,0)
               mode(2)
                    
  






