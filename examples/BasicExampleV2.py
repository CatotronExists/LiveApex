# This is a basic example of how to structure your code to use the LiveApex API. #

import LiveApex
import asyncio

async def filter_events(event):
    if event != None:
        if 'category' in event:
            if event['category'] == "init":
                await LiveApex.Lobby.sendChatMessage("[LiveApex] Startup Successful")
                await LiveApex.Lobby.getPlayers()

            # Your program should roughly follow this structure...
            # running a function after a certain event is received


async def main():
    # Start the API
    api_task = asyncio.create_task(LiveApex.Core.startLiveAPI())
    listener_task = asyncio.create_task(LiveApex.Core.startListener(filter_events, method = "Protobuf"))

    await asyncio.gather(api_task, listener_task)

asyncio.run(main())