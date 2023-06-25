from fpioa_manager import fm
from Maix import GPIO
import sensor, image, time, uos, utime
from machine import UART

# setup uart
fm.register(34, fm.fpioa.UART1_TX)
fm.register(35, fm.fpioa.UART1_RX)
uart_out = UART(UART.UART1, 115200, 8, None, 1, timeout=1000, read_buf_len=1)

# setup sensor
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

# setup buttons
fm.register(18, fm.fpioa.GPIO1)
button_a = GPIO(GPIO.GPIO1, GPIO.IN)

fm.register(19, fm.fpioa.GPIO2)
button_b = GPIO(GPIO.GPIO2, GPIO.IN)

status = True
i = 0

while True:

    if not button_a.value():
        status = not status

    if status:
        print('off')
        out = 1

        if not button_b.value():
            for j in uos.listdir('/sd'):
                try:
                    file_remove = '/sd/' + j
                    uos.remove(file_remove)
                    print(file_remove, 'removed')
                    out = 2

                except:
                    pass

    else:
        clock.tick()
        img = sensor.snapshot()
        i += 1
        file_save = '/sd/' + str(i) + '.jpg'
        img.save(file_save, quality=95)
        print('on', file_save, 'saved')
        out = 0

    uart_out.write(str(out))
    utime.sleep_ms(500)
