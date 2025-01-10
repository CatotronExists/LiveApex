import websockets
import events_pb2
import json

with open('websocket.json', 'r') as f:
    websocket_data = json.load(f)

class LiveApexLobby:
    """
    # LiveApex Lobby

    This class contains functions for the LiveApex lobby.
    """

    async def sendChatMessage(text: str):
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
    
    async def customGetSettings():
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
    
    async def customGetPlayers():
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
    
    async def customSetTeamName(team_id, team_name):
        """
        # Set Team Name

        This function sets the name of a team.

        ## Parameters

        :team_id: The ID of the team.
        :team_name: The name of the team.

        ## Example

        ```python
        await LiveApexLobby.customSetTeamName(1, 'Awesome Team')
        ```
        """

        uri = f'ws://{websocket_data['host']}:{websocket_data['port']}'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            teamname = events_pb2.CustomMatch_SetTeamName(teamId=team_id, teamName=team_name)
            teamname.SerializeToString()
            
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetTeamName.CopyFrom(events_pb2.CustomMatch_SetTeamName(teamname))
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

            response = await websocket.recv()
            print(f"response: {response}")
        
    async def customKickPlayer(username, user_hash):
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
    
    async def customMovePlayer(team_id, hardware_name, user_hash):
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
    
    async def customTogglePause():
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
    
    async def customCreateMatch():
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
    

