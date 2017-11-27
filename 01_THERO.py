# -*- coding: utf-8 -*-

#Includes
from time import sleep
import sys
sys.path.append("..")
import RPi.GPIO as GPIO
from ax12 import ax12
import sys
import os
import subprocess

#Global variables
#Led----------------------
redPin=16
greenPin=20
bluePin=21
red=0
green=0
blue=0
#Servo--------------------
servoUp = False
Position=0
#Booleans-----------------
start=False
Apache = False
Run = True
servoUp = False


#Reading Mac's------------
counter=0 #Counter for Disconnected phones
status=0 #Status of connection
mac=" "
var=0

#SETUP INIT///////////////////////////////////////////////

#Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT) 
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

#Setup Servos
def servoSetup():
      global servo
      servo = ax12.Ax12()
      servo.__init__()

      servo.setLedStatus(1, 1)

#INIT SERVO
def initServoPos(_start,Position):


      #Posición 0 Servo.

      if  _start == False:
            
          if Position >=485 and Position <510 :
                print "INIT!"
                servo.move(1,Position)
                sleep(1) 
                servo.setTorqueStatus(1,0)
                global start
                start=True

          else:
                rgbLed(1,1,0)
                print "Go to 0 Position"
                #servo.move(1,0)
                sleep(1)
                servo.move(1,510)


if  servoUp== False:
    servoSetup()
    servoUp= True

#SETUP END///////////////////////////////////////////////

#RGB Leds
def rgbLed(rojo,verde,azul):

      if(rojo==1):
        GPIO.output(redPin, GPIO.HIGH)
      else:
        GPIO.output(redPin, GPIO.LOW)

      if(verde==1):
        GPIO.output(greenPin, GPIO.HIGH)
      else:
        GPIO.output(greenPin, GPIO.LOW)

      if(azul==1):
        GPIO.output(bluePin, GPIO.HIGH)
      else:
        GPIO.output(bluePin, GPIO.LOW)

#Leds a 0----------------
rgbLed(0,0,0)


#Gestiona la conexión internet/////////////////////////////
def mode(mod):

      global Apache
      
      if mod==0 and Apache==False:
           subprocess.call(["sudo","service","apache2","stop"])
           print ("Apagamos Apache")
           sleep(1)
           print ("Permitimos internet Wifi")
           Apache=True
           
           
      if mod==2 and Apache:
           subprocess.call(["sudo","service","apache2","start"])
           print ("Encendemos Apache")
           sleep(1)
           print ("Desconectamos internet")
           Apache=False





