import serial
import wave
from pygame import mixer
import pygame
import json


# Instantiate mixer
mixer.pre_init()
# mixer.init(48000, -16, 2, 512)
mixer.init(48000, 16, 2, 512) # unsigned

conversion_factor = 3.3 / 65535
pcm = 32768

# reading_1 = sensor_1.read_u16() * conversion_factor
# print(str(reading_1 - pcm) + "," + str(reading_2 - pcm))
# print(str(reading_1))

ser = serial.Serial(
    # Serial Port to read the data from
    # port='/dev/ttyACM0',
    port='/dev/pts/6',
    # port='COM24',

    # Rate at which the information is shared to the communication channel
    baudrate=1152000,

    # Applying Parity Checking (none in this case)
    parity=serial.PARITY_NONE,

    # Pattern of Bits to be read
    stopbits=serial.STOPBITS_ONE,

    # Total number of bits to be read
    bytesize=serial.EIGHTBITS,

    # Number of serial commands to accept before timing out
    timeout=1
)
# Pause the program for 1 second to avoid overworking the serial port

myArray = bytearray(b'')

for i in range(48000):
    y = ser.readline().strip()
    # print('y: ', y)
    if (y != b'') & (y.isdigit() & (len(y) < 5)):
        x = (int(y) - pcm).to_bytes(2, 'big', signed=True)
        myArray.extend(x)

        # print(x - pcm)
        # print('x: ',x)

print(myArray)

# with open("output.raw", "rb") as inp_f:
#     rawSample = inp_f.read()
#
# print(rawSample)

# data = myArray
# with wave.open("sound.wav", "wb") as out_f:
#     out_f.setnchannels(1)
#     out_f.setsampwidth(2)  # number of bytes
#     out_f.setframerate(11250)
#     out_f.writeframesraw(data)

# mixer.music.load('0.wav')

# print("music started playing....")

# # Set preferred volume
# mixer.music.set_volume(0.9)

# # Play the music
# mixer.music.play()

sound = mixer.Sound(myArray)

sound.play(0)
pygame.time.wait(int(sound.get_length() * 1000))


# with open('sine5.txt', 'w') as filehandle:
#     json.dump(myArray.toList(), filehandle)

