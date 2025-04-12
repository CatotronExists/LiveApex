# This is a basic example of how to structure your code to use the LiveApex API.

import LiveApex
import asyncio

websocket_data = {'host': '127.0.0.1', 'port': 7777}

async def filter_events(event):
    if event != None:
        if 'category' in event:
            if event['category'] == "init":
                await LiveApex.Lobby.sendChatMessage("[LiveApex] Startup Successful", websocket_data)
                await LiveApex.Lobby.getPlayers(websocket_data)

            # Your program should roughly follow this structure...
            # running a function after a certain event is received


async def api_socket():
    # Start the API
    api_task = asyncio.create_task(LiveApex.Core.startLiveAPI(websocket_data))
    listener_task = asyncio.create_task(LiveApex.Core.startListener(filter_events, websocket_data))

    await asyncio.gather(api_task, listener_task)

asyncio.run(api_socket())