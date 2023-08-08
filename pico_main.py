import machine
import utime

# from machine import Pin

# pinIn = Pin(1, Pin.IN,Pin.PULL_DOWN)
# pinIn = Pin(2, Pin.IN,Pin.PULL_DOWN)


sensor_1 = machine.ADC(26)

# sensor_2 = machine.ADC(2)
# sensor_3 = machine.ADC(3)
# sensor_4 = machine.ADC(4)


pcm = 32768

# conversion_factor = 3.3 / (65535)
# conversion_factor = 3.3 / (pcm)

conversion_factor = 1

while True:
    reading_1 = sensor_1.read_u16() * conversion_factor
    # reading_2 = sensor_2.read_u16() * conversion_factor
    # reading_3 = sensor_3.read_u16() * conversion_factor
    # reading_4 = sensor_4.read_u16() * conversion_factor

    # temperature = 27 - (reading - 0.706)/0.001721
    # print(str(reading_1 - pcm) + "," + str(reading_2 - pcm))
    print(str(reading_1))

    # print(reading_2)
    # print(reading_3)
    # print(reading_4)
    # print("====================")
    # utime.sleep(0.001)
    utime.sleep(0.0001)

