from machine import Pin
from utime import sleep


pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(5)  # sleep 5 sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
