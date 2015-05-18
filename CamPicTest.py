################################################################
#           Cam test when Pin 17 goes high Test 1              #
#         Developed 18/05/2015 by Quirijn Lukas Vermeire       #
#       Co-developed by: Anhad Sandhu, Abdullah El Agha        #
#         Pin layout image: http://i.imgur.com/vabFhTG.png     #
################################################################

#Imports and setup
import picamera
import time
import RPi.GPIO as GPIO
#GPIO setup
GPIO.setmode(GPIO.BCM)      #Setup Pin IO
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Name setup
camera = picamera.PiCamera()#Giving the camera object a name
prev_input = 0              #Variable to check previous pininput
Number = 1                  #Variable for naming the fil
GPIO.add_event_detect(27, GPIO.RISING) #Detect if ping goes to high
#take a picture function
def my_callback(Unused):
  global Number
  camera.capture('image' + str(Number) +'.jpg') #take a picture
  print('Took picture #' + str(Number))		#print to console
  Number += 1             #increase filename # by 1
#check if button is pushed function
GPIO.add_event_callback(27, my_callback) #calls my_callback