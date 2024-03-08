import dht
from machine import Pin
from time import sleep


sensor = dht.DHT11(Pin(0))
while True:
    try:
        sleep(2)
        sensor.measure()
        print(sensor.measure())
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9 / 5) + 32.22
        print("Temperature: %3.1f C" % temp)
        print("Temperature: %3.1f F" % temp_f)
        print("Humidity: %3.1f %%" % hum)
    except OSError as e:
        print(e)
        print("Failed to read sensor.")