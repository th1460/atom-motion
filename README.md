# Atom Motion


## Install ESP32 firmware

To download the firmware: https://micropython.org/download/esp32/

    # Install esptool
    pip install esptool

    # Erase device
    esptool.py --port /dev/ttyUSB0 erase_flash

    # Install firmware
    esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 750000 write_flash -z 0x1000 esp32-20210902-v1.17.bin

## Atom Motion controled by Joystick

``` mermaid
flowchart LR
    A[<img src='/docs/joystick.png'/>Joystick]
    B[<img src='https://raw.githubusercontent.com/th1460/atom-motion/refs/heads/main/docs/atom-lite.png'/>Atom Lite]
    C[<img src='https://raw.githubusercontent.com/th1460/atom-motion/refs/heads/main/docs/atom-motion.png'/>Atom Motion]
    D[<img src='https://raw.githubusercontent.com/th1460/atom-motion/refs/heads/main/docs/servo-180.png'/>Servo 180]
    E[<img src='https://raw.githubusercontent.com/th1460/atom-motion/refs/heads/main/docs/servo-360.png'/>Servo 360]
    A --> |I2C| B
    B -.-> |Socket| C
    C --> |I2C| D
    C --> |I2C| E

```
