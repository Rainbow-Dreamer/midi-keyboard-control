import pygame
import pygame.midi
import keyboard
import mouse
import os
import sys
import time
from tkinter import *
from tkinter import ttk
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
            return 'error'
        midi_delay_time = int(delay_time * 1000)
    notenames = os.listdir(sound_path)
    notenames = [x[:x.index('.')] for x in notenames]
    wavdic = load({i: i
                   for i in notenames}, sound_path, sound_format,
                  global_volume)
    current_play = []
    last = current_play.copy()


def play_key(current):
    if 'mouse' not in current:
        keyboard.press(current)
    else:
        if current == 'mouse left click':
            mouse.click('left')
        elif current == 'mouse right click':
            mouse.click('right')
        elif current == 'mouse middle click':
            mouse.click('middle')
        elif current == 'mouse move up':
            mouse.move(0, -mouse_move_distance, absolute=False, duration=mouse_move_duration)
        elif current == 'mouse move down':
            mouse.move(0, mouse_move_distance, absolute=False, duration=mouse_move_duration)
        elif current == 'mouse move left':
            mouse.move(-mouse_move_distance, 0, absolute=False, duration=mouse_move_duration)
        elif current == 'mouse move right':
            mouse.move(mouse_move_distance, 0, absolute=False, duration=mouse_move_duration)                   


show = []

class midi_key(str):
    pass


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("midi keyboard control")
        self.minsize(900, 500)
        self.detect_msg = ttk.Label(self,text='')
        self.current_playing = StringVar()
        self.current_play_msg = ttk.Label(self, textvariable=self.current_playing)
        self.current_play_msg.configure(font=(fonts, fonts_size))
        check = init_midi()
        if check == 'error':
            self.detect_msg.configure(text='no midi devices detected, please check again')
            self.detect_msg.place(x=0, y=50)
        else:
            self.current_play_msg.place(x=0, y=100)
            self.current_playing.set(f'currently playing:  {current_play}\n\ncorresponding keys:  {show}')
            self.read_input()        
    
    
    def read_input(self):
        current_time = time.time()
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
                    current = reverse_key_settings[str(current_note)]
                    if 'mouse' not in current:
                        keyboard.release(current)
                    show.remove(current)
            else:
                if current_note not in current_play:
                    current_note_text = str(current_note)
                    
                    if current_note_text in reverse_key_settings:
                        current = midi_key(reverse_key_settings[current_note_text])
                        current.current_time = current_time
                        play_key(current)        
                    show.append(current)
                    current_play.append(current_note)
                    current_sound = wavdic[str(current_note)]
                    current_sound.set_volume(velocity / 127)
                    current_sound.play(maxtime=midi_delay_time)
            self.current_playing.set(f'currently playing:  {current_play}\n\ncorresponding keys:  {show}')
        for current in show:
            if current_time - current.current_time >= repeat_interval:
                play_key(current)
                current.current_time  = current_time
        self.after(midi_keyboard_detect_interval, self.read_input)


root = Root()
root.lift()
root.attributes("-topmost", True)
root.mainloop()
