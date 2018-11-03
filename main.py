from time import sleep
import machine, ssd1306
import iss

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3c)
interval = 10

while True:
    iss.overhead(oled, interval)
    
    sleep(interval)

    iss.get_location(oled)

    sleep(interval)
