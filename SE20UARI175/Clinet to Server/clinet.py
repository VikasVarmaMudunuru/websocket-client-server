import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://139.59.33.235:1500") as websocket:
        message = "Hi, I am Vikas Varma"
        await websocket.send(message)
        print("Message sent to server")

asyncio.get_event_loop().run_until_complete(send_message())

