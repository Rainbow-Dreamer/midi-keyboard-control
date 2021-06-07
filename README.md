# Midi Keyboard Control

## This software can make you control your computer with your midi keyboard, or any midi inputs from DAW

![image](https://github.com/Rainbow-Dreamer/midi_keyboard_control/blob/master/previews/1.jpg)

This software is very easy to use, just plug in your midi keyboard to your computer, or initialize virtual midi ports and connect them to your DAWs or any softwares that have midi output functions, and then open this software, then you can play your midi keyboard to control your computer.

You can customize the corresponding computer actions of each key played from your midi keyboard or DAWs, just change `key_settings` dictionary in the file `config.py` in `packages` folder, or you can use `change_settings.exe` in `tools` folder to change configs more easily.

The computer actions including key press of keys on your computer keyboard, move your mouse with a direction, left/right/middle click of your mouse.

You can change the value of `midi_device_id` in `config.py` in `packages` folder to match the device id of your midi keyboard, so if you see error messages when you open the software, you can change the device id so that the software can read the midi outputs from your midi keyboard.

If you are not using a midi keyboard when you open the software, you can initialize virtual midi ports and connect them to your DAWs or any softwares that have midi output functions. I recommend using `loopMIDI` to initialize virtual midi ports, because it is very convenient.

### 使用你的midi键盘来当做电脑键盘玩电脑
