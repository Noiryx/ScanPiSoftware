################################################################
#           Cam test when Pin 17 goes high Test 1              #
#          Created 17/05/2015 by Quirijn Lukas Vermeire        #
#            Circuit setup: DC 5v -> Resistor -> Pin 17        #
#         Pin layout image: http://i.imgur.com/vabFhTG.png     #
################################################################

#Imports and setup
import picamera
import time
import RPi.GPIO as GPIO
#GPIO setup
GPIO.setmode(GPIO.BCM)      #Setup Pin IO
GPIO.setup(17,GPIO.IN)      #Setup pin 17 as Input
#Name setup
camera = picamera.PiCamera()#Giving the camera object a name
prev_input = 0              #Variable to check previous pininput
Number = 1                  #Variable for naming the file

while True:
  input = GPIO.input(17)    #take new reading
  if ((not prev_input) and input):           #If PIN17 went LO->HI
    camera.capture('image' + Number +'.jpg') #take a picture
    Number += 1             #increase filename # by 1
  prev_input = input        #update previous input
  time.sleep(0.12)          #debounce pause 




