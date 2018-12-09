__author__ = 'Zotya'
from gpiozero import MotionSensor
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode (GPIO.BCM)
# Set relay pins as output
GPIO.setup (2, GPIO.OUT)
GPIO.setup (4, GPIO.IN)

try:
	pir = MotionSensor(4)
	while True:	
    		if pir.motion_detected:
         		GPIO.output(2, GPIO.LOW)
			print "ON"
			sleep(15)
			GPIO.output(2,GPIO.HIGH)
			sleep(5)
			print "OFF"         		
except KeyboardInterrupt:
	print "Interrupted"

finally:
	GPIO.cleanup()
