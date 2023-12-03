import ctypes
import psutil

# Constants
WM_SYSCOMMAND = 0x0112
SC_MAXIMIZE = 0xF030
SC_RESTORE = 0xF120

# Function to find and maximize the window of a process by name or non-empty title
def maximize_window_by_name(name_or_title):
    print("List of processes and their titles:")
    for process in psutil.process_iter(['pid', 'name']):
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}")
        hwnd = ctypes.windll.user32.FindWindowW(None, None)
        while hwnd:
            window_title = ctypes.create_unicode_buffer(256)
            ctypes.windll.user32.GetWindowTextW(hwnd, window_title, 255)
            
            # Trim and check if the title is not empty
            trimmed_title = window_title.value.strip()
            if trimmed_title:
                print(f"  Window Title: {trimmed_title}")
                
                if trimmed_title.lower() == name_or_title.lower():
                    # Maximize the window
                    ctypes.windll.user32.ShowWindow(hwnd, SC_MAXIMIZE)
                    # Bring the window to the foreground
                    ctypes.windll.user32.SetForegroundWindow(hwnd)

                    # If you want to restore the window instead of maximizing, use the following line:
                    # ctypes.windll.user32.ShowWindow(hwnd, SC_RESTORE)

                    # Find and maximize all child windows
                    EnumWindows = ctypes.windll.user32.EnumWindows
                    EnumChildWindows = ctypes.windll.user32.EnumChildWindows

                    def callback(hwnd, lParam):
                        ctypes.windll.user32.ShowWindow(hwnd, SC_MAXIMIZE)
                        return True

                    EnumWindows(callback, 0)
                    EnumChildWindows(hwnd, callback, 0)

                    return True

            hwnd = ctypes.windll.user32.FindWindowExW(None, hwnd, None, None)

    return False

# Example usage: Maximize windows of processes or titles starting with "Sound"
name_or_title_to_find = "Sound"
if not maximize_window_by_name(name_or_title_to_find):
    print(f"No process or window found with name or non-empty title '{name_or_title_to_find}'")
