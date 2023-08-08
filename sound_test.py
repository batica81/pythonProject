from pygame import mixer
import pygame

import pygame._sdl2 as sdl2

pygame.init()
is_capture = 0  # zero to request playback devices, non-zero to request recording devices
num = sdl2.get_num_audio_devices(is_capture)
names = [str(sdl2.get_audio_device_name(i, is_capture), encoding="utf-8") for i in range(num)]
print("\n".join(names))
pygame.quit()


# Instantiate mixer
mixer.pre_init()
mixer.init(48000,-16,2,512)


mixer.music.load('0.wav')

print("music started playing....")

# Set preferred volume
mixer.music.set_volume(0.2)

# Play the music
mixer.music.play()
