from time import sleep
import RPi.GPIO as GPIO
from ax12 import ax12
import sys
import os
import subprocess

#GPIO SetUp
GPIO.cleanup()


#GLOBAL VARIABLES
Run= True
servoUp= False
redPin=16
greenPin=20
bluePin=21
Position=0
red=0
green=0
blue=0
connect=True;
#################

#SETUP GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(redPin, GPIO.OUT) 
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

##Test GPIO propouses
print("Test GPIO Led Rojo ON")
GPIO.output(12, GPIO.HIGH)
#################


#READ MACS SETUP
counter=0 #Counter for Disconnected phones
status=0 #Status of connection
mac="80:13:82:44:E3:F2"
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
rgbLed(1,0,0)
################
            

#SETUP SERVOS
def servoSetup():
      global servo
      servo = ax12.Ax12()
      servo.__init__()

      servo.setLedStatus(1, 0)

#TEST SERVOS
def servoTestRun():
      #Testing servo

      print("movimiento 1")
      servo.move(1,0)
      sleep(1) 

      print("movimiento 2")
      servo.moveSpeed(1,250,80)
      sleep(1)
      
      print("movimiento 3")
      servo.move(1,0)
      sleep(1)
      
      servo.setTorqueStatus(1,0)
   
   
if  servoUp== False:
    servoSetup()
    servoUp= True
   
sleep(1)
servoTestRun()
################

#DETECT MAC WHITE LIST
def servoMacRun(mov):

      servo.move(1,0)
      sleep(1) 
      servo.moveSpeed(1,mov,80)
      sleep(4)
      servo.move(1,0)
      sleep(1)
      servo.setTorqueStatus(1,0)

def mode(mod):
      if (mod==0):
           subprocess.call(["sudo","service","apache2","stop"])
           print "Apagamos Apache"
           
      if (mod==2):
           subprocess.call(["sudo","service","apache2","start"])
           print "Encendemos Apache"


#GENERAL CODE
while Run:
      
       print(servo.readPosition(1))
       sleep(1)
       Position= servo.readPosition(1)
       sleep(1)
       print(servo.readTemperature(1))
       sleep(1)

       if Position >=0 and Position <=350:
             print("WIFI MODE / COLOR VERDE")
             rgbLed(1,0,0)
             mode(0)
             
       elif Position >=351 and Position <=650:
             print("TOR MODE / COLOR AZUL")
             rgbLed(0,1,0)
             mode(1)
       else:
             print("BLACKOUT MODE / COLOR ROJO")
             rgbLed(0,0,1)
             mode(2)


       #CHECK MACS###############
       if (var < 10000):
              
              #OPEN FILE WITH MACS WHITE LIST
              file = open("/home/pi/Desktop/THERO/readTxt/outputMacs.txt","r")

              x = []
              for line in file.readlines():
                   y = [line.strip()]
                   x.append(y)

              file.close()

              print "Buscando..."
              
              result=subprocess.check_output("sudo nmap -sn 192.168.0.180-200", shell=True)
            
              for i in range(1,len(x)):
                      mac = x[i]
                      print ", ".join(mac)
  
                      if (", ".join(mac) in result) and (status==0): # At the first connection sends a welcome message Answer("Welcome back!")
                           status=1
                         
                           print "hola que tal, como estamos?..."
                           servoMacRun(750)
                           rgbLed(0,1,0)
            
                  
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
              
  



##GPIO.cleanup()


