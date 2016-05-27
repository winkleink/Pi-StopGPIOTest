from gpiozero import LED
from time import sleep
green = LED(17)
amber = LED(27)
red = LED(22)

while True:
    green.on()
    amber.on()
    red.on()
    sleep(1)
    green.off()
    amber.off()
    red.off()
    sleep(1)
    
