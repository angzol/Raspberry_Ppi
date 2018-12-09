__author__ = 'Zotya'

import RPi.GPIO as GPIO

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode (GPIO.BCM)
# Set relay pins as output
GPIO.setup(21, GPIO.OUT)

# Turn on relay
GPIO.output(21, GPIO.LOW)
