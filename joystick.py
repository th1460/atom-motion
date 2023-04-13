import machine
import struct
import network
import socket
import neopixel
import time

# setup led
np = neopixel.NeoPixel(machine.Pin(27), 1)

# setup joystick
sda_pin = machine.Pin(26)
scl_pin = machine.Pin(32)

i2c = machine.I2C(0, sda=sda_pin, scl=scl_pin, freq=400000)
devices = i2c.scan()
device = [i for i in devices if hex(i) == '0x52'][0]

# create access-point
def ap_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ATOM-MOTION')
        while not wlan.isconnected():
            pass
    print('network config', wlan.ifconfig())

ap_connect()

# create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# green led
np[0] = (0,255,0)
np.write()

while True:
    client.sendto(i2c.readfrom(device, 3), ('192.168.4.1', 12000))
    time.sleep(1)
