import asyncio
import websockets
import os
import site
import traceback
import json

### LiveApex Core Functions ###
# These functions are essential for the LiveApex library to work #

class Core:
    """
    # Core

    This class contains functions to start the WebSocket server and listener.
    """

    async def startLiveAPI(debug = False):
        """
        # Start the LiveAPI WebSocket server

        This function starts the LiveAPI WebSocket server. It is used to connect to the game to send/receive events.

        ## Example

        ```python
        LiveApex.Core.startLiveAPI()
        ```
        """

        # Get server.py path
        server_path = os.path.join(site.getsitepackages()[0], "Lib", "site-packages", "LiveApex", "server.py")

        # start server.py subprocess
        process = await asyncio.create_subprocess_exec(
            "python", server_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        print(r"""
 _     _              _
| |   (_)_   _____   / \   _ __   _____  __
| |   | \ \ / / _ \ / _ \ | '_ \ / _ \ \/ /
| |___| |\ V /  __// ___ \| |_) |  __/>  <
|_____|_| \_/ \___/_/   \_\ .__/ \___/_/\_\
                            |_|
===========================================
Version 1.2.0 // 1/07/2025
        """)
        print("[LiveApexCore] Starting WebSocket Server")

        # Read the output and error streams
        async def read_stream(stream, callback):
            while True:
                line = await stream.readline()
                if not line:
                    break
                callback(line.decode().strip())

        # Define output and error streams
        if debug == False:
            stdout_task = asyncio.create_task(read_stream(process.stdout, lambda x: print(f"[LiveApexSocket] {x}")))
            stderr_task = asyncio.create_task(read_stream(process.stderr, lambda x: print(f"[LiveApexSocket] [ERROR] {x}")))

        elif debug == True:
            stdout_task = asyncio.create_task(read_stream(process.stdout, lambda x: print(f"[LiveApexSocket] {x}\n===\nError Log\n{traceback.format_exc()}\n===")))
            stderr_task = asyncio.create_task(read_stream(process.stderr, lambda x: print(f"[LiveApexSocket] [ERROR] {x}\n===\nError Log\n{traceback.format_exc()}\n===")))

        # Keep socket process running
        await process.wait()

        # Close streams after socket ends
        stdout_task.cancel()
        stderr_task.cancel()

        # Catch any exceptions that happen when tasks end
        try:
            try:
                await stdout_task
                await stderr_task
            except asyncio.CancelledError as e:
                if debug == False: print(f"[LiveApexCore] Error: {e}")
                elif debug == True: print(f"[LiveApexCore] Error: {e}\n===\nError Log\n{traceback.format_exc()}\n===")
                pass
        except Exception as e:
            if debug == False: print(f"[LiveApexCore] Error: {e}")
            elif debug == True: print(f"[LiveApexCore] Error: {e}\n===\nError Log\n{traceback.format_exc()}\n===")
            pass

        print("[LiveApexCore] WebSocket Server Process Ended")

    # Define how websocket events are handled
    async def startListener(callback):
        async with websockets.connect(f"ws://127.0.0.1:7777") as websocket:
            print("[LiveApexCore] Started WebSocket Listener")
            async for message in websocket:
                message = json.loads(message)
                await callback(message) # Convert to JSON, recieved as str