# ISS-Overhead-Check

Check International Space Station Pass Times Over 
Location using ESP8266 and [MicroPython](https://micropython.org/).

This project is created to run on my Nodemcu Wifi Esp8266 with Oled Display 128x32, can't test in others devices.

## Software Install

- Edit `boot.py` and update wifi credentials
- Edit `main.py` and change coords to your location.
- Upload both to controller

## Phisical Install

![Nodemcu Wifi Esp8266](assets/nodemcu-wifi-esp8266-12e-esp12-iot-0072-D_NQ_NP_726976-MLB26000601668_092017-F.webp)
![Nodecmu pins](assets/nodemcu-wifi-esp8266-12e-esp12-iot-0072-D_NQ_NP_825146-MLB26000607767_092017-F.webp)
![Oled display](assets/display-oled-branco-128x32-pixel-091-polegadas-4-pinos-i2c-D_NQ_NP_716164-MLB27547156742_062018-F.webp)
![Oled display](assets/display-oled-branco-128x32-pixel-091-polegadas-4-pinos-i2c-D_NQ_NP_912496-MLB27547182569_062018-F.webp)

Connect pins from oled display in nodecmu using pins:

- D1: SCL
- D2: SDA
- GND and VCC can be pluged on 3.3 pin from board and GND.

## LICENSE

GPL3<Plug>(neosnippet_expand)

