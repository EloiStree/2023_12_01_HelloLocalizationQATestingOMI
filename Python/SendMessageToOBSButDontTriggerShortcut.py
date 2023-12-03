import ctypes
import win32gui
import win32con
import time

def find_window_by_title_startswith(startswith):
    def callback(hwnd, hwnds):
        title = win32gui.GetWindowText(hwnd)
        if title.startswith(startswith):
            hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds

def send_key_combination(hwnd, *keys):
    for key in keys:
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
        time.sleep(0.1)  # Adjust sleep duration as needed
    for key in keys:
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)
        time.sleep(0.1)  # Adjust sleep duration as needed

def send_key_combinations_to_children(parent_hwnd, *combinations):
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and not win32gui.IsIconic(hwnd):
            print(f"Sending key combinations to visible child window with handle {hwnd}")
            for keys in combinations:
                print(f"Sending keys: {keys}")
                send_key_combination(hwnd, *keys)
                time.sleep(1)  # Adjust sleep duration as needed between combinations
        return True

    win32gui.EnumChildWindows(parent_hwnd, callback, None)

if __name__ == "__main__":
    # Specify the starting substring of the window title
    obs_startswith = 'OBS 29'

    # Find OBS windows whose title starts with the specified substring
    obs_windows = find_window_by_title_startswith(obs_startswith)

    if obs_windows:
        # Assuming you want to operate on the first found window
        obs_hwnd = obs_windows[0]

        # Send three different key combinations to visible child windows
        combinations = [
            (win32con.VK_CONTROL, win32con.VK_SHIFT, win32con.VK_MENU, ord('L')),
            (win32con.VK_CONTROL, win32con.VK_SHIFT, win32con.VK_MENU, ord('P')),
            (win32con.VK_CONTROL, win32con.VK_SHIFT, win32con.VK_MENU, ord('M'))
            # Add more combinations as needed
        ]
        send_key_combinations_to_children(obs_hwnd, *combinations)
    else:
        print("No OBS windows found with the specified title prefix.")
