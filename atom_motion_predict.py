import machine
import struct
import network
import socket
import neopixel
import utime

# setup uart
uart = machine.UART(1, tx=19, rx=22)
uart.init(115200, bits=8, parity=0, stop=0)

# setup led
np = neopixel.NeoPixel(machine.Pin(27), 1)

# setup servo and motor
sda_pin = machine.Pin(25)
scl_pin = machine.Pin(21)

i2c = machine.I2C(0, sda=sda_pin, scl=scl_pin, freq=400000)
devices = i2c.scan()

device = [i for i in devices if hex(i) == '0x38'][0]

def set_speed(speed):
    buf = bytearray(1)
    struct.pack_into('b', buf, 0, speed)
    i2c.writeto_mem(device, 0, buf)

def set_angle(angle):
    buf = bytearray(1)
    struct.pack_into('b', buf, 0, angle)
    i2c.writeto_mem(device, 2, buf)

def set_direction(x):
    if x == 0:
        set_angle(65)
    elif x == 1:
        set_angle(115)
    else:
        set_angle(90)
        
def set_run(x):
    if x > 200:
        set_speed(127)
    elif x < 50:
        set_speed(0)
    else:
        set_speed(86)
        
while True:
    try:
        out = uart.read(1)
        print(out.decode())
        
        set_direction(int(out))
    except:
        pass
