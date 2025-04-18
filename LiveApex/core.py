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

    async def startLiveAPI():
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

        print("[LiveApexCore] Starting WebSocket Server")

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
                print(f"[LiveApexCore] Error: {e}")
                pass
        except Exception as e:
            print(f"[LiveApexCore] Error: {e}")
            pass

        print("[LiveApexCore] WebSocket Server Process Ended")

    # Define how websocket events are handled
    async def startListener(callback):
        async with websockets.connect(f"ws://127.0.0.1:7777") as websocket:
            print("[LiveApexCore] Started WebSocket Listener")
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
            # Parse event
            live_api_event = events_pb2.LiveAPIEvent()
            live_api_event.ParseFromString(event)

            try:
                result_type = live_api_event.gameMessage.TypeName()

                # Filters
                if result_type != "":
                    if result_type == "rtech.liveapi.Response": # Response messages
                        msg_result = symbol_database.Default().GetSymbol(result_type)()
                        live_api_event.gameMessage.Unpack(msg_result)
                        result = MessageToDict(msg_result)

                        if result['success'] == True:
                            if "CustomMatch_SetSettings" in result['result']['@type']: # if setting is False that setting is not sent
                                playlistName = result['result']['playlistName']
                                adminChat = result['result'].get('adminChat', False)
                                teamRename = result['result'].get('teamRename', False)
                                selfAssign = result['result'].get('selfAssign', False)
                                aimAssist = result['result'].get('aimAssist', False)
                                anonMode = result['result'].get('anonMode', False)
                                result = {
                                    "playListName": playlistName,
                                    "adminChat": adminChat,
                                    "teamRename": teamRename,
                                    "selfAssign": selfAssign,
                                    "aimAssist": aimAssist,
                                    "anonMode": anonMode,
                                }
                                return result

                    else: # LiveAPIEvents
                        msg_result = symbol_database.Default().GetSymbol(result_type)()
                        live_api_event.gameMessage.Unpack(msg_result)
                        result = MessageToDict(msg_result)
                        return result

                else: # Assume sending to websocket
                    return None

            except Exception as e:
                print(f"[LiveApexCore] Error decoding socket event: {e}")
                return None

        except Exception as e:
            print(f"[LiveApexCore] Error parsing event: {e}")
            return None