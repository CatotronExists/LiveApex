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

class Lobby:
    """
    # Lobby

    This class contains functions to alter or get data on the lobby and it's players.
    """

    async def setDropLocation(team_id: int, drop_location: int, websocket_data: dict):
        """
        # Set Drop Location

        This function sets the drop location of a team.

        ## Parameters

        :team_id: The ID of the team. team_id=0 is unassigned, team_id=1 is observer, team_id=2 is team 1 and so on.
        :drop_location: The POI ID of any POI (this is the same system as the @XX that can also be used to set drop locations).
        :websocket_data: The websocket data. This is a dictionary containing the host and port of the websocket server.

        ## Example

        ```python
        await LiveApex.Lobby.setDropLocation(2, 20, websocket_data)
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Serialize the drop location
            set_location = events_pb2.CustomMatch_SetSpawnPoint(teamID=team_id, spawnPoint=drop_location)
            set_location.SerializeToString()

            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetSpawnPoint.CopyFrom(set_location)

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
        :websocket_data: The websocket data. This is a dictionary containing the host and port of the websocket server.

        ## Example

        ```python
        await LiveApex.Lobby.sendChatMessage('Hello World!', websocket_data)
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

            # Serialize the Request message
            serialized_request = request.SerializeToString()
            
            # Send the message
            await websocket.send(serialized_request)
    
    async def getSettings(websocket_data: dict): ## IDK, DOESNT WORK
        """
        # Get Custom Match Settings

        This function gets the custom match settings.

        ## Parameters

        :websocket_data: The websocket data. This is a dictionary containing the host and port of the websocket server.

        ## Example
        
        ```python
        await LiveApex.Lobby.getSettings(websocket_data)
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
    
    async def getPlayers(websocket_data: dict):
        """
        # Get Custom Match Players

        This function gets the custom match players.

        ## Parameters

        :websocket_data: The websocket data. This is a dictionary containing the host and port of the websocket server.

        ## Example

        ```python
        await LiveApex.Lobby.getPlayers(websocket_data)
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_GetLobbyPlayers.CopyFrom(events_pb2.CustomMatch_GetLobbyPlayers())

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)
    
    async def setTeamName(team_id: int, team_name: str, websocket_data: dict):
        """
        # Set Team Name

        This function sets the name of a team.

        ## Parameters

        :team_id: The ID of the team. team_id=0 is unassigned, team_id=1 is observer, team_id=2 is team 1 and so on.
        :team_name: The name of the team.
        :websocket_data: The websocket data. This is a dictionary containing the host and port of the websocket server.

        ## Notes

        Team names can only be set when using lobby codes from EA/Respawn.
        
        ## Raises

        `notInLobby` - Not connected to a custom match.\n
        `notInGame` - Game client is not running Apex Legends or is not past the main menu.\n
        `invalidTeamIndex` - Invalid team index, must be a value between 1 and 21 (Differs gamemode to gamemode).

        ## Example

        ```python
        await LiveApex.Lobby.setTeamName(2, 'Awesome Team', websocket_data)
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            teamname = events_pb2.CustomMatch_SetTeamName(teanId=team_id, teamName=team_name)
            teamname.SerializeToString()
            
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetTeamName.CopyFrom(teamname)

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)



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
                        print(f"[LiveApexLobby] teamId {team_id} has been set to '{team_name}'")
                    else:
                        print(f"[LiveApexLobby] teamId {team_id} could not be set to '{team_name}'")
  
    async def kickPlayer(hardware_name: str, user_hash: str, websocket_data: dict):
        """
        # Kick Player

        This function kicks a player from the custom match.

        ## Parameters

        :username: The username of the player.
        :user_hash: The hash of the player.
        :websocket_data: The websocket data. This is a dictionary containing the host and port of the websocket server.

        ## Example

        ```python
        await LiveApex.Lobby.kickPlayer('PC-STEAM', 'ad431d95fd8cdaf5e56f2b661cada2fb', websocket_data)
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_KickPlayer.CopyFrom(events_pb2.CustomMatch_KickPlayer(targetHardwareName=hardware_name, targetNucleusHash=user_hash))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)
    
    async def movePlayer(team_id: int, hardware_name: str, user_hash: str, websocket_data: dict):
        """
        # Set Team

        This function moves a player to a different team.

        ## Parameters

        :team_id: The ID of the team. team_id=0 is unassigned, team_id=1 is observer, team_id=2 is team 1 and so on.
        :hardware_name: The platform of the player, i.e PC-STEAM.
        :user_hash: The hash of the player. Obtained via LiveApex.Lobby.getPlayers().

        ## Example

        ```python
        await LiveApex.Lobby.movePlayer(2, 'PC-STEAM', 'ad431d95fd8cdaf5e56f2b661cada2fb', 'websocket_data')
        ```
        """
            
        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            team = events_pb2.CustomMatch_SetTeam(teamId=team_id, targetHardwareName=hardware_name, targetNucleusHash=user_hash)
            team.SerializeToString()

            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetTeam.CopyFrom(team)

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)
    
    async def togglePause(websocket_data: dict):
        """
        # Toggle Pause

        This function toggles the pause state of the custom match.

        ## Example

        ```python
        await LiveApex.Lobby.togglePause(websocket_data)
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_TogglePause.CopyFrom(events_pb2.CustomMatch_TogglePause())

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)
    
    async def createMatch(websocket_data: dict):
        """
        # Create Custom Match

        This function creates a custom match.

        ## Example

        ```python
        await LiveApex.Lobby.createMatch()
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_CreateMatch.CopyFrom(events_pb2.CustomMatch_CreateMatch())

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)