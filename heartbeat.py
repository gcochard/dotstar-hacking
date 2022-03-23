import board
import digitalio
import busio
import time
import random

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.175)
    led.value = False
    time.sleep(0.1)
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(1.15)
