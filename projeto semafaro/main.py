from machine import Pin
from utime import sleep

print("hello word!")

ledRed = Pin(15, Pin.OUT)
ledGreen = Pin(17, Pin.OUT)
ledYellow = Pin(16, Pin.OUT)

while True:
    ledGreen.on()
    print("Verde ON")
    sleep(20)
    ledGreen.off()
    print("Verde OFF")
    sleep(0.5)
    
    ledYellow.on()
    print("Amarelo ON")
    sleep(10)
    ledYellow.off()
    print("Amarelo OFF")
    sleep(0.5)

    ledRed.on()
    print("Vermelho ON")
    sleep(7)
    ledRed.off()
    print("Vermelho OFF")
    sleep(0.5)
