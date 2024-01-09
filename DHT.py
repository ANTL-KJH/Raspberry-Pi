import time
import adafruit_dht
from board import *

# GPIO4
SENSOR_PIN = 37

dht11 = adafruit_dht.DHT11(SENSOR_PIN, use_pulseio=False)

while True:
    temperature = dht11.temperature
    humidity = dht11.humidity
    print(f"Humidity= {humidity:.2f}")
    print(f"Temperature= {temperature:.2f}°C")
    time.sleep()
