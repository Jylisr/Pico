from machine import Pin
import time

sw = Pin(22, pull = Pin.PULL_UP, mode=Pin.IN)
led = Pin(22, Pin.OUT)
led.off()
val = 0
while True:
    if not sw.value():
        val ^=1
        led.value(val)
        while not sw.value():
            pass
        time.sleep_ms(50)