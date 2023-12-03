import socket
import ctypes
import time

# Constants for SendMessage function
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101

# Virtual Key Codes
VK_CONTROL = 0x11
VK_R = 0x52
VK_ESCAPE = 0x1B

# Function to send keydown and keyup messages
def send_key(hwnd, key, key_down=True):
    lParam = 0
    if not key_down:
        lParam |= 0xC0000000  # keyup flag

    ctypes.windll.user32.PostMessageW(hwnd, WM_KEYDOWN if key_down else WM_KEYUP, key, lParam)

# Function to find the window handle by title
def find_window(title_start):
    hwnd = ctypes.windll.user32.FindWindowW(None, None)
    while hwnd:
        window_title = ctypes.create_unicode_buffer(512)
        ctypes.windll.user32.GetWindowTextW(hwnd, window_title, len(window_title))
        if window_title.value.startswith(title_start):
            return hwnd
        hwnd = ctypes.windll.user32.GetWindow(hwnd, ctypes.c_uint(2))  # GW_HWNDNEXT

    return None

# Function to start recording
def start_recording(window_title_start):
    hwnd = find_window(window_title_start)
    if hwnd:
        send_key(hwnd, VK_CONTROL)
        send_key(hwnd, VK_R)
        send_key(hwnd, VK_CONTROL, key_down=False)  # Release Ctrl key
    else:
        print(f"Window starting with title '{window_title_start}' not found.")

# Function to stop recording
def stop_recording(window_title_start):
    hwnd = find_window(window_title_start)
    if hwnd:
        send_key(hwnd, VK_ESCAPE)
    else:
        print(f"Window starting with title '{window_title_start}' not found.")

# Main function to listen for UDP messages and check every 10 seconds
def main():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5006

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    window_title_start = "Sound Recorder"

    print(f"Listening for UDP messages on port {UDP_PORT}...")

    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode('utf-8')

        if message == "Start":
            print("Received 'Start' command. Starting recording...")
            start_recording(window_title_start)
        elif message == "Stop":
            print("Received 'Stop' command. Stopping recording...")
            stop_recording(window_title_start)
        else:
            print(f"Received unknown command: {message}")

        time.sleep(0.1)  # Sleep for 10 seconds before checking again

if __name__ == "__main__":
    main()
