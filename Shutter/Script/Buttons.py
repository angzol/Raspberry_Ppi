import os
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import time
from time import sleep

GPIO.setmode (GPIO.BCM)
lcd=LCD.Adafruit_CharLCDPlate()

try:
	while True:
		if lcd.is_pressed(LCD.SELECT):
			lcd.clear()			
			lcd.message ("KIKAPCSOLAS..\n"+ "3 MP")
			sleep(1)
			lcd.clear()
			lcd.message("KIKAPCSOLAS..\n" + "2 MP")
			sleep(1)
			lcd.clear()			
			lcd.message("KIKAPCSOLAS..\n" + "1 MP")
			sleep(1)
			lcd.clear()
			lcd.set_backlight(0)

			GPIO.cleanup()

			os.system('sudo shutdown -h now')
		elif lcd.is_pressed(LCD.LEFT):
			lcd.clear()
			lcd.message ("UJ REDONY\n" + " FELVETELE")
			sleep(3)
			lcd.clear()
			lcd.message("ADATOK MENTESE")

			a=time.strftime("%Y-%m-%d")
			os.system('sudo mkdir -p /home/pi/Shutter/backup/'+a+'/')

			os.system('sudo cp /home/pi/Shutter/Up.dat /home/pi/Shutter/backup/'+a+'/Up.dat')
			os.system('sudo cp /home/pi/Shutter/Down.dat /home/pi/Shutter/backup/'+a+'/Down.dat')

			print("Kesz")
		
			f=open('/home/pi/Shutter/Down.dat',"rw+")
			f.write(str(0))
			f.close
			g=open('/home/pi/Shutter/Up.dat',"rw+")
			g.write(str(0))
			g.close

			sleep(2)

			lcd.clear()
			lcd.message("MENTES KESZ")

			sleep(3)
			lcd.message("INDITSA UJRA\n" + "A GEPET!")
except KeyboardInterrupt:
	print "interrupted"
	lcd.clear()
	lcd.set_backlight(0)
