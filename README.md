# Pi-StopGPIOTest
python and Scratch Raspberry Pi GPIO tests using Pi-Stop from 4tronix

Simple code using 3 LEDS on Pi-Stop to quickly test if th GPIO pins are working using python and Scratch on the Raspberry Pi.

Attach the Pi-Stop as follows

GND - GND (Pin 6)
Green - BCM 14 (Pin 8)
Amber - BCM 15 (Pin 10)
Red - BCM 18 (Pin 12)

All these 4 pins are together so the Pi-Stop will slot right on.
To place the pi-stop on the Pi have the GPIO header at the top of the Pi with the USB ports on the right.
Then skip the first 2 pins on the top row and connect the GND to the 3rd pin.  This is GND on the PI.  Then Green, Amber and Red connect to pins 8,10,12 

If you don't have a Pi-Stop then with the GPIO Pins you could wire up 3 LEDs to these pins and the code will also work.
