# directkeys.py
# http://stackoverflow.com/questions/13564851/generate-keyboard-events
# msdn.microsoft.com/en-us/library/dd375731
## SOURCE https://gist.github.com/Aniruddha-Tapas/1627257344780e5429b10bc92eb2f52a
import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)


# Import statements and other code...

# Constants for virtual key codes
CTRL = 0x11
SHIFT = 0x10
ALT = 0x12

LEFT_ARROW = 0x25
UP_ARROW = 0x26
RIGHT_ARROW = 0x27
DOWN_ARROW = 0x28

NUMPAD_0 = 0x60
NUMPAD_1 = 0x61
NUMPAD_2 = 0x62
NUMPAD_3 = 0x63
NUMPAD_4 = 0x64
NUMPAD_5 = 0x65
NUMPAD_6 = 0x66
NUMPAD_7 = 0x67
NUMPAD_8 = 0x68
NUMPAD_9 = 0x69

A = 0x41
B = 0x42
C = 0x43
D = 0x44
E = 0x45
F = 0x46
G = 0x47
H = 0x48
I = 0x49
J = 0x4A
K = 0x4B
L = 0x4C
M = 0x4D
N = 0x4E
O = 0x4F
P = 0x50
Q = 0x51
R = 0x52
S = 0x53
T = 0x54
U = 0x55
V = 0x56
W = 0x57
X = 0x58
Y = 0x59
Z = 0x5A

# Alphanumeric keys 0 to 9
NUM_0 = 0x30
NUM_1 = 0x31
NUM_2 = 0x32
NUM_3 = 0x33
NUM_4 = 0x34
NUM_5 = 0x35
NUM_6 = 0x36
NUM_7 = 0x37
NUM_8 = 0x38
NUM_9 = 0x39

# Additional keys
WINDOW = 0x5B  # Windows key
SPACE = 0x20   # Spacebar

# Rest of the script...



INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# List of all codes for keys:
# # msdn.microsoft.com/en-us/library/dd375731
UP = 0x26
DOWN = 0x28
A = 0x41
VK1 = 0x31
VK2 = 0x32

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


# Functions for pressing and releasing multiple keys
def PressKeyAll(hexKeyCodes):
    for hexKeyCode in hexKeyCodes:
        PressKey(hexKeyCode)

def ReleaseKeyAll(hexKeyCodes):
    for hexKeyCode in hexKeyCodes:
        ReleaseKey(hexKeyCode)

def PressAndReleaseKeysAll(hexKeyCodes, duration=0.1):
    PressKeyAll(hexKeyCodes)
    time.sleep(duration)
    ReleaseKeyAll(hexKeyCodes)



if __name__ == "__main__":
    while True:
        PressKey(VK1)
        time.sleep(1)
        ReleaseKey(VK1)
        time.sleep(1)
        PressKey(VK2)
        time.sleep(1)
        ReleaseKey(VK2)
        print("Pressed")
        PressKey(0x67)
        time.sleep(1)
        ReleaseKey(0x67)
        time.sleep(1)
        PressKey(0x69)
        time.sleep(1)
        ReleaseKey(0x69)
        print("Pressed")



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
def A(isPress):
    print("Button A  "+str(isPress) )
    PressAndReleaseKeysAll([CTRL, SHIFT, ALT, LEFT_ARROW])

    
def B(isPress):
    print("Button B "+str(isPress) )
    PressAndReleaseKeysAll([CTRL, SHIFT, ALT, RIGHT_ARROW])
    
def Y(isPress):
    print("Button Y "+str(isPress) )
    PressAndReleaseKeysAll([CTRL, SHIFT, ALT, UP_ARROW])
    
def X(isPress):
    print("Button X "+str(isPress) )
    PressAndReleaseKeysAll([0x41,0x42])


#CTRL = 0x11
#SHIFT = 0x10
#ALT = 0x12

#LEFT_ARROW = 0x25
#UP_ARROW = 0x26
#RIGHT_ARROW = 0x27
#DOWN_ARROW = 0x28
    
