import pygame
import numpy as np
import json

pygame.mixer.init(size=32)

buffer = np.sin(2 * np.pi * np.arange(44100) * 440 / 44100).astype(np.float32)
print(buffer)
sound = pygame.mixer.Sound(buffer)

sound.play(0)
pygame.time.wait(int(sound.get_length() * 1000))


with open('sine5.txt', 'w') as filehandle:
    json.dump(buffer.toList(), filehandle)

