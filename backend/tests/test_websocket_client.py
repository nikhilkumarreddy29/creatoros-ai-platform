import asyncio
import websockets


async def test_live_feed():
    uri = "ws://127.0.0.1:8000/stream/live-feed"

    async with websockets.connect(uri) as websocket:
        for _ in range(3):
            message = await websocket.recv()
            print(message)


asyncio.run(test_live_feed())