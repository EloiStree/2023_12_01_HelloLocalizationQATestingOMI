import ctypes
import time
import psutil
import pygetwindow as gw

# Define constants for key codes
VK_SHIFT = 0x10
VK_CONTROL = 0x11
VK_MENU = 0x12
VK_P = 0x50
VK_M = 0x4D
VK_L = 0x4C

def find_obs_process():
    obs_processes = []

    for process in psutil.process_iter(['pid', 'name']):
        if 'obs' in process.info['name'].lower():
            obs_processes.append(process.info)

    return obs_processes

def center_obs_window(pid):
    try:
        obs_window = gw.getWindowsWithTitle("OBS 29.1.3")[0]
        obs_window.activate()
        obs_window.maximize()
        
        # Get screen dimensions
        screen_rect = gw.getScreenRect()
        screen_width = screen_rect.width
        screen_height = screen_rect.height
        
        # Calculate center coordinates
        center_x = (screen_width - obs_window.width) // 2
        center_y = (screen_height - obs_window.height) // 2
        
        # Move the window to the center
        obs_window.moveTo(center_x, center_y)
        
        print(f"OBS process with PID {pid} brought to the foreground, maximized, and centered.")
        
        # Send key combinations
        send_key_combination(obs_window)
        
    except IndexError:
        print("No OBS window found with title 'OBS 29.1.3'.")

def send_key_combination(obs_window):
    # Add a 5-second delay at the start
    time.sleep(5)
    
    # Send the key combinations and release the keys
    send_key(obs_window, [VK_SHIFT, VK_CONTROL, VK_MENU, VK_P])  # Shift+Control+Alt+P
    time.sleep(5)  # Add a 5-second delay between key combinations
    send_key(obs_window, [VK_SHIFT, VK_CONTROL, VK_MENU, VK_M])  # Shift+Control+Alt+M
    time.sleep(5)  # Add a 5-second delay between key combinations
    send_key(obs_window, [VK_SHIFT, VK_CONTROL, VK_MENU, VK_L])  # Shift+Control+Alt+L
    send_key(obs_window, [ VK_P])  # Shift+Control+Alt+P
    time.sleep(5)  # Add a 5-second delay between key combinations
    send_key(obs_window, [ VK_M])  # Shift+Control+Alt+M
    time.sleep(5)  # Add a 5-second delay between key combinations
    send_key(obs_window, [ VK_L])  # Shift+Control+Alt+L

def send_key(obs_window, keys):
    for key in keys:
        ctypes.windll.user32.PostMessageW(obs_window._hWnd, 0x100, key, 0)  # WM_KEYDOWN
        time.sleep(0.1)  # Add a short delay between key presses

    for key in keys:
        ctypes.windll.user32.PostMessageW(obs_window._hWnd, 0x101, key, 0)  # WM_KEYUP
        time.sleep(0.1)  # Add a short delay between key releases

if __name__ == "__main__":
    obs_processes = find_obs_process()

    if obs_processes:
        print("OBS processes found:")
        for process in obs_processes:
            print(f"PID: {process['pid']}, Name: {process['name']}")
            center_obs_window(process['pid'])
    else:
        print("No OBS processes found.")
