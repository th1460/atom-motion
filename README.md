# atom-motion

## Install esp32 firmware

To download the firmware: https://micropython.org/download/esp32/

```
# Install esptool
pip3 install esptool

# Erase device
esptool.py --port /dev/ttyUSB0 erase_flash

# Install firmware
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 750000 write_flash -z 0x1000 esp32-20210902-v1.17.bin
```

## Install maixpy firmware

>[Maixpy](https://github.com/sipeed/MaixPy) is designed to make AIOT programming easier, based on the Micropython syntax, running on a very powerful embedded AIOT chip K210.

To download the firmware: https://dl.sipeed.com/MAIX/MaixPy/release/master/

```
# Install kflash (https://github.com/kendryte/kflash.py)
pip3 install kflash

# Install  firmware
kflash -p /dev/ttyUSB0 -b 1500000 -B goE ~/Downloads/maixpy_v0.6.2_84_g8fcd84a58_m5stickv.bin
```
