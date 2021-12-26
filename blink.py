# This code will cause the LED on a Raspberry Pi Pico (flashed for MicroPython) to blink.
# Changing the frequency number on line 11 will change the blink rate (higher = faster).

from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=5, mode=Timer.PERIODIC, callback=blink)
