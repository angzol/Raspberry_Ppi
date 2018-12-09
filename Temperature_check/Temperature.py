from gpiozero import CPUTemperature
import Adafruit_DHT as dht
from time import sleep, strftime, time

h,t=dht.read_retry(dht.DHT22,2)
cpu=CPUTemperature()

print 'Kulso homerseklet: ', '{0:0.1f}*C'.format(t)
print 'Kulso paratartalom: ', '{0:0.1f}%'.format(h)
print 'Rendszer homerseklet: ', '{0:0.2f}*C'.format(cpu.temperature)
