import asyncio
import websockets
import json

with open('websocket.json', 'r') as f:
    websocket_data = json.load(f)

connected_clients = set()

async def echo(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the message to all connected clients
            tasks = [asyncio.create_task(client.send(message)) for client in connected_clients]
            await asyncio.gather(*tasks)
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(echo, websocket_data['host'], websocket_data['port'], ping_interval=20, ping_timeout=20):
        print(f"WebSocket server started on ws://{websocket_data['host']}:{websocket_data['port']}")
        await asyncio.Future() # Run forever

if __name__ == "__main__":
    asyncio.run(main())