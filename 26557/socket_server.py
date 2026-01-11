import websockets, asyncio, json


clients = set()


async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            print(json.loads(message))
    finally:
        clients.remove(websocket)


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever
        
        
asyncio.run(main())