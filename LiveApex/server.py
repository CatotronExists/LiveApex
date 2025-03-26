import asyncio
import sys
import websockets

connected_clients = set()

async def echo(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the message to all connected clients
            tasks = [asyncio.create_task(client.send(message)) for client in connected_clients]
            await asyncio.gather(*tasks)
    
    except websockets.exceptions.ConnectionClosedOK:
        pass

    finally:
        connected_clients.remove(websocket)

async def main():
    try:
        websocket_data = sys.argv[1].split(",")
        async with websockets.serve(echo, websocket_data[0], websocket_data[1], ping_interval=20, ping_timeout=20):
            print(f"WebSocket server started on ws://{websocket_data[0]}:{websocket_data[1]}")
            await asyncio.Future() # Run forever
    except OSError as e: # Another websocket instance is already running
        if '10048' in str(e):
            raise Exception("[LiveApexSocket] existingInstance: Another websocket instance is already running")

        else:
            raise e

if __name__ == "__main__":
    asyncio.run(main())