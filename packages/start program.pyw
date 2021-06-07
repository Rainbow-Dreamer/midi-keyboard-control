import pygame
import pygame.midi
import keyboard
import mouse
import os
import sys
import time
from tkinter import *
from tkinter import ttk
from musicpy import *

abs_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(abs_path)
sys.path.append(abs_path)
with open('packages/midi keyboard control.pyw', encoding='utf-8') as f:
    exec(f.read())