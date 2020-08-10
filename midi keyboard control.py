import pygame
import pygame.midi
import keyboard
import os, sys
abs_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(abs_path)
sys.path.append(abs_path)
with open('config.py', encoding='utf-8') as f:
    exec(f.read())
from musicpy.musicpy import *
os.chdir(abs_path)
midi_device_load = False
pygame.mixer.init(frequency, size, channel, buffer)


def has_load():
    global midi_device_load
    midi_device_load = True


def load(dic, path, file_format, volume):
    wavedict = {
        i: pygame.mixer.Sound(f'{path}{dic[i]}.{file_format}')
        for i in dic
    }
    if volume != None:
        [wavedict[x].set_volume(volume) for x in wavedict]
    return wavedict


def init_midi():
    global current_play
    global midi_delay_time
    global wavdic
    global device
    global last
    if not midi_device_load:
        has_load()
        pygame.mixer.set_num_channels(maxinum_channels)
        pygame.midi.init()
        try:
            device = pygame.midi.Input(midi_device_id)
        except:
            print('no midi devices detected')
            return 'error'
        midi_delay_time = int(delay_time * 1000)
    notenames = os.listdir(sound_path)
    notenames = [x[:x.index('.')] for x in notenames]
    wavdic = load({i: i
                   for i in notenames}, sound_path, sound_format,
                  global_volume)
    current_play = []
    last = current_play.copy()


def read_input():
    show = []
    while True:
        if device.poll():
            event = device.read(1)[0]
            data = event[0]
            timestamp = event[1]
            note_number = data[1]
            velocity = data[2]
            current_note = degree_to_note(note_number)
            if velocity == 0:
                if current_note in current_play:
                    current_play.remove(current_note)
                    current = key_settings[str(current_note)]
                    keyboard.release(current)
                    show.remove(current)
            else:
                if current_note not in current_play:
                    current_note_text = str(current_note)
                    if current_note_text in key_settings:
                        current = key_settings[current_note_text]
                        keyboard.press(current)
                        show.append(current)
                    current_play.append(current_note)
                    current_sound = wavdic[str(current_note)]
                    current_sound.set_volume(velocity / 127)
                    current_sound.play(maxtime=midi_delay_time)
            os.system('cls')
            print(show)


check = init_midi()
if check != 'error':
    read_input()
else:
    input()