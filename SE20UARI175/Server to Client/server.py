import asyncio
import websockets

async def send_message(websocket, path):
    message = "I am 4th Year B.Tech Student at Mahindra University"
    await websocket.send(message)
    print("Message sent to client")

start_server = websockets.serve(send_message, "139.59.33.235", 3000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()