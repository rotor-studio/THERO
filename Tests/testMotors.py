from time import sleep
import RPi.GPIO as GPIO
from ax12 import ax12

#GLOBAL VARIABLES
Apache = False;
Run = True
servoUp = False
redPin=16
greenPin=20
bluePin=21
Position=0
red=0
green=0
blue=0
ipRangeInit=1;
ipRangeEnd=20;

GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setup(12, GPIO.OUT)
GPIO.setup(redPin, GPIO.OUT) 
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

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
      print "hola"
      servo.setLedStatus(1, 0)


################

#TEST SERVOS
def servoTestRun():
      #Testing servo

      print("movimiento 1")
      servo.move(1,0)
      sleep(1) 

      print("movimiento 2")
      servo.moveSpeed(1,200,80)
      sleep(1)
      
      print("movimiento 3")
      servo.move(0,0)
      sleep(1)
      
      servo.setTorqueStatus(1,0)


if  servoUp== False:
    servoSetup()
    servoUp= True
   
sleep(1)
servoTestRun()

sleep(1)
print (servo.readPosition(1))
   

################

#GPIO.cleanup()
