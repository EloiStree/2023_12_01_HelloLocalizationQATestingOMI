import socket
import pygetwindow as gw
import threading
import keyboard  # You may need to install it using: pip install keyboard
import time

def get_window_by_title(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        return window
    except IndexError:
        print(f"Window with title '{window_title}' not found.")
        return None

def focus_window_by_title(window_title):
    window = get_window_by_title(window_title)
    if window:
        window.activate()

def udp_listener():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5006

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    try:
        print("Listening for UDP messages...")
        while True:
            data, addr = sock.recvfrom(1024)
            message = data.decode("utf-8")
            print(f"Received message: {message}")
            window_title = message
            focus_window_by_title(window_title)

    except KeyboardInterrupt:
        print("UDP listener terminated by user.")
    finally:
        sock.close()

def main():
    # Start the UDP listener on a separate thread
    udp_thread = threading.Thread(target=udp_listener)
    udp_thread.daemon = True
    udp_thread.start()

    try:
        # Main thread for debugging with 'Y' key
        while True:
            if keyboard.is_pressed('Y'):
                window_title = ("Sound Recorder")
                focus_window_by_title(window_title)
                
            if keyboard.is_pressed('T'):
                window_title = ("WhatApps")
                focus_window_by_title(window_title)
                
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Main thread terminated by user.")
    finally:
        udp_thread.join()

if __name__ == "__main__":
    main()
