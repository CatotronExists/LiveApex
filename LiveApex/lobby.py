import websockets
from google.protobuf.any_pb2 import Any
from google.protobuf import symbol_database
from google.protobuf.json_format import MessageToDict
from . import events_pb2

# ERROR FORMAT
# "Raw error message": "Raises: Reason"
errors = {
    "Client is not connected to a server. Ensure you are connected before proceeding.": "[LiveApexLobby] notInGame: Game client is not running Apex Legends or is not past the main menu",
    "Not connected to a custom match and this request requires you to have created/joined a lobby. Send CustomMatch_CreateLobby or CustomMatch_JoinLobby first": "[LiveApexLobby] notInLobby: Not connected to a custom match",
    "Invalid team index": "[LiveApexLobby] invalidTeamIndex: Invalid team index, must be a value between 1 and 21 (Differs gamemode to gamemode)",
    "Team name is too long.": "[LiveApexLobby] teamNameTooLong: Team name is too long, must be equal to or less than 255 characters",


}

class LiveApexLobby:
    """
    # LiveApex Lobby

    This class contains functions for the LiveApex lobby.
    """

    async def setDropLocation(teamid: int, dropLocation: int, websocket_data: dict):
        """
        # Set Drop Location

        This function sets the drop location of the lobby.

        ## Parameters

        :dropLocation: The drop location to set.

        ## Example

        ```python
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Serialize the drop location
            drop_location = events_pb2.CustomMatch_SetSpawnPoint(spawnPoint=dropLocation)
            drop_location.SerializeToString()

            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetSpawnPoint.CopyFrom(drop_location)
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def sendChatMessage(text: str, websocket_data: dict):
        """
        # Send a Chat Message

        This function sends a chat message to the lobby.

        ## Parameters

        :text: The text of the chat message.

        ## Example

        ```python
        await LiveApexLobby.sendChatMessage('Hello, World!')
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Serialize the chat message
            chat_message = events_pb2.CustomMatch_SendChat(text=text)
            chat_message.SerializeToString()

            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SendChat.CopyFrom(chat_message)
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()
            
            # Send the message
            await websocket.send(serialized_request)

            received_response_raw = await websocket.recv()
            response = events_pb2.Response()
            response.ParseFromString(received_response_raw)
            response = MessageToDict(response)
            print(f"chat response: {response}")
    
    async def customGetSettings(websocket_data: dict):
        """
        # Get Custom Match Settings

        This function gets the custom match settings.

        ## Example
        
        ```python
        await LiveApexLobby.customGetSettings()
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_GetSettings.CopyFrom(events_pb2.CustomMatch_GetSettings())
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)
    
    async def customGetPlayers(websocket_data: dict):
        """
        # Get Custom Match Players

        This function gets the custom match players.

        ## Example

        ```python
        await LiveApexLobby.customGetPlayers()
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_GetLobbyPlayers.CopyFrom(events_pb2.CustomMatch_GetLobbyPlayers())
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)
    
    async def customSetTeamName(teamId: int, teamName: str, websocket_data: dict):
        """
        # Set Team Name

        This function sets the name of a team.

        ## Parameters

        `team_id` The ID of the team. (1 is observer, 2 is team 1, 3 is team 2, etc.)\n
        `team_name` The name of the team.

        ## Notes

        Team names can only be set when using lobby codes from EA/Respawn.
        
        ## Raises

        `notInLobby` - Not connected to a custom match.\n
        `notInGame` - Game client is not running Apex Legends or is not past the main menu.\n
        `invalidTeamIndex` - Invalid team index, must be a value between 1 and 21 (Differs gamemode to gamemode).\n

        ## Example

        ```python
        await LiveApexLobby.customSetTeamName(1, 'Awesome Team')
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            teamname = events_pb2.CustomMatch_SetTeamName()
            teamname.teamId = teamId
            teamname.teamName = teamName
            teamname.SerializeToString()
            
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetTeamName.CopyFrom(teamname)
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

            # Await response and decode, first response is if the game received the message, second response is if the request was successful
            received_response_raw = await websocket.recv()
            response = events_pb2.Response()
            response.ParseFromString(received_response_raw)
            response = MessageToDict(response)
            print(f"team name response: {response}")

            if 'success' in response:
                if response['success'] == True:
                    print(f"[LiveApexLobby] Request recieved by game to set teamId {teamId} to '{teamName}'")
                else:
                    print(f"[LiveApexLobby] Request failed to set teamId {teamId} to '{teamName}'")

            # For Future Reference
            # I have no idea why but code from decodeSocketEvent() works perfectly fine for this
            # despite it using the wrong event_pb2.TYPE() and the wrong status_response.gameMessage (should be .result)
            # it works but there should be no way it does, im not complaining though
            status_response_raw = await websocket.recv()
            status_response = events_pb2.LiveAPIEvent()
            status_response.ParseFromString(status_response_raw)

            # Unpack the gameMessage field
            game_message = Any()
            game_message.CopyFrom(status_response.gameMessage)

            # Get the type of the contained message
            result_type = game_message.TypeName()
            
            if result_type != "":
                msg_result = symbol_database.Default().GetSymbol(result_type)()

                game_message.Unpack(msg_result)

                # Turn the message into a dictionary
                result = MessageToDict(msg_result)

                if 'result' in result:
                    if result['result']['status'] in errors:
                        raise Exception(errors[result['result']['status']])
                
                else:
                    if result['success'] == True:
                        print(f"[LiveApexLobby] teamId {teamId} has been set to '{teamName}'")
                    else:
                        print(f"[LiveApexLobby] teamId {teamId} could not be set to '{teamName}'")
  
    async def customKickPlayer(username, user_hash, websocket_data: dict):
        """
        # Kick Player

        This function kicks a player from the custom match.

        ## Parameters

        :username: The username of the player.
        :user_hash: The hash of the player.

        ## Example

        ```python
        await LiveApexLobby.customKickPlayer('player', 'hash')
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_KickPlayer.CopyFrom(events_pb2.CustomMatch_KickPlayer(username=username, userHash=user_hash))
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)
    
    async def customMovePlayer(team_id, hardware_name, user_hash, websocket_data: dict):
        """
        # Set Team

        This function moves a player to a different team.

        ## Parameters

        :team_id: The ID of the team. team_id=1 is observer, team_id=2 is team 1 and so on.
        :hardware_name: The platform of the player, i.e PC-STEAM.
        :user_hash: The hash of the player. Obtained via LiveApexLobby.customGetPlayers().

        ## Example

        ```python
        await LiveApexLobby.customMovePlayer(1, 'player', 'hash')
        ```
        """
            
        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            team = events_pb2.CustomMatch_SetTeam(teamId=team_id, targetHardwareName=hardware_name, targetNucleusHash=user_hash)
            team.SerializeToString()

            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetTeam.CopyFrom(team)
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)
    
    async def customTogglePause(websocket_data: dict):
        """
        # Toggle Pause

        This function toggles the pause state of the custom match.

        ## Example

        ```python
        await LiveApexLobby.customTogglePause()
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_TogglePause.CopyFrom(events_pb2.CustomMatch_TogglePause())
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)
    
    async def customCreateMatch(websocket_data: dict):
        """
        # Create Custom Match

        This function creates a custom match.

        ## Example

        ```python
        await LiveApexLobby.customCreateMatch()
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_CreateMatch.CopyFrom(events_pb2.CustomMatch_CreateMatch())
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)