from machine import Pin
import utime
from machine import Pin, Timer


trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
led = Pin(22, Pin.OUT)
timer = Timer()


def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(4)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    if 10 < int(distance) < 12:
        led.toggle()
        utime.sleep(1)

    #print(distance, "cm")


while True:
    ultra()
