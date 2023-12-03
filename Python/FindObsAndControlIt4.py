from obswebsocket import obsws, requests
import time

# Connect to OBS WebSocket server
host = "localhost"
port = 4545
password = "HelloWorld"  # Set the password you configured in OBS WebSocket settings

ws = obsws(host, port, password)
ws.connect()

time.sleep(5)

# Start recording
response_start_recording = ws.call(requests.StartRecording())
print(f"Start Recording Response: {response_start_recording}")

time.sleep(5)

# Stop recording
response_stop_recording = ws.call(requests.StopRecording())
print(f"Stop Recording Response: {response_stop_recording}")

# Take screenshot of the entire scene (final composited image)
file_path = "screenshot.png"
response_take_screenshot = ws.call(requests.TakeScreenshot(saveToFilePath=file_path))
print(f"Take Screenshot Response: {response_take_screenshot}")

# Disconnect from OBS WebSocket server
ws.disconnect()
