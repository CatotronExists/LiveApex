import asyncio
import websockets

## LiveApex WebSocket Server ##
# This starts the WebSocket server for the LiveApex library #

connected_clients = set()

async def echo(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket: # Broadcast the message to all connected clients
            tasks = [asyncio.create_task(client.send(message)) for client in connected_clients]
            await asyncio.gather(*tasks)

    except websockets.exceptions.ConnectionClosedOK: 
        pass

    finally: 
        connected_clients.remove(websocket)

async def main():
    try:
        print("[LiveApexSocket] Starting WebSocket Server")

        async with websockets.serve(echo, '127.0.0.1', '7777', open_timeout=None, ping_timeout=None):
            print(f"[LiveApexSocket] WebSocket server started on ws://127.0.0.1:7777")
            await asyncio.Future() # Run forever

    except OSError as e: # Another websocket instance is already running
        if '10048' in str(e): 
            raise Exception("[LiveApexSocket] existingInstance: Another websocket instance is already running")

        else: 
            raise e