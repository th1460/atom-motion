import machine
import struct
import network
import socket
import neopixel

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

def get_speed():
    return struct.unpack('b', i2c.readfrom_mem(device, 0, 1))[0]

def set_angle(angle):
    buf = bytearray(1)
    struct.pack_into('b', buf, 0, angle)
    i2c.writeto_mem(device, 2, buf)

def get_angle():
    return struct.unpack('b', i2c.readfrom_mem(device, 2, 1))[0]


def set_direction(x):
    if x > 200:
        set_angle(65)
    elif x < 50:
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

# create access-point
ap = network.WLAN(network.AP_IF)
ap.config(essid='ATOM-MOTION')
ap.config(max_clients=10)
ap.active(True)

# create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 12000))
np[0] = (0,255,0)
np.write()

while True:
    direction, address_client = server.recvfrom(2048)
    out = struct.unpack('BBB', direction)
    set_direction(out[0])
    set_run(out[1])
    print(out)

