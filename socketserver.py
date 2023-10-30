import asyncio
import websockets
import random

async def echo(websocket, path):
    async for message in websocket:
        print("Received:", message)
        random_number = random.randint(1, 100)
        response = f"{message} {random_number}"
        await websocket.send(response)
        print("Sent:", response)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
