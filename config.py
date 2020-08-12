# basic screen settings


midi_keyboard_detect_interval = 10
repeat_interval = 0.3
mouse_move_distance = 30
mouse_move_duration = 0.1
screen_size = (1280, 650)
background_image = 'white.png'
background_size = None
piano_image = 'piano.png'
piano_size = None
message_color = (0, 0, 0, 255)
fonts_size = 20
label1_place = (300, 400)
label2_place = 300, 350
label3_place = 300, 450
label_anchor_x = 'left'
label_anchor_y = 'center'
fonts = 'Cambria'
bold = True
notes_image = 'playing.png'
notes_resize_num = 1.2
go_back_image = 'go_back.png'
go_back_place = 50, 550
self_play_image = 'play.png'
self_play_place = 50, 480
self_midi_image = 'midi_keyboard.png'
self_midi_place = 50, 410
play_midi_image = 'play_midi.png'
play_midi_place = 50, 340
button_resize_num = 2.3

# the key settings for playing 88 notes (from A1 to C9)
# (if you have sound files that beyond these range then you can
# modify this dictionary to play them)

key_settings = {
    'print screen': 'A1',
    'scroll lock': 'A#1',
    'insert': 'B1',
    'home': 'C2',
    'page up': 'C#2',
    'delete': 'D2',
    'end': 'D#2',
    'page down': 'E2',
    'esc': 'F2',
    '`': 'F#2',
    '=': 'G2',
    '\\': 'G#2',
    'ctrl': 'A2',    
    'alt': 'A#2',
    'tab': 'B2',
    'mouse move up': 'C3',
    'mouse move down': 'C#3',
    'mouse move left': 'D3',
    'mouse move right': 'D#3',
    'mouse middle click': 'E3',
    'mouse left click': 'F3',
    'mouse right click': 'F#3',
    '/': 'G3',
    '[': 'G#3',
    ']': 'A3',
    'left': 'A#3',
    'right': 'B3',
    'up': 'C4',
    'down': 'C#4',
    ';': 'D4',
    "'": 'D#4',
    ',': 'E4',
    '.': 'F4',
    "caps lock": 'F#4',
    'win': 'G4',
    'shift': 'G#4',
    'space': 'A4',
    'backspace': 'A#4',
    'enter': 'B4',
    'a': 'C5',
    'b': 'C#5',
    'c': 'D5',
    'd': 'D#5',
    'e': 'E5',
    'f': 'F5',
    'g': 'F#5',
    'h': 'G5',
    'i': 'G#5',
    'j': 'A5',
    'k': 'A#5',
    'l': 'B5',
    'm': 'C6',
    'n': 'C#6',
    'o': 'D6',
    'p': 'D#6',
    'q': 'E6',
    'r': 'F6',
    's': 'F#6',
    't': 'G6',
    'u': 'G#6',
    'v': 'A6',
    'w': 'A#6',
    'x': 'B6',
    'y': 'C7',
    'z': 'C#7',
    '0': 'D7',
    '1': 'D#7',
    '2': 'E7',
    '3': 'F7',
    '4': 'F#7',
    '5': 'G7',
    '6': 'G#7',
    '7': 'A7',
    '8': 'A#7',
    '9': 'B7',
    '-': 'C8',
    'f1': 'C#8',
    'f2': 'D8',
    'f3': 'D#8',
    'f4': 'E8',
    'f5': 'F8',
    'f6': 'F#8',
    'f7': 'G8',
    'f8': 'G#8',
    'f9': 'A8',
    'delete': 'A#8',
    'f11': 'B8',
    'f12': 'C9'
}

reverse_key_settings = {j: i for i, j in key_settings.items()}

# switching mode for self playing ('self'),
# or play midi ('show'),
# or play chords with self-configured playing chords keys settings ('chord')
mode = 'show'
self_device = 'pc'
midi_device_id = 1

# operation key settings for pause, unpause, repeat and so on
pause_key = 'space'
repeat_key = 'ctrl'
unpause_key = 'enter'
exit_key = 'esc'
pause_key_clear_notes = False

# show_key set to True will show what keyboard keys you are pressing
show_key = False

# if mode is 'show', you can set musicsheet as a musicpy sentence,
# or set the path of midi you want to play
musicsheet = "(chd('C','maj7').set(4,1))*3"

path = None

# these are the number of tracks of the midi you want to play from
track_ind = 2
track = 1

# the bpm you want to play
bpm = None

# play_interval: play the parts of the midi in this interval (percentages)
play_interval = None

# these are the init parameters of the mixer
frequency = 44100
size = -16
channel = 1
buffer = 1024
maxinum_channels = 100

global_volume = 0.6

# if delay is set to True, when you are self playing, the sounds will
# last for delay_time seconds
delay = True
delay_time = 6

# touch interval is when the sound is still on delay, if you re-press
# the key for the same key for that sound, the time interval between
# the last time you press the key and this time is beyond this interval,
# then the sound will stop and replay again, this paramter is used
# for pressing keys' sensitivity.
touch_interval = 0.1

# if this parameter is set to True,
# then it only reads the key you are actually pressing now,
# not to include the sounds on delay but you are not pressing
delay_only_read_current = True

# the suffix of the sound files
sound_format = 'wav'

# the path of the sounds folder
sound_path = 'sounds/'

# when the mode is in 'show' mode, the delay time for the sounds
show_delay_time = 1

