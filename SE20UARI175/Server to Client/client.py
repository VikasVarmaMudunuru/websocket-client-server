import asyncio
import websockets

async def receive_message():
    async with websockets.connect("ws://139.59.33.235:3000") as websocket:
        message = await websocket.recv()
        print(f"Recived message from server: {message}")

asyncio.get_event_loop().run_until_complete(receive_message())

