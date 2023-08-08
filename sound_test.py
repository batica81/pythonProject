from pygame import mixer
import pygame


# Instantiate mixer
mixer.pre_init()
mixer.init(48000,-16,2,512)


mixer.music.load('0.wav')

print("music started playing....")

# Set preferred volume
mixer.music.set_volume(0.2)

# Play the music
mixer.music.play()
