import os
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
from time import sleep

lcd=LCD.Adafruit_CharLCDPlate()
GPIO.setmode (GPIO.BCM)

GPIO.setup(19,GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

#le és fel adatok dat fájljai
f=open('/home/pi/Shutter/Down.dat',"rw+") 
g=open('/home/pi/Shutter/Up.dat', "rw")  

#le és fel adatok olvasása változóba
le = int(f.readline()) 
fel = int(g.readline()) 

print(le)
print(fel)

try:
        while True:
# a Relék alaphelyzetbe állása
                GPIO.output(19,GPIO.HIGH)
		sleep(1) #biztonsági tényező
                GPIO.output(26,GPIO.LOW)

                le=le+1
		# dat fájlba írás
		f=open('/home/pi/Shutter/Down.dat',"rw+")
                f.write(str(le) + os.linesep)
		full=le+fel
		#le + fel darabszám kiírása az lcd kijelzőre
                print(full)
                full_str=str(full)
                lcd.message('FEL / LE MOZGAS: \n')
		lcd.message(full_str)
                sleep(3600)
		lcd.clear()

                GPIO.output(26,GPIO.HIGH)
		sleep(1) #bizt. tényező
                GPIO.output(19, GPIO.LOW)

                fel=fel+1
                g=open('/home/pi/Shutter/Up.dat',"rw+")
                g.write(str(fel) + os.linesep)
		full=le+fel
		lcd.clear()
                print(full)
                full_str=str(full)
                lcd.message('FEL / LE MOZGAS: \n')
                lcd.message(full_str)
                sleep(3600)
		lcd.clear()

except KeyboardInterrupt:
        print "Interrupted"
        f.close()
        g.close()
finally:
        GPIO.cleanup()
        lcd.clear()
        lcd.set_backlight(0)

