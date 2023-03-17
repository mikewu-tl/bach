import pygame
import base64

def play_music(music_file):
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
    except pygame.error:
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)

music_file = "audio/invent13.mid"
# mid64=base64.encodebytes(open(music_file, 'rb').read())

freq = 44100 # CD quality
bitsize = -16
channels = 2    # stereo
buffer = 1024    # sample rate
pygame.mixer.init(freq, bitsize, channels, buffer)

pygame.mixer.music.set_volume(0.8)

try:
    play_music(music_file)
except KeyboardInterrupt:
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit