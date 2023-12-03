from XInput import *

import ctypes
import pyvjoy
import pyautogui
import time
from nearactions import *



try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


INIT()


# What force does trigger of the Xbox need to be used to go forward
trigger_sensibility=0.05



root = tk.Tk()
root.title("XInput")
canvas = tk.Canvas(root, width= 600, height = 400, bg="white")
canvas.pack()

set_deadzone(DEADZONE_TRIGGER,10)

hide_cursor=False


def switch_mouse_hide():
    global hide_cursor
    hide_cursor = not hide_cursor
    ctypes.windll.user32.ShowCursor(not hide_cursor)


class Controller:
    def __init__(self, center):
        self.center = center

        self.on_indicator_pos = (self.center[0], self.center[1] - 50)

        self.on_indicator = canvas.create_oval(((self.on_indicator_pos[0] - 10, self.on_indicator_pos[1] - 10), (self.on_indicator_pos[0] + 10, self.on_indicator_pos[1] + 10)))
        
        self.r_thumb_pos = (self.center[0] + 50, self.center[1] + 20)

        r_thumb_outline = canvas.create_oval(((self.r_thumb_pos[0] - 25, self.r_thumb_pos[1] - 25), (self.r_thumb_pos[0] + 25, self.r_thumb_pos[1] + 25)))

        r_thumb_stick_pos = self.r_thumb_pos

        self.r_thumb_stick = canvas.create_oval(((r_thumb_stick_pos[0] - 10, r_thumb_stick_pos[1] - 10), (r_thumb_stick_pos[0] + 10, r_thumb_stick_pos[1] + 10)))

        self.l_thumb_pos = (self.center[0] - 100, self.center[1] - 20)

        l_thumb_outline = canvas.create_oval(((self.l_thumb_pos[0] - 25, self.l_thumb_pos[1] - 25), (self.l_thumb_pos[0] + 25, self.l_thumb_pos[1] + 25)))

        l_thumb_stick_pos = self.l_thumb_pos

        self.l_thumb_stick = canvas.create_oval(((l_thumb_stick_pos[0] - 10, l_thumb_stick_pos[1] - 10), (l_thumb_stick_pos[0] + 10, l_thumb_stick_pos[1] + 10)))

        self.l_trigger_pos = (self.center[0] - 120, self.center[1] - 70)

        l_trigger_outline = canvas.create_rectangle(((self.l_trigger_pos[0] - 5, self.l_trigger_pos[1] - 20), (self.l_trigger_pos[0] + 5, self.l_trigger_pos[1] + 20)))

        l_trigger_index_pos = (self.l_trigger_pos[0], self.l_trigger_pos[1] - 20)

        self.l_trigger_index = canvas.create_rectangle(((l_trigger_index_pos[0] - 10, l_trigger_index_pos[1] - 5), (l_trigger_index_pos[0] + 10, l_trigger_index_pos[1] + 5)))

        self.r_trigger_pos = (self.center[0] + 120, self.center[1] - 70)

        r_trigger_outline = canvas.create_rectangle(((self.r_trigger_pos[0] - 5, self.r_trigger_pos[1] - 20), (self.r_trigger_pos[0] + 5, self.r_trigger_pos[1] + 20)))

        r_trigger_index_pos = (self.r_trigger_pos[0], self.r_trigger_pos[1] - 20)

        self.r_trigger_index = canvas.create_rectangle(((r_trigger_index_pos[0] - 10, r_trigger_index_pos[1] - 5), (r_trigger_index_pos[0] + 10, r_trigger_index_pos[1] + 5)))

        buttons_pos = (self.center[0] + 100, self.center[1] - 20)

        A_button_pos = (buttons_pos[0], buttons_pos[1] + 20)

        B_button_pos = (buttons_pos[0] + 20, buttons_pos[1])

        Y_button_pos = (buttons_pos[0], buttons_pos[1] - 20)

        X_button_pos = (buttons_pos[0] - 20, buttons_pos[1])

        self.A_button = canvas.create_oval(((A_button_pos[0] - 10, A_button_pos[1] - 10), (A_button_pos[0] + 10, A_button_pos[1] + 10)))

        self.B_button = canvas.create_oval(((B_button_pos[0] - 10, B_button_pos[1] - 10), (B_button_pos[0] + 10, B_button_pos[1] + 10)))

        self.Y_button = canvas.create_oval(((Y_button_pos[0] - 10, Y_button_pos[1] - 10), (Y_button_pos[0] + 10, Y_button_pos[1] + 10)))

        self.X_button = canvas.create_oval(((X_button_pos[0] - 10, X_button_pos[1] - 10), (X_button_pos[0] + 10, X_button_pos[1] + 10)))

        dpad_pos = (self.center[0] - 50, self.center[1] + 20)

        self.dpad_left = canvas.create_rectangle(((dpad_pos[0] - 30, dpad_pos[1] - 10), (dpad_pos[0] - 10, dpad_pos[1] + 10)), outline = "")

        self.dpad_up = canvas.create_rectangle(((dpad_pos[0] - 10, dpad_pos[1] - 30), (dpad_pos[0] + 10, dpad_pos[1] - 10)), outline = "")

        self.dpad_right = canvas.create_rectangle(((dpad_pos[0] + 10, dpad_pos[1] - 10), (dpad_pos[0] + 30, dpad_pos[1] + 10)), outline = "")

        self.dpad_down = canvas.create_rectangle(((dpad_pos[0] - 10, dpad_pos[1] + 10), (dpad_pos[0] + 10, dpad_pos[1] + 30)), outline = "")

        dpad_outline = canvas.create_polygon(((dpad_pos[0] - 30, dpad_pos[1] - 10), (dpad_pos[0] - 10, dpad_pos[1] - 10), (dpad_pos[0] - 10, dpad_pos[1] - 30), (dpad_pos[0] + 10, dpad_pos[1] - 30),
                                              (dpad_pos[0] + 10, dpad_pos[1] - 10), (dpad_pos[0] + 30, dpad_pos[1] - 10), (dpad_pos[0] + 30, dpad_pos[1] + 10), (dpad_pos[0] + 10, dpad_pos[1] + 10),
                                              (dpad_pos[0] + 10, dpad_pos[1] + 30), (dpad_pos[0] - 10, dpad_pos[1] + 30), (dpad_pos[0] - 10, dpad_pos[1] + 10), (dpad_pos[0] - 30, dpad_pos[1] + 10)),
                                             fill = "", outline = "black")

        back_button_pos = (self.center[0] - 20, self.center[1] - 20)

        self.back_button = canvas.create_oval(((back_button_pos[0] - 5, back_button_pos[1] - 5), (back_button_pos[0] + 5, back_button_pos[1] + 5)))

        start_button_pos = (self.center[0] + 20, self.center[1] - 20)

        self.start_button = canvas.create_oval(((start_button_pos[0] - 5, start_button_pos[1] - 5), (start_button_pos[0] + 5, start_button_pos[1] + 5)))

        l_shoulder_pos = (self.center[0] - 90, self.center[1] - 70)

        self.l_shoulder = canvas.create_rectangle(((l_shoulder_pos[0] - 20, l_shoulder_pos[1] - 5), (l_shoulder_pos[0] + 20, l_shoulder_pos[1] + 10)))

        r_shoulder_pos = (self.center[0] + 90, self.center[1] - 70)

        self.r_shoulder = canvas.create_rectangle(((r_shoulder_pos[0] - 20, r_shoulder_pos[1] - 10), (r_shoulder_pos[0] + 20, r_shoulder_pos[1] + 5)))

controllers = (Controller((150., 100.)),
               Controller((450., 100.)),
               Controller((150., 300.)),
               Controller((450., 300.)))

vjoy_device_id = 2  
joystick = pyvjoy.VJoyDevice(vjoy_device_id)



# ACTION TO DO IN GAME START ############


    
def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)
while 1:
    events = get_events()
    for event in events:
        controller = controllers[event.user_index]
        if event.type == EVENT_CONNECTED:
            canvas.itemconfig(controller.on_indicator, fill="light green")
            
        elif event.type == EVENT_DISCONNECTED:
            canvas.itemconfig(controller.on_indicator, fill="")
            
        elif event.type == EVENT_STICK_MOVED:
            if event.stick == LEFT:
                l_thumb_stick_pos = (int(round(controller.l_thumb_pos[0] + 25 * event.x,0)), int(round(controller.l_thumb_pos[1] - 25 * event.y,0)))
                canvas.coords(controller.l_thumb_stick, (l_thumb_stick_pos[0] - 10, l_thumb_stick_pos[1] - 10, l_thumb_stick_pos[0] + 10, l_thumb_stick_pos[1] + 10))

                
            elif event.stick == RIGHT:
                r_thumb_stick_pos = (int(round(controller.r_thumb_pos[0] + 25 * event.x,0)), int(round(controller.r_thumb_pos[1] - 25 * event.y,0)))
                canvas.coords(controller.r_thumb_stick, (r_thumb_stick_pos[0] - 10, r_thumb_stick_pos[1] - 10, r_thumb_stick_pos[0] + 10, r_thumb_stick_pos[1] + 10))
                

        elif event.type == EVENT_TRIGGER_MOVED:
            if event.trigger == LEFT:
                l_trigger_index_pos = (controller.l_trigger_pos[0], controller.l_trigger_pos[1] - 20 + int(round(40 * event.value, 0)))
                canvas.coords(controller.l_trigger_index, (l_trigger_index_pos[0] - 10, l_trigger_index_pos[1] - 5, l_trigger_index_pos[0] + 10, l_trigger_index_pos[1] + 5))
                print(f"JOYSTICK LEFT : {event.value}")
                if event.value>trigger_sensibility:
                    TRIGGER_LEFT(True)
                else:
                    TRIGGER_LEFT(False)
                
            elif event.trigger == RIGHT:
                r_trigger_index_pos = (controller.r_trigger_pos[0], controller.r_trigger_pos[1] - 20 + int(round(40 * event.value, 0)))
                canvas.coords(controller.r_trigger_index, (r_trigger_index_pos[0] - 10, r_trigger_index_pos[1] - 5, r_trigger_index_pos[0] + 10, r_trigger_index_pos[1] + 5))
                print(f"JOYSTICK Right : {event.value}")
                if event.value>trigger_sensibility:
                    TRIGGER_RIGHT(True)
                else:
                    TRIGGER_RIGHT(False)
               

        elif event.type == EVENT_BUTTON_PRESSED:
            if event.button == "LEFT_THUMB":
                canvas.itemconfig(controller.l_thumb_stick, fill="red")
                LEFT_THUMB(True)
            elif event.button == "RIGHT_THUMB":
                canvas.itemconfig(controller.r_thumb_stick, fill="red")
                RIGHT_THUMB(True)
            elif event.button == "LEFT_SHOULDER":
                canvas.itemconfig(controller.l_shoulder, fill="red")
                LEFT_SHOULDER(True)
            elif event.button == "RIGHT_SHOULDER":
                canvas.itemconfig(controller.r_shoulder, fill="red")
                RIGHT_SHOULDER(True)
 

            elif event.button == "BACK":
                canvas.itemconfig(controller.back_button, fill="red")
                BACK(True)
                
            elif event.button == "START":
                canvas.itemconfig(controller.start_button, fill="red")
                START(True)

            elif event.button == "DPAD_LEFT":
                canvas.itemconfig(controller.dpad_left, fill="red")
                DPAD_LEFT(True)
                #pyautogui.keyDown(NUMPAD_PLUS)
                #pyautogui.keyUp(NUMPAD_PLUS)
    

            elif event.button == "DPAD_RIGHT":
                canvas.itemconfig(controller.dpad_right, fill="red")
                DPAD_RIGHT(True)
            elif event.button == "DPAD_UP":
                canvas.itemconfig(controller.dpad_up, fill="red")
                DPAD_UP(True)
            elif event.button == "DPAD_DOWN":
                canvas.itemconfig(controller.dpad_down, fill="red")
                DPAD_DOWN(True)

            elif event.button == "A":
                canvas.itemconfig(controller.A_button, fill="red")
                A(True)
                
            elif event.button == "B":
                canvas.itemconfig(controller.B_button, fill="red")
                B(True)

                
            elif event.button == "Y":
                canvas.itemconfig(controller.Y_button, fill="red")
                Y(True)
                
            elif event.button == "X":
                canvas.itemconfig(controller.X_button, fill="red")
                X(True)
                

        elif event.type == EVENT_BUTTON_RELEASED:
            if event.button == "LEFT_THUMB":
                canvas.itemconfig(controller.l_thumb_stick, fill="")
                LEFT_THUMB(False)
                
            elif event.button == "RIGHT_THUMB":
                canvas.itemconfig(controller.r_thumb_stick, fill="")
                RIGHT_THUMB(False)

            elif event.button == "LEFT_SHOULDER":
                canvas.itemconfig(controller.l_shoulder, fill="")
                LEFT_SHOULDER(False)
                
            elif event.button == "RIGHT_SHOULDER":
                canvas.itemconfig(controller.r_shoulder, fill="")
                RIGHT_SHOULDER(False)

            elif event.button == "BACK":
                canvas.itemconfig(controller.back_button, fill="")
                BACK(False)
                
            elif event.button == "START":
                canvas.itemconfig(controller.start_button, fill="")
                START(False)

            elif event.button == "DPAD_LEFT":
                canvas.itemconfig(controller.dpad_left, fill="")
                DPAD_LEFT(False)
                
            elif event.button == "DPAD_RIGHT":
                canvas.itemconfig(controller.dpad_right, fill="")
                DPAD_RIGHT(False)
                
            elif event.button == "DPAD_UP":
                canvas.itemconfig(controller.dpad_up, fill="")
                DPAD_UP(False)
                
            elif event.button == "DPAD_DOWN":
                canvas.itemconfig(controller.dpad_down, fill="")
                DPAD_DOWN(False)

            elif event.button == "A":
                canvas.itemconfig(controller.A_button, fill="")
                A(False)

            elif event.button == "B":
                canvas.itemconfig(controller.B_button, fill="")
                B(False)

            elif event.button == "Y":
                canvas.itemconfig(controller.Y_button, fill="")
                Y(False)
                
                
            elif event.button == "X":
                canvas.itemconfig(controller.X_button, fill="")
                X(False)


    try:          
        root.update()
    except tk.TclError:
        break

