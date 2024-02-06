from machine import Pin, ADC
import time

led = Pin(21, Pin.OUT)
adc_thing = ADC(Pin(26))
print(adc_thing.read_u16())

while True:
    adc_reading = adc_thing.read_u16()
    time_wait = adc_reading/65535
    led.on()
    time.sleep(time_wait)
    led.off()
    time.sleep(time_wait)
    #led.value(0)

