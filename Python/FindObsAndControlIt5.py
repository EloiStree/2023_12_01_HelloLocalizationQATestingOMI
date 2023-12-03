import asyncio
import websockets
import json

async def send_message(websocket, message):
    await websocket.send(json.dumps(message))
    print(f"Sent message: {message}")

async def main():
    # Connection details
    host = "localhost"
    port = 4455
    password = "wLYFuuNgO5ielczz"

    # WebSocket URL
    url = f"ws://{host}:{port}/"

    # Connect to OBS WebSocket server
    async with websockets.connect(url) as websocket:
        # Authenticate with the provided password
        auth_message = {
            "request-type": "SetPassword",
            "messsage-id":"1",
            "password": password
        }
        await send_message(websocket, auth_message)

        # Start recording
        start_recording_message = {
            "request-type": "StartRecording",
            "messsage-id":"1"

        }
        await send_message(websocket, start_recording_message)

        # Wait for a few seconds (you can adjust this delay)
        await asyncio.sleep(5)

        # Stop recording
        stop_recording_message = {
            "request-type": "StopRecording",
            "messsage-id":"1"
        }
        await send_message(websocket, stop_recording_message)

        # Take a screenshot (replace "your_source_name" with the actual source name)
        take_screenshot_message = {
            "request-type": "TakeSourceScreenshot",
            "message-id": "unique_id",
            "sourceName": "",
            "embedPictureFormat": "png"
        }
        await send_message(websocket, take_screenshot_message)

if __name__ == "__main__":
    asyncio.run(main())
