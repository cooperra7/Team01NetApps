import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
print "LED on"
GPIO.output(25,GPIO.HIGH)
time.sleep(2)
GPIO.output(24,GPIO.HIGH)
time.sleep(2)
GPIO.output(25,GPIO.LOW)
time.sleep(2)
print "LED Off"
GPIO.output(24,GPIO.LOW)
