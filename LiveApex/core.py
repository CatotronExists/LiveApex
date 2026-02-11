import asyncio
import websockets
import os
import site
import traceback
import json
import importlib

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

        print("[LiveApexCore] WebSocket Server Task Ended")

    async def startListener(callback, method = "Protobuf"):
        """
        # Start the LiveAPI WebSocket server

        This function starts the LiveAPI WebSocket server. It is used to connect to the game to send/receive events.
        
        ## Parameters

        :callback: (function) A function that takes a single parameter. All decoded WebSocket messages will be fowarded to this callback for handling. This is where you will handle all events from the game.
        :method: (string) The method to decode WebSocket messages. Can be either "Protobuf" or "JSON". Default is "Protobuf". Ensure your launch options are set correctly for your choice.

        ## Example

        ```python
        LiveApex.Core.startListener(callback, "Protobuf")
        ```
        """

        async with websockets.connect(f"ws://127.0.0.1:7777") as websocket:
            print("[LiveApexCore] Started WebSocket Listener\n[LiveApexCore] Awaiting connection to Apex client. This may take some time")
            async for raw_message in websocket: # Decode, check for init, foward to callback
                print(raw_message)
                if method == "JSON":
                    decoded_message = json.loads(raw_message)
                else: # Default to protobuf
                    decoded_message = Core.decodeSocketEvent(raw_message)

                if decoded_message is not None:
                    if 'category' in decoded_message and decoded_message['category'] == 'init':
                        print("[LiveApexCore] Connection to Apex client established, LiveApex is ready")
                
                await callback(decoded_message)

    def decodeSocketEvent(event: Any):
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
                            # Required due to Respawn jank
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

        except: # If the event is a sent command to the websocket and not a LiveAPIEvent, ignore it
            return None