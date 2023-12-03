import pyautogui
import time

# Constants for virtual key codes
CTRL = 'ctrl'
SHIFT = 'shift'
ALT = 'alt'

LEFT_ARROW = 'left'
UP_ARROW = 'up'
RIGHT_ARROW = 'right'
DOWN_ARROW = 'down'

NUMPAD_0 = 'numpad0'
NUMPAD_1 = 'numpad1'
NUMPAD_2 = 'numpad2'
NUMPAD_3 = 'numpad3'
NUMPAD_4 = 'numpad4'
NUMPAD_5 = 'numpad5'
NUMPAD_6 = 'numpad6'
NUMPAD_7 = 'numpad7'
NUMPAD_8 = 'numpad8'
NUMPAD_9 = 'numpad9'

A = 'a'
B = 'b'
C = 'c'
D = 'd'
E = 'e'
F = 'f'
G = 'g'
H = 'h'
I = 'i'
J = 'j'
K = 'k'
L = 'l'
M = 'm'
N = 'n'
O = 'o'
P = 'p'
Q = 'q'
R = 'r'
S = 's'
T = 't'
U = 'u'
V = 'v'
W = 'w'
X = 'x'
Y = 'y'
Z = 'z'

NUMPAD_PLUS = 'numadd'
NUMPAD_MINUS = 'numsub'
NUMPAD_MULTIPLY = 'nummult'
NUMPAD_DIVIDE = 'numdiv'
NUMPAD_DECIMAL_POINT = 'numdecimal'

# Rest of the code...

def PressKey(key):
    pyautogui.keyDown(key)

def ReleaseKey(key):
    pyautogui.keyUp(key)

# Functions for pressing and releasing multiple keys
def PressKeyAll(keys):
    for key in keys:
        PressKey(key)

def ReleaseKeyAll(keys):
    for key in keys:
        ReleaseKey(key)

def PressAndReleaseKeysAll(keys, duration=0.1):
    PressKeyAll(keys)
    time.sleep(duration)
    ReleaseKeyAll(keys)





#----------------------------------------------------------

def INIT():
    print("Init")
    
p_left_trigger=False
p_left_right=False
def TRIGGER_LEFT(isPress):
    global p_left_trigger
    p = p_left_trigger
    p_left_trigger =isPress
    if p!=p_left_trigger:
        print("Button "+str(isPress) )
def TRIGGER_RIGHT(isPress):
    global p_left_right
    p = p_left_right
    p_left_right =isPress
    if p!=p_left_right:
        print("Button "+str(isPress) )
def LEFT_THUMB(isPress):
    print("Button "+str(isPress) )
def RIGHT_THUMB(isPress):
    print("Button "+str(isPress) )
def LEFT_SHOULDER(isPress):
    print("Button "+str(isPress) )
def RIGHT_SHOULDER(isPress):
    print("Button "+str(isPress) )
def BACK(isPress):
    print("Button "+str(isPress) )
def START(isPress):
    print("Button "+str(isPress) )
def DPAD_LEFT(isPress):
    print("Button "+str(isPress) )
def DPAD_RIGHT(isPress):
    print("Button "+str(isPress) )
def DPAD_UP(isPress):
    print("Button "+str(isPress) )
def DPAD_DOWN(isPress):
    print("Button "+str(isPress) )

# NUMPAD_PLUS = 'numadd'
# NUMPAD_MINUS = 'numsub'
# NUMPAD_MULTIPLY = 'nummult'
# NUMPAD_DIVIDE = 'numdiv'
# NUMPAD_DECIMAL_POINT = 'numdecimal'
    
def A(isPress):
    print("Button A  "+str(isPress) )
#    PressAndReleaseKeysAll([NUMPAD_PLUS],0.2)

    pyautogui.keyDown(NUMPAD_PLUS)
    pyautogui.keyUp(NUMPAD_PLUS)
   
def B(isPress):
    print("Button B "+str(isPress) )
    PressAndReleaseKeysAll([NUMPAD_MINUS],0.2)    

def Y(isPress):
    print("Button Y "+str(isPress) )
    PressAndReleaseKeysAll([NUMPAD_MULTIPLY],0.2)
    
def X(isPress):
    print("Button X "+str(isPress) )
    PressAndReleaseKeysAll([NUMPAD_DIVIDE],0.2)

#CTRL = 0x11
#SHIFT = 0x10
#ALT = 0x12

#LEFT_ARROW = 0x25
#UP_ARROW = 0x26
#RIGHT_ARROW = 0x27
#DOWN_ARROW = 0x28
    
