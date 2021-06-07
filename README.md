# Midi Keyboard Control

English [中文](#这个软件可以让你用你的midi键盘或DAW控制你的电脑)

## This software can make you control your computer with your midi keyboard or DAW

![image](https://github.com/Rainbow-Dreamer/midi_keyboard_control/blob/master/previews/1.jpg?raw=true)

This software is very easy to use, just plug in your midi keyboard to your computer, or initialize virtual midi ports and connect them to your DAWs or any softwares that have midi output functions, and then open this software, then you can play your midi keyboard to control your computer.

You can customize the corresponding computer actions of each key played from your midi keyboard or DAWs, just change `key_settings` dictionary in the file `config.py` in `packages` folder, or you can use `change_settings.exe` in `tools` folder to change configs more easily (the same as click `Change Settings` button in main window).

The computer actions including key press of keys on your computer keyboard, move your mouse with a direction, left/right/middle click of your mouse.

You can choose the MIDI input driver that matches your name of midi keyboard or virtual midi ports in the MIDI input driver selection menu. The MIDI output driver selection menu will not affected what we want to do (although you can change it anyway).

If you are not using a midi keyboard when you open the software, you can initialize virtual midi ports and connect them to your DAWs or any softwares that have midi output functions. I recommend using `loopMIDI` to initialize virtual midi ports, because it is very convenient.

## 这个软件可以让你用你的midi键盘或DAW控制你的电脑

[English](#Midi-Keyboard-Control) 中文

![image](https://github.com/Rainbow-Dreamer/midi_keyboard_control/blob/master/previews/1.jpg?raw=true)

本软件的使用非常简单，只需将你的midi键盘插入电脑，或者初始化虚拟midi端口并连接到DAW或任何具有midi输出功能的软件上，然后打开本软件，就可以通过midi键盘来控制你的电脑。

你可以自定义你的midi键盘或DAW播放的每个键所对应的电脑动作，只需修改`packages`文件夹下`config.py`文件中的`key_settings`字典，或者你可以使用`tools`文件夹下的`change_settings.exe`来更方便地修改配置（与点击主窗口的`Change Settings`按钮一样）。

电脑动作包括按电脑键盘上的键，移动鼠标的方向，鼠标的左/右/中键。

你可以在MIDI输入驱动选择菜单中选择与你的MIDI键盘或虚拟MIDI端口名称相符的MIDI输入驱动。MIDI输出驱动选择菜单不会影响我们要做的事情（尽管你无论如何可以改变它）。

如果你在打开软件时没有使用midi键盘，你可以初始化虚拟midi端口，并将它们连接到DAW或任何有midi输出功能的软件上。我推荐使用`loopMIDI`来初始化虚拟 midi 端口，因为它非常方便。
