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
    async def startLiveAPI(self, websocket_data: dict):
        # Convert websocket_data
        websocket_data_converted = f"{websocket_data['host']},{websocket_data['port']}"

        # Get server.py path
        server_path = os.path.join(site.getsitepackages()[0], "Lib", "site-packages", "LiveApex", "server.py")

        # start server subprocess
        process = await asyncio.create_subprocess_exec(
            "python", server_path, websocket_data_converted,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        print("[LiveApex Core] Starting WebSocket server")

        async def read_stream(stream, callback):
            while True:
                line = await stream.readline()
                if not line:
                    break
                callback(line.decode().strip())

        stdout_task = asyncio.create_task(read_stream(process.stdout, lambda x: print(f"[LiveApexSocket] {x}")))
        stderr_task = asyncio.create_task(read_stream(process.stderr, lambda x: print(f"[LiveApexSocket] [ERROR] {x}")))

        # Wait for the process to complete
        await process.wait()

        # Ensure the tasks are cancelled and the streams are closed
        stdout_task.cancel()
        stderr_task.cancel()

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

    async def startListener(self, callback, websocket_data: dict):
        async with websockets.connect(f"ws://{websocket_data['host']}:{websocket_data['port']}") as websocket:
            print("[LiveApexCore] Started WebSocket listener\n")
            async for message in websocket:
                decoded = Core.decodeSocketEvent(message)

                await callback(decoded)
        
    def decodeSocketEvent(self, event: Any):
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
            live_api_event = events_pb2.LiveAPIEvent()
            live_api_event.ParseFromString(event)

            #print(f"live api event: {live_api_event}")
            # Unpack the gameMessage field
            game_message = Any()
            game_message.CopyFrom(live_api_event.gameMessage)

            # Get the type of the contained message
            result_type = game_message.TypeName()
            #print(f"result type: {result_type}")
            
            if result_type != "": # "" Filters messages that are sent to the server
                if result_type != "rtech.liveapi.Response": # "rtech.liveapi.Response" Filters out responses (These are handled by other functions)
                    msg_result = symbol_database.Default().GetSymbol(result_type)()
                    #print(f"symbol: {symbol_database.Default().GetSymbol(result_type)()}")

                    game_message.Unpack(msg_result)

                    # Turn the message into a dictionary
                    result = MessageToDict(msg_result)

                    return result
                
                else:
                    return None
            
            else:
                return None
        
        except Exception as e:
            print(f"[LiveApexCore] Error decoding socket event: {e}")
            return None