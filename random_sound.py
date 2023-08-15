import pygame
import numpy as np

pygame.mixer.init(frequency=44100, size=-16, channels=2)

size = 44100
buffer = np.random.randint(-32768, 32767, size*2)
buffer = buffer.reshape(size, 2)

sound = pygame.sndarray.make_sound(buffer)
sound.play()
pygame.time.wait(int(sound.get_length() * 1000))