# these are the parameters for chord types detections
# ignore_sort_from : avoid the detection result are sorting from another chord as much as possible
# change_from_first: detection result is preferentially chosen as changed from another chord(flat or sharp some notes)
# original_first: detection result is preferentially chosen as a variation of the original position of the chord(i.e. no inversion or any changes to the notes of the chord)
# ignore_add_from : detection result will ignore the result for adding notes from another chord
detect_mode = 'chord'
inv_num = False
rootpitch = 5
ignore_sort_from = False
change_from_first = True
original_first = True
ignore_add_from = True
same_note_special = False
whole_detect = True
return_fromchord = False
two_show_interval = True
poly_chord_first = False

# the operations on the midi you want to play
# show_change_pitch : a positive number: will sharp all the notes in the midi by the number; a negative number: same except flat all the notes
# show_modulation : [scale1, scale2] perform modulation from scale1 to scale2 on the notes in the midi
show_change_pitch = None
show_modulation = None

# if this is set to True, then you enable the config key during the playing
config_enable = True

# if you press the config key with the following keys, those keys will be able to adjust settings in realtime.
config_key = 'alt'

# volume change keys
volume_up = '='
volume_down = '-'

# volume change of each volume up/down
volume_change_unit = 0.05

# if delay is set to True before you press, then it will change to False, if False before then set to True
change_delay = 'd'
change_read_current = 'c'
change_pause_key_clear_notes = 'x'

# chords types for each key if you use 'chord' mode
# During the chord mode, if you press a root note key with a chord key,
# then the piano will play that chord types with the root note,
# you can set some keys for chord inversions (i.e. 1st inversion, 2nd inversion, ...),
# and you can even set keys for reversing a chord, and the tempo and interval of the
# chord could also be setted and changed.
CHORDKEY = {
    'num 0': 'maj',
    'decimal': 'm',
    'num 1': '7',
    'num 2': 'maj7',
    'num 3': 'm7',
    'num 4': 'dim7',
    'num 5': 'o7',
    'num 6': 'aug',
    'num 7': 'fifth 9th',
    'num 8': '5(+octave)',
    'num 9': 'mM7'
}

# keys for chord inversions and reversing
CHORD_MODIFY = {
    'f1': [1, 'inv'],
    'f2': [2, 'inv'],
    'f3': [3, 'inv'],
    'f4': [4, 'inv'],
    'f5': [0, 'reverse'],
    'f6': [1, 'inv_high']
}

# chords' intervals and durations (timing unit: miliseconds)
chord_interval = 0.3
chord_duration = 1
note_place = [
    (-2, 50), (11, 102), (24, 50), (45.25, 50), (58.25, 102), (71.25, 50),
    (84.25, 102), (97.25, 50), (118.5, 50), (131.5, 102), (144.5, 50),
    (157.5, 102), (170.5, 50), (183.5, 102), (196.5, 50), (217.75, 50),
    (230.75, 102), (243.75, 50), (256.75, 102), (269.75, 50), (291.0, 50),
    (304.0, 102), (317.0, 50), (330.0, 102), (343.0, 50), (356.0, 102),
    (369.0, 50), (390.25, 50), (403.25, 102), (416.25, 50), (429.25, 102),
    (442.25, 50), (463.5, 50), (476.5, 102), (489.5, 50), (502.5, 102),
    (515.5, 50), (528.5, 102), (541.5, 50), (562.75, 50), (575.75, 102),
    (588.75, 50), (601.75, 102), (614.75, 50), (636.0, 50), (649.0, 102),
    (662.0, 50), (675.0, 102), (688.0, 50), (701.0, 102), (714.0, 50),
    (735.25, 50), (748.25, 102), (761.25, 50), (774.25, 102), (787.25, 50),
    (808.5, 50), (821.5, 102), (834.5, 50), (847.5, 102), (860.5, 50),
    (873.5, 102), (886.5, 50), (907.75, 50), (920.75, 102), (933.75, 50),
    (946.75, 102), (959.75, 50), (981.0, 50), (994.0, 102), (1007.0, 50),
    (1020.0, 102), (1033.0, 50), (1046.0, 102), (1059.0, 50), (1080.25, 50),
    (1093.25, 102), (1106.25, 50), (1119.25, 102), (1132.25, 50), (1153.5, 50),
    (1166.5, 102), (1179.5, 50), (1192.5, 102), (1205.5, 50), (1218.5, 102),
    (1231.5, 50), (1252.75, 50)
]

# load sounds from the folders of sound paths when playing or not
load_sound = True

# detect chord types when the current notes change
show_chord = True

# names of intervals
perfect_unison = 0
minor_second = 1
augmented_unison = 1
major_second = 2
diminished_third = 2
minor_third = 3
augmented_second = 3
major_third = 4
diminished_fourth = 4
perfect_fourth = 5
augmented_third = 5
diminished_fifth = 6
augmented_fourth = 6
perfect_fifth = 7
diminished_sixth = 7
minor_sixth = 8
augmented_fifth = 8
major_sixth = 9
diminished_seventh = 9
minor_seventh = 10
augmented_sixth = 10
major_seventh = 11
diminished_octave = 11
perfect_octave = 12
octave = 12
augmented_seventh = 12

# the parameters of the function split_melody
melody_tol = minor_seventh
chord_tol = major_sixth

# notes showing mode: choose one from 'dots' and 'bars'
note_mode = 'bars'
bar_width = 14
bar_height = 20
bar_color = (124, 252, 0)
bar_y = 80
bar_offset_x = 9
bar_opacity = 160
opacity_change_by_velocity = True
# color mode: choose one from 'normal' and 'rainbow'
color_mode = 'rainbow'
bar_steps = 7
bar_unit = 50
bar_hold_increase = 5

# when play midi files, if you choose to merge all tracks, get_off_drums
# set to True will not merge the drum tracks if your midi file has
get_off_drums = True
