#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  joy.py
#  
#  Copyright 2017 Matthew Mashewske <matthew@matthew-W65-67SJ>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
import uinput
import time
import mem

def createController():
    events = (
        uinput.BTN_JOYSTICK,
        uinput.BTN_A,
        uinput.BTN_B,
        uinput.BTN_X,
        uinput.BTN_Y,
        uinput.BTN_TL,
        uinput.BTN_TR,
        uinput.BTN_TL2,
        uinput.BTN_TR2,
        uinput.BTN_SELECT,
        uinput.BTN_START,
        uinput.ABS_HAT0Y + (-1, 1, 0, 0),
        uinput.ABS_HAT0X + (-1, 1, 0, 0)
        )
    
    return uinput.Device(events)

def press(button, controller):
    if(button == '4'):
        controller.emit(uinput.ABS_HAT0X, -1)
        return True
    elif(button == '6'):
        controller.emit(uinput.ABS_HAT0X, 1)
        return True
    
    elif(button == '5x'):
        controller.emit(uinput.ABS_HAT0X, 0)
        return True
    elif(button == '2'):
        controller.emit(uinput.ABS_HAT0Y, 1)
        return True
    elif(button == '8'):
        controller.emit(uinput.ABS_HAT0Y, -1)
        return True
    elif(button == '5y'):
        controller.emit(uinput.ABS_HAT0Y, 0)
        return True
    elif(button == 'q'):
        press('2', controller)
        press('6', controller)
        press('5y', controller)
        return True
    elif(button == 'b'):
        press('2', controller)
        press('6', controller)
        press('5y', controller)
        return True
    elif(button == 'h'):
        press('4', controller)
        press('2', controller)
        press('5x', controller)
        press('6', controller)
        press('5y', controller)
        return True
    elif(button == 'g'):
        press('6', controller)
        press('2', controller)
        press('5x', controller)
        press('4', controller)
        press('5y', controller)
        return True
    elif(button == 'w'):
        press('6', controller)
        press('2', controller)
        press('5x', controller)
        press('4', controller)
        press('5y', controller)
        press('8', controller)
        press('5x', controller)
        press('6', controller)
        press('5y', controller)
        return True
    elif(button == 'z'):
        press('6', controller)
        press('2', controller)
        press('5y', controller)
        return True
    elif(button == 's'):
        press('4', controller)
        press('2', controller)
        press('5y', controller)
        return True
    elif(button == 'i'):
        controller.emit(uinput.BTN_X, 1)
        time.sleep(.02)
        controller.emit(uinput.BTN_X, 0)
        return True
    elif(button == 'o'):
        controller.emit(uinput.BTN_Y, 1)
        time.sleep(.02)
        controller.emit(uinput.BTN_Y, 0)
        return True
    elif(button == 'p'):
        controller.emit(uinput.BTN_TL, 1)
        time.sleep(.02)
        controller.emit(uinput.BTN_TL, 0)
        return True
    elif(button == 'j'):
        controller.emit(uinput.BTN_A, 1)
        time.sleep(.02)
        controller.emit(uinput.BTN_A, 0)
        return True
    elif(button == 'k'):
        controller.emit(uinput.BTN_B, 1)
        time.sleep(.02)
        controller.emit(uinput.BTN_B, 0)
        return True
    elif(button == 'l'):
        controller.emit(uinput.BTN_TR, 1)
        time.sleep(.02)
        controller.emit(uinput.BTN_TR, 0)
        return True
    elif(button == 't'):
        controller.emit(uinput.BTN_X, 1)
        controller.emit(uinput.BTN_Y, 1)
        time.sleep(.02)
        controller.emit(uinput.BTN_X, 0)
        controller.emit(uinput.BTN_Y, 0)
        return True
    elif(button == 'y'):
        controller.emit(uinput.BTN_A, 1)
        controller.emit(uinput.BTN_B, 1)
        time.sleep(.02)
        controller.emit(uinput.BTN_A, 0)
        controller.emit(uinput.BTN_B, 0)
        return True
    elif(button == '!'):
        controller.emit(uinput.BTN_SELECT, 1)
        time.sleep(.02)
        controller.emit(uinput.BTN_SELECT, 0)
        return True
    elif(button == '?'):
        controller.emit(uinput.BTN_START, 1)
        time.sleep(.02)
        controller.emit(uinput.BTN_START, 0)
        return True
    else:
        return False

