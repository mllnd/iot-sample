import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("itcollege")

import sys
import uwebsockets
from machine import Pin, PWM
led = PWM(Pin(14, mode=Pin.OUT), freq=400) # SCK LED on WeMos D1
uri = "ws://iot.koodur.com:80/ws/mllnd-xyz"
print("Connecting to:", uri)
conn = uwebsockets.connect(uri)
conn.send("alive")
while True:
    print("Reading message...")
    try:
        fin, opcode, data = conn.read_frame()
    except OSError: # Connection timeout or reset
        sys.exit() # Soft reset
    if data.startswith(b"duty:"):
        led.duty(int(data[5:]))
    else:
        print("Got unknown command:", data)
