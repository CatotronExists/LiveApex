import asyncio
import websockets
import os
import site

from google.protobuf.any_pb2 import Any
from google.protobuf import symbol_database
from google.protobuf.json_format import MessageToDict
from . import events_pb2

### LiveApex Core Functions ###
# These functions are essential for the LiveApex library to work #

class Core:
    """
    # Core

    This class contains functions to start the WebSocket server and listener.
    """

    async def startLiveAPI(websocket_data):
        """
        # Start the LiveAPI WebSocket server

        This function starts the LiveAPI WebSocket server. It is used to connect to the game to send/receive events.

        ## Parameters

        :websocket_data: The websocket data to connect to the server.

        ## Example

        ```python
        LiveApex.Core.startLiveAPI(websocket_data)
        ```
        """

        # Convert websocket_data
        websocket_data_converted = f"{websocket_data['host']},{websocket_data['port']}"

        # Get server.py path
        server_path = os.path.join(site.getsitepackages()[0], "Lib", "site-packages", "LiveApex", "server.py")

        # start server.py subprocess
        process = await asyncio.create_subprocess_exec(
            "python", server_path, websocket_data_converted,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        print("[LiveApexCore] Starting WebSocket server")

        # Read the output and error streams
        async def read_stream(stream, callback):
            while True:
                line = await stream.readline()
                if not line:
                    break
                callback(line.decode().strip())

        # Define output and error streams
        stdout_task = asyncio.create_task(read_stream(process.stdout, lambda x: print(f"[LiveApexSocket] {x}")))
        stderr_task = asyncio.create_task(read_stream(process.stderr, lambda x: print(f"[LiveApexSocket] [ERROR] {x}")))

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
                print("[LiveApexCore] error: ", e)
                pass
        except Exception as e:
            print("[LiveApexCore] error: ", e)
            pass

        print("[LiveApexCore] WebSocket server process ended")

    # Define how websocket events are handled
    async def startListener(callback, websocket_data: dict):
        async with websockets.connect(f"ws://{websocket_data['host']}:{websocket_data['port']}") as websocket:
            print("[LiveApexCore] Started WebSocket listener\n")
            async for message in websocket:
                decoded = Core.decodeSocketEvent(message)

                await callback(decoded)

    def decodeSocketEvent(event: Any):
        """
        # Decode a Socket Event

        This function decodes a socket event. Used to convert socket events to a `dict`.

        ## Parameters

        :event: The event to decode.

        ## Returns

        The decoded event as `dict`.

        ## Example

        ```python
        decodeSocketEvent(event)
        ```
        """

        try:
            # Parse the event
            live_api_event = events_pb2.LiveAPIEvent()
            live_api_event.ParseFromString(event)

            # Unpack the gameMessage field
            game_message = Any()
            game_message.CopyFrom(live_api_event.gameMessage)

            # Get the type of the contained message
            result_type = game_message.TypeName()

            # Filter messages & return a dict result
            if result_type != "": # "" Filters messages that are sent to the server
                if result_type != "rtech.liveapi.Response": # "rtech.liveapi.Response" Filters out responses (These are handled by other functions)
                    msg_result = symbol_database.Default().GetSymbol(result_type)()
                    #print(msg_result)

                    game_message.Unpack(msg_result)
                    result = MessageToDict(msg_result)
                    return result

                else: # Some responses are converted to gameEvents (i.e CustomMatch_GetSettings)
                    #if 
                    print(f"[LiveApexCore] Filtered out response message\n{event}")
                    return None

            else:
                print(f"[LiveApexCore] Sent to websocket:\n{event}")
                return None

        except Exception as e:
            print(f"[LiveApexCore] Error decoding socket event: {e}")
            return None