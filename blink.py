def blink():
    from machine import Pin
    from time import sleep

    led = Pin(2, Pin.OUT)
    
    for i in range(0, 9):
        led.value(not led.value())
        sleep(0.5)
    
    # esp8266 use 'on()' to turn off led (?!?!?)
    led.on()
