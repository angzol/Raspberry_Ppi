
import codecs
import pygame
import feedparser
import subprocess
import time
import os
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode (GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
f=open('/home/pi/Python/alarm_clock/weather.txt', "rw+")

try: 
	GPIO.output(2,GPIO.HIGH)
	while True:
		sleep(60)
		dt = list(time.localtime())
		hour = dt[3]
		minute = dt[4]
			if hour == 5 and minute == 45:
			GPIO.output(2,GPIO.LOW)
       	        	os.system('echo "Good morning Zita and Zoli, it is time to get up"| festival --tts')
			os.system('echo "Lets start the new day with a beautiful music before the weather details" |festival --tts')

			pygame.mixer.init()
			pygame.mixer.music.load("/home/pi/Python/alarm_clock/Drive.wav")
			pygame.mixer.music.play(loops=0, start=0.0)

			d=feedparser.parse('http://open.live.bbc.co.uk/weather/feeds/en/3054643/3dayforecast.rss')
			text=d['entries'][0]['description']
			f.write(text.encode('utf8'))
			f.close
			sleep(258)
			os.system('echo "Todays weather details: " |festival --tts')
			subprocess.call("festival --tts /home/pi/Python/alarm_clock/weather.txt", shell=True)

			sleep(10)
			GPIO.output(2,GPIO.HIGH)
			os.system('echo "Thank you for listening. Have a nice and wonderful day!" |festival --tts')

except KeyboardInterrupt:
	print "Interrupted"

finally:
	GPIO.cleanup()