def pressOn(button, controller):
    if(button == '4'):
        controller.emit(uinput.ABS_HAT0X, -1)
        return True
    elif(button == '6'):
        controller.emit(uinput.ABS_HAT0X, 1)
        return True
    
    elif(button == '5x'):
        controller.emit(uinput.ABS_HAT0X, 0)
        return True
    elif(button == '2'):
        controller.emit(uinput.ABS_HAT0Y, 1)
        return True
    elif(button == '8'):
        controller.emit(uinput.ABS_HAT0Y, -1)
        return True
    elif(button == '5y'):
        controller.emit(uinput.ABS_HAT0Y, 0)
        return True
    elif(button == 'q'):
        press('2', controller)
        press('6', controller)
        press('5y', controller)
        return True
    elif(button == 'b'):
        press('2', controller)
        press('6', controller)
        press('5y', controller)
        return True
    elif(button == 'h'):
        press('4', controller)
        press('2', controller)
        press('5x', controller)
        press('6', controller)
        press('5y', controller)
        return True
    elif(button == 'g'):
        press('6', controller)
        press('2', controller)
        press('5x', controller)
        press('4', controller)
        press('5y', controller)
        return True
    elif(button == 'w'):
        press('6', controller)
        press('2', controller)
        press('5x', controller)
        press('4', controller)
        press('5y', controller)
        press('8', controller)
        press('5x', controller)
        press('6', controller)
        press('5y', controller)
        return True
    elif(button == 'z'):
        press('6', controller)
        press('2', controller)
        press('5y', controller)
        return True
    elif(button == 's'):
        press('4', controller)
        press('2', controller)
        press('5y', controller)
        return True
    elif(button == 'i'):
        controller.emit(uinput.BTN_X, 1)
        return True
    elif(button == 'o'):
        controller.emit(uinput.BTN_Y, 1)
        return True
    elif(button == 'p'):
        controller.emit(uinput.BTN_TL, 1)
        return True
    elif(button == 'j'):
        controller.emit(uinput.BTN_A, 1)
        return True
    elif(button == 'k'):
        controller.emit(uinput.BTN_B, 1)
        return True
    elif(button == 'l'):
        controller.emit(uinput.BTN_TR, 1)
        return True
    elif(button == 't'):
        controller.emit(uinput.BTN_X, 1)
        controller.emit(uinput.BTN_Y, 1)
        return True
    elif(button == 'y'):
        controller.emit(uinput.BTN_A, 1)
        controller.emit(uinput.BTN_B, 1)
        return True
    else:
        return False

def pressOff(button, controller):
    if(button == 'i'):
        controller.emit(uinput.BTN_X, 0)
        return True
    elif(button == 'o'):
        controller.emit(uinput.BTN_Y, 0)
        return True
    elif(button == 'p'):
        controller.emit(uinput.BTN_TL, 0)
        return True
    elif(button == 'j'):
        controller.emit(uinput.BTN_A, 0)
        return True
    elif(button == 'k'):
        controller.emit(uinput.BTN_B, 0)
        return True
    elif(button == 'l'):
        controller.emit(uinput.BTN_TR, 0)
        return True
    elif(button == 't'):
        controller.emit(uinput.BTN_X, 0)
        controller.emit(uinput.BTN_Y, 0)
        return True
    elif(button == 'y'):
        controller.emit(uinput.BTN_A, 0)
        controller.emit(uinput.BTN_B, 0)
        return True
    else:
        return False

def waitPress(amount, button, controller):
    time.sleep(amount)
    press(button, controller)
    
def pressSequence( sequence, controller):
    for move in sequence:
        press(move,controller)
        time.sleep(.016)

def pressCombination( combination, controller):
    buttons = [ '4','8','2','6', 'i', 'o', 'p', 'j', 'k', 'l', 'q', 'b', 'h', 'g', 'w', 'z', 's']
    for i in range(len(combination)):
        if i < 2:
            if combination[0] and combination[1] < .8:
                pressOn('5x', controller)
        elif i < 4:
            if combination[1] and combination[2] < .8:
                pressOn('5y', controller)
        if combination[i] > .8:
            pressOn(buttons[i],controller)
    time.sleep(.02)
    for i in range(len(combination)):
        if combination[i] > .8:
            pressOff(buttons[i],controller)
