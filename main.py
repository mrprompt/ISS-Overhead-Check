from time import sleep
from utime import localtime
from urequests import get
import machine, ssd1306

BASE_URL = "http://api.open-notify.org/iss-pass.json?lat={}&lon={}&alt={}"
LATITUDE = -27.591665
LONGITUDE = -48.589599
ALTITUDE = 12
INTERVAL = 10

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3c)

while True:
    url = BASE_URL.format(LATITUDE, LONGITUDE, ALTITUDE)
    response = get(url)
    content = response.json()

    oled.fill(0)

    if (content['message'] == 'success'):
        line = 5
        column = 5
        counter = 0

        for overhead in content['response']:
            ts = overhead['risetime']
            year, month, day, hour, minute, seconds, epoc, other = localtime(ts)
            
            oled.text("{}/{} - {}:{}".format(day, month, hour, minute), column, line)
            oled.show()

            line = line + 10
            counter = counter + 1

            if (counter == 3):
                sleep(10)

                line = 5

                oled.fill(0)
    else:
        oled.text("Invalid response.", 0, 0)
        oled.text("Check parameters.", 0, 10)
        oled.show()
    
    sleep(INTERVAL)
