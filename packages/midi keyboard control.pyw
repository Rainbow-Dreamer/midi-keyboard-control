with open('packages/config.py', encoding='utf-8') as f:
    exec(f.read())
os.chdir(abs_path)
pygame.mixer.init(frequency, size, channel, buffer)
pygame.mixer.set_num_channels(maxinum_channels)
pygame.midi.init()


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
    try:
        device = pygame.midi.Input(midi_device_id)
    except Exception as e:
        print(str(e))
        return 'error'
    midi_delay_time = int(delay_time * 1000)
    notenames = os.listdir(sound_path)
    notenames = [x[:x.index('.')] for x in notenames]
    wavdic = load({i: i
                   for i in notenames}, sound_path, sound_format,
                  global_volume)
    current_play = []


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
            mouse.move(0,
                       -mouse_move_distance,
                       absolute=False,
                       duration=mouse_move_duration)
        elif current == 'mouse move down':
            mouse.move(0,
                       mouse_move_distance,
                       absolute=False,
                       duration=mouse_move_duration)
        elif current == 'mouse move left':
            mouse.move(-mouse_move_distance,
                       0,
                       absolute=False,
                       duration=mouse_move_duration)
        elif current == 'mouse move right':
            mouse.move(mouse_move_distance,
                       0,
                       absolute=False,
                       duration=mouse_move_duration)


show = []


class midi_key(str):
    pass


class Root(Tk):

    def __init__(self):
        super(Root, self).__init__()
        self.title("midi keyboard control")
        self.minsize(*screen_size)
        self.detect_msg = ttk.Label(self,
                                    text='',
                                    font=(fonts, fonts_size, bold))
        self.current_playing = StringVar()
        self.current_play_msg = ttk.Label(self,
                                          textvariable=self.current_playing)
        self.current_play_msg.configure(font=(fonts, fonts_size, bold))

        midi_info = []
        counter = 0
        while True:
            current = counter, pygame.midi.get_device_info(counter)
            counter += 1
            if current[1] is None:
                break
            midi_info.append(current)

        self.midi_inputs = [
            (i[0], f'{i[1][0].decode("utf-8")}, {i[1][1].decode("utf-8")}')
            for i in midi_info if i[1][2] == 1
        ]
        self.midi_outputs = [
            (i[0], f'{i[1][0].decode("utf-8")}, {i[1][1].decode("utf-8")}')
            for i in midi_info if i[1][2] == 0
        ]
        self.midi_ports = self.midi_inputs + self.midi_outputs
        self.midi_outputs.insert(0, (-1, ''))
        self.midi_input_label = ttk.Label(self, text='MIDI Input Driver')
        self.midi_input_label.place(x=0, y=50)
        self.choose_midi_input_device = ttk.Combobox(
            self,
            values=[i[1] for i in self.midi_inputs],
            width=40,
            state='readonly')
        if self.midi_inputs:
            self.choose_midi_input_device.current(0)
        self.choose_midi_input_device.place(x=120, y=50)

        self.midi_output_label = ttk.Label(self, text='MIDI Output Driver')
        self.midi_output_label.place(x=450, y=50)
        self.choose_midi_output_device = ttk.Combobox(
            self,
            values=[i[1] for i in self.midi_outputs],
            width=40,
            state='readonly')
        if self.midi_outputs:
            self.choose_midi_output_device.current(0)
        self.choose_midi_output_device.place(x=580, y=50)

        self.midi_input_ind = 0
        global midi_device_id
        if self.midi_inputs:
            self.midi_device_id = self.midi_inputs[0][0]
        else:
            self.midi_device_id = 0
        midi_device_id = self.midi_device_id

        if self.midi_outputs:
            self.midi_device_output_id = self.midi_outputs[0][0]
        else:
            self.midi_device_output_id = 0

        self.choose_midi_input_device.bind(
            '<<ComboboxSelected>>', lambda e: self.change_midi_device_id())
        self.choose_midi_output_device.bind(
            '<<ComboboxSelected>>',
            lambda e: self.change_midi_output_device_id())

        self.stop_read_input = False

        self.change_settings_button = ttk.Button(
            self, text='Change Settings', command=self.open_change_settings)
        self.change_settings_button.place(x=0, y=450)
        self.open_settings = False

        check = init_midi()
        if check == 'error':
            self.detect_msg.configure(
                text='no midi devices detected, please check again')
            self.detect_msg.place(x=0, y=150)
        else:
            self.current_playing.set(
                f'currently playing:  {current_play}\n\ncorresponding keys:  {show}'
            )
            self.current_play_msg.place(x=0, y=150)
            self.read_input()

    def open_change_settings(self):
        if not self.open_settings:
            self.open_settings = True
        else:
            root2.focus_force()
            return
        os.chdir('packages')
        with open('change_settings.pyw', encoding='utf-8') as f:
            exec(f.read(), globals(), globals())

    def change_midi_device_id(self):
        self.focus_set()
        self.stop_read_input = True
        self.update()
        global current_play
        for each in show:
            keyboard.release(each)
        current_play.clear()
        show.clear()
        current_midi_input = self.choose_midi_input_device.get()
        self.midi_device_id = self.midi_inputs[[
            i[1] for i in self.midi_inputs
        ].index(current_midi_input)][0]
        global midi_device_id
        midi_device_id = self.midi_device_id
        check = 'good'
        try:
            pygame.midi.quit()
            pygame.midi.init()
            global device
            device = pygame.midi.Input(midi_device_id)
        except Exception as e:
            print(str(e))
            check = 'error'
        if check == 'error':
            self.current_play_msg.place_forget()
            self.detect_msg.configure(
                text='no midi devices detected, please check again')
            self.detect_msg.place(x=0, y=150)
        else:
            self.detect_msg.place_forget()
            self.current_playing.set(
                f'currently playing:  {current_play}\n\ncorresponding keys:  {show}'
            )
            self.current_play_msg.place(x=0, y=150)
            self.read_input()

    def change_midi_output_device_id(self):
        self.focus_set()
        current_midi_output = self.choose_midi_output_device.get()
        self.midi_device_output_id = self.midi_outputs[[
            i[1] for i in self.midi_outputs
        ].index(current_midi_output)][0]

    def read_input(self):
        if self.stop_read_input:
            self.stop_read_input = False
            return
        current_time = time.time()
        if device.poll():
            event = device.read(1)[0]
            data = event[0]
            msg_type = data[0]
            timestamp = event[1]
            note_number = data[1]
            velocity = data[2]
            current_note = degree_to_note(note_number)
            if msg_type in [128, 144]:
                if velocity == 0 or msg_type == 128:
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
                            current = midi_key(
                                reverse_key_settings[current_note_text])
                            current.current_time = current_time
                            play_key(current)
                            show.append(current)
                            current_play.append(current_note)
                            current_sound = wavdic[str(current_note)]
                            current_sound.set_volume(velocity / 127)
                            current_sound.play(maxtime=midi_delay_time)
            self.current_playing.set(
                f'currently playing:  {current_play}\n\ncorresponding keys:  {show}'
            )
        for current in show:
            if current_time - current.current_time >= repeat_interval:
                play_key(current)
                current.current_time = current_time
        self.after(midi_keyboard_detect_interval, self.read_input)


root = Root()
root.lift()
root.attributes("-topmost", True)
root.attributes("-topmost", 0)
root.mainloop()