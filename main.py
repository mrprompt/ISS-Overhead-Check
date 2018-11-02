from time import sleep
from utime import localtime
from urequests import get

BASE_URL = "http://api.open-notify.org/iss-pass.json?lat={}&lon={}&alt={}"
LATITUDE = -27.591665
LONGITUDE = -48.589599
ALTITUDE = 12
INTERVAL = 300

while True:
    url = BASE_URL.format(LATITUDE, LONGITUDE, ALTITUDE)
    response = get(url)
    content = response.json()

    if (content['message'] == 'success'):
        for overhead in content['response']:
            ts = overhead['risetime']
            
            print(localtime(ts))
    else:
        print("Invalid response from API, check parameters.")

    sleep(INTERVAL)
