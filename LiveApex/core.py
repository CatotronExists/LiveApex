import json
import asyncio
import websockets

from google.protobuf.any_pb2 import Any
from google.protobuf import symbol_database
from google.protobuf.json_format import MessageToDict
import events_pb2

with open('websocket.json', 'r') as f:
    websocket_data = json.load(f)

### LiveApex Core Functions ###
# These functions are essential for the LiveApex library to work #

class LiveApexCore:
    async def startLiveAPI():
        # Due to issues for now run server.py then run tests/your programs

        # start server subprocess
        process = await asyncio.create_subprocess_exec(
            "python", "server.py",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        print("[LiveApexCore] Started WebSocket server")

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
        await process.stdout.close()
        await process.stderr.close()

        print("[LiveApexCore] WebSocket server process ended")

    async def startListener(callback):
        async with websockets.connect(f"ws://{websocket_data['host']}:{websocket_data['port']}") as websocket:
            print("[LiveApexCore] Started WebSocket listener")
            async for message in websocket:
                decoded = LiveApexCore.decodeSocketEvent(message)

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
                live_api_event = events_pb2.LiveAPIEvent()
                live_api_event.ParseFromString(event)

                print(f"live api event: {live_api_event}")
                # Unpack the gameMessage field
                game_message = Any()
                game_message.CopyFrom(live_api_event.gameMessage)

                # Get the type of the contained message
                result_type = game_message.TypeName()
                print(f"result type: {result_type}")
                
                if result_type == "rtech.liveapi.Response":
                    return None

                msg_result = symbol_database.Default().GetSymbol(result_type)()
                print(f"symbol: {symbol_database.Default().GetSymbol(result_type)()}")

                game_message.Unpack(msg_result)
            
            except Exception as e:
                if 'Couldn\'t find message' in str(e): # Assume its a response. Fixes breaking after SendChat, maybe due to the response?
                    try:
                        live_api_event = events_pb2.Response()
                        live_api_event.ParseFromString(event)

                        game_message = Any()
                        game_message.CopyFrom(live_api_event.result)

                        result_type = game_message.TypeName()

                        msg_result = symbol_database.Default().GetSymbol(result_type)()

                        game_message.Unpack(msg_result)

                    except Exception as e:
                        return {'Error': 'Unknown Error', 'Raw': event, 'Exception': str(e)}

                else:
                    return {'Error': 'Unknown message type', 'Raw': event}

            # Turn the message into a dictionary
            result = MessageToDict(msg_result)

            return result