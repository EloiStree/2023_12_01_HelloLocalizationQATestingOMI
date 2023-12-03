import ctypes
import win32gui
import win32con
import time

def find_window(title):
    hwnd = win32gui.FindWindow(None, title)
    return hwnd

def set_foreground_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)

def send_alt_key(hwnd, key):
    try:
        # Send Alt key down
        win32gui.SendMessage(hwnd, win32con.WM_SYSKEYDOWN, win32con.VK_MENU, 0)
        time.sleep(0.1)  # Adjust the delay if needed

        # Send specified key down
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
        time.sleep(0.1)  # Adjust the delay if needed

        # Send specified key up
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)
        time.sleep(0.1)  # Adjust the delay if needed

        # Send Alt key up
        win32gui.SendMessage(hwnd, win32con.WM_SYSKEYUP, win32con.VK_MENU, 0)
        time.sleep(0.1)  # Adjust the delay if needed

    except Exception as e:
        print(f"Exception occurred while sending Alt+Key: {e}")

def send_message_to_children(hwnd, message, w_param, l_param):
    try:
        child_windows = []
        win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd), child_windows)
        
        for child_hwnd in child_windows:
            win32gui.SendMessage(child_hwnd, message, w_param, l_param)
            time.sleep(0.1)  # Adjust the delay if needed

    except Exception as e:
        print(f"Exception occurred while sending message to children: {e}")

if __name__ == "__main__":
    window_title = "Sound Recorder"  # Change this to your desired window title or prefix

    hwnd = find_window(window_title)

    if hwnd:
        set_foreground_window(hwnd)
        
        # Wait for 5 seconds
        time.sleep(5)
        
        send_alt_key(hwnd, win32con.VK_R)  # Sending Alt+R key combination to the main window
        time.sleep(1)  # Adjust the delay if needed
        send_alt_key(hwnd, win32con.VK_S)  # Sending Alt+S key combination to the main window
        
        send_message_to_children(hwnd, win32con.WM_KEYDOWN, win32con.VK_A, 0)  # Sending WM_KEYDOWN message to all children with 'A' key
        print(f"Sent Alt+R, Alt+S, and WM_KEYDOWN to window with title: {window_title}")
    else:
        print(f"Window with title '{window_title}' not found")
