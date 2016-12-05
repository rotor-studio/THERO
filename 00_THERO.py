from time import sleep
import fcntl,socket,struct
import sys
sys.path.append("..")
import RPi.GPIO as GPIO
from ax12 import ax12

#GPIO SetUp
Run= True
servoUp= False
redPin=16
greenPin=20
bluePin=21
Position=0
red=0
green=0
blue=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

##Test GPIO propouses
print("Test GPIO Led Rojo ON")
GPIO.output(12, GPIO.HIGH)


#RGB_LED
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

def getHwAddr(ifname):
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', ifname[:15]))
      return ':'.join(['%02x' % ord(char) for char in info[18:24]])

print getHwAddr('eth0')
            

#Declare & init servo var
def servoSetup():
      global servo
      servo = ax12.Ax12()
      servo.__init__()

      servo.setLedStatus(1, 1)


def servoRun():
      #Testing servo

      print("movimiento 1")
      servo.moveSpeed( 1,100, 200)
      sleep(1)

      print("movimiento 2")
      servo.moveSpeed(1,800,50)
      sleep(1)

      print("movimiento 3")
      servo.moveSpeed(1,50,100)
      sleep(1)

      servo.setTorqueStatus(1, 0)

if  servoUp== False:
    servoSetup()
    servoUp= True
    
sleep(1)
servoRun()




while Run:
      
       print(servo.readPosition(1))
       sleep(0.5)
       Position= servo.readPosition(1)
       sleep(0.5)

       if Position >=0 and Position <=350:
             print("Rojo")
             rgbLed(1,0,0)

       elif Position >=351 and Position <=650:
             print("Verde")
             rgbLed(0,1,0)
       else:
             print("Azul")
             rgbLed(0,0,1)



#GPIO.cleanup()


