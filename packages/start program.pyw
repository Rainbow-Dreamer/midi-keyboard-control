import pygame
import pygame.midi
import keyboard
import mouse
import os
import sys
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from ast import literal_eval
import mido_fix
import chunk
import fractions

abs_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(abs_path)
sys.path.append(abs_path)
sys.path.append('packages')
with open('packages/musicpy/__init__.py', encoding='utf-8') as f:
    exec(f.read())
with open('packages/midi keyboard control.pyw', encoding='utf-8') as f:
    exec(f.read())