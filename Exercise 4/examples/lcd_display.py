# Source: Electrocredible.com, Language: MicroPython
import utime
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 0x3F
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
utime.sleep(1)
lcd.clear()
lcd.move_to(0, 0)
lcd.putstr("Hello Klim!")
lcd.move_to(0, 1)
lcd.putstr("Welcome back")
