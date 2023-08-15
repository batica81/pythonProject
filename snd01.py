#!/usr/bin/env python

import serial
import pygame
import numpy
import time
import json

numpy.set_printoptions(threshold=numpy.inf)

# ser = serial.Serial('COM10', baudrate=9600)
ser = serial.Serial('COM1', baudrate=9600)
previous_dsr = False
count = 0
sampleRate = 192000

#############################################

freq = 800
fileName = 'array_' + str(freq) + '.txt'

pygame.mixer.pre_init(sampleRate, -16, 2, 512)
pygame.mixer.init()

try:
    # check to see if file is readable
    with open(fileName) as tempFile:
        arr = json.loads(tempFile.read())

except Exception as e:

    arr = numpy.array([16384 * numpy.sin(2.0 * numpy.pi * freq * x / sampleRate) for x in range(0, int(sampleRate/100))]).astype(
        numpy.int16)

    # arr = numpy.array([16384 * numpy.sin(2.0 * numpy.pi * freq * x / sampleRate) for x in range(0, int(sampleRate/100))]).astype(
    #     numpy.int16)

    with open(fileName, 'w') as filehandle:
        json.dump(arr.tolist(), filehandle)

# arr1 = numpy.array([15000 * numpy.sin(2.0 * numpy.pi * (freq - 100) * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
arr2 = numpy.c_[arr, arr]
# print(str(arr2))
sound = pygame.sndarray.make_sound(arr2)
sound.set_volume(0.2)

# Main loop to monitor DSR signal and play/stop the beep
while True:
    # Read the current DSR state
    current_dsr = ser.dsr

    # Check if DSR state has changed
    if current_dsr != previous_dsr:
        if current_dsr:
            # print("key down "  + str(count))
            # count += 1
            sound.play(-1)

        else:
            # print("key up")
            sound.stop()

    # Update the previous DSR state
    previous_dsr = current_dsr
    time.sleep(0.001)  # debounce
