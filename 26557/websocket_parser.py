import websockets, asyncio, requests, json


async def send_and_recive():
    count = 0
    # async for websocket  in  websockets.connect('wss://r3558nlk-8765.euw.devtunnels.ms/'):
    async with websockets.connect('wss://r3558nlk-8765.euw.devtunnels.ms/') as websocket:
        try:
            # await websocket.send(json.dumps({"type": "ывапвылаывилвы ваывышлварываыв авылприывлываиывла"}))
            response = await websocket.recv()
            print(f"Получено: {response}")
            count += 1
        except websockets.ConnectionClosed as e:
            print(e)
        if count == 5:
            pass
    
async def main():
    await send_and_recive()    

if __name__ == '__main__':
    asyncio.run(main())