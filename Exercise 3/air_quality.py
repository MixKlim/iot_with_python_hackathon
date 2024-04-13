import dht

# import datetime
from time import sleep
from machine import Pin

sensor = dht.DHT22(Pin(22))

while True:
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        # The following command converts the temperature to Fahrenheit degrees.
        # temp_f = temp * (9/5) + 32.0
        # print(
        #     "Measurement time: " % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # )
        print("Temperature: %3.1f C" % temp)
        # print("Temperature: %3.1f F" % temp_f)
        print("Humidity: %3.1f %%" % hum)
    except OSError as e:
        continue
