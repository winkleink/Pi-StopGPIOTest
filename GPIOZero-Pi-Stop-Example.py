from gpiozero import LED
from time import sleep
green = LED(14)
amber = LED(15)
red = LED(18)

while True:
    green.on()
    amber.on()
    red.on()
    sleep(1)
    green.off()
    amber.off()
    red.off()
    sleep(1)
    
