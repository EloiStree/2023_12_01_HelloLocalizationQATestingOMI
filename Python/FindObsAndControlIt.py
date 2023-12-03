import ctypes
import time
import psutil

# Define constants for key codes
VK_SHIFT = 0x10
VK_CONTROL = 0x11
VK_MENU = 0x12
VK_P = 0x50
VK_M = 0x4D
VK_L = 0x4C

# Function to check if a process name contains "OBS" (case-insensitive)
def is_obs_process(process):
    return "OBS" in process.info['name'].upper()

# Function to send the key combination to the specified window
def send_key_combination(hwnd, keys):
    for key in keys:
        ctypes.windll.user32.PostMessageW(hwnd, 0x100, key, 0)  # WM_KEYDOWN
        time.sleep(0.1)  # Add a short delay between key presses

    for key in keys:
        ctypes.windll.user32.PostMessageW(hwnd, 0x101, key, 0)  # WM_KEYUP
        time.sleep(0.1)  # Add a short delay between key releases

# Main script
for process in psutil.process_iter(['pid', 'name']):
    if is_obs_process(process):
        # Get the process handle
        process_handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, process.info['pid'])

        # Get the window handle (hwnd) of the process
        hwnd = ctypes.windll.user32.GetForegroundWindow()

        # Bring the OBS window to the foreground
        ctypes.windll.user32.ShowWindow(hwnd, 9)  # SW_RESTORE
        ctypes.windll.user32.SetForegroundWindow(hwnd)

        # Add a 5-second delay at the start
        time.sleep(5)

        # Send the key combinations and release the keys
        send_key_combination(hwnd, [VK_SHIFT, VK_CONTROL, VK_MENU, VK_P])  # Shift+Control+Alt+P
        time.sleep(5)  # Add a 5-second delay between key combinations
        send_key_combination(hwnd, [VK_SHIFT, VK_CONTROL, VK_MENU, VK_M])  # Shift+Control+Alt+M
        time.sleep(5)  # Add a 5-second delay between key combinations
        send_key_combination(hwnd, [VK_SHIFT, VK_CONTROL, VK_MENU, VK_L])  # Shift+Control+Alt+L

        # Close the process handle
        ctypes.windll.kernel32.CloseHandle(process_handle)
