from time import sleep
from utime import localtime
from urequests import get
from blink import blink

BASE_URL = "http://api.open-notify.org/"
LATITUDE = -27.591665
LONGITUDE = -48.589599
ALTITUDE = 12

def overhead(oled, interval):
    url = (BASE_URL + "iss-pass.json?lat={}&lon={}&alt={}").format(LATITUDE, LONGITUDE, ALTITUDE)
    response = get(url)
    content = response.json()
    oled.fill(0)

    if (content['message'] == 'success'):
        line = 5
        column = 5
        counter = 0

        for overhead in content['response']:
            ts = overhead['risetime']
            duration = overhead['duration']
            year, month, day, hour, minute, seconds, epoc, other = localtime(ts)
            
            oled.text("{}/{} - {}:{}".format(day, month, hour, minute), column, line)
            oled.show()

            line = line + 10
            counter = counter + 1

            if (counter == 3):
                sleep(interval)

                line = 5

                oled.fill(0)
    else:
        oled.text("Invalid response.", 0, 0)
        oled.text("Check parameters.", 0, 10)
        oled.show()

def get_location(oled):
    url = BASE_URL + "iss-now.json"
    response = get(url)
    content = response.json()
    oled.fill(0)

    if (content['message'] == 'success'):
        iss_position = content['iss_position']
        iss_latitude = iss_position['latitude']
        iss_longitude = iss_position['longitude']
        iss_timestamp = content['timestamp']
        year, month, day, hour, minute, seconds, epoc, other = localtime(iss_timestamp)
            
        oled.text("Lat: {}".format(iss_latitude), 0, 0)
        oled.text("Long: {}".format(iss_longitude), 0, 10)
        oled.text("Time: {}:{}".format(hour, minute), 0, 20)
        oled.show()
    else:
        oled.text("Invalid response.", 0, 0)
        oled.text("Check parameters.", 0, 10)
        oled.show()
