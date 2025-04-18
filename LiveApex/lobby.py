import websockets
from . import events_pb2

### LiveApex Lobby Functions ###
# These functions are used to interact with the lobby and players in the custom match #

class Lobby:
    """
    # Lobby

    This class contains functions to alter or get data on the lobby and it's players.
    """

    async def sendChatMessage(text: str):
        """
        # Send a Chat Message

        This function sends a chat message to the lobby.

        ## Parameters

        :text: The text of the chat message.

        ## Notes

        :sendChatMessage: has a rate limit of ~10 messages in quick succession, any messages after this limit will be ignored by the game.

        ## Example

        ```python
        await LiveApex.Lobby.sendChatMessage('Hello World!')
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SendChat.CopyFrom(events_pb2.CustomMatch_SendChat(text=text))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def togglePause(countdown: int):
        """
        # Toggle Pause

        This function toggles the pause state of the custom match.

        ## Parameters

        :countdown: The countdown until the match is paused/unpaused. If set to 0, the match pause state will change instantly.

        ## Example

        ```python
        await LiveApex.Lobby.togglePause(5)
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_TogglePause.CopyFrom(events_pb2.CustomMatch_TogglePause(preTimer=countdown))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def createLobby():
        """
        # Create Lobby

        This function creates a custom match lobby.

        ## Example

        ```python
        await LiveApex.Lobby.createLobby()
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_CreateLobby.CopyFrom(events_pb2.CustomMatch_CreateLobby())

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def joinLobby(lobby_code: str):
        """
        # Join Lobby

        This function joins a custom match lobby.

        ## Parameters

        :lobby_code: The lobby code to join (either admin or player code works).

        ## Example

        ```python
        await LiveApex.Lobby.joinLobby(abcd1234)
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_JoinLobby.CopyFrom(events_pb2.CustomMatch_JoinLobby(roleToken=lobby_code))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def leaveLobby():
        """
        # Leave Lobby

        This function leaves a custom match lobby.

        ## Example

        ```python
        await LiveApex.Lobby.leaveLobby()
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_LeaveLobby.CopyFrom(events_pb2.CustomMatch_LeaveLobby())

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def setReady(ready: bool):
        """
        # Set Ready

        This function sets the ready state of the player.

        ## Parameters

        :ready: The ready state of the player.

        ## Example

        ```python
        await LiveApex.Lobby.setReady(True)
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetReady.CopyFrom(events_pb2.CustomMatch_SetReady(isReady=ready))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def setTeamName(team_id: int, team_name: str):
        """
        # Set Team Name

        This function sets the name of a team.

        ## Parameters

        :team_id: The ID of the team. team_id=0 is unassigned, team_id=1 is observer, team_id=2 is team 1 and so on.
        :team_name: The name of the team.

        ## Notes

        Team names can only be set when using lobby codes from EA/Respawn.

        ## Raises

        `notInLobby` - Not connected to a custom match.\n
        `notInGame` - Game client is not running Apex Legends or is not past the main menu.\n
        `invalidTeamIndex` - Invalid team index, must be a value between 1 and 21 (Differs gamemode to gamemode).

        ## Example

        ```python
        await LiveApex.Lobby.setTeamName(2, 'Awesome Team')
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetTeamName.CopyFrom(events_pb2.CustomMatch_SetTeamName(teanId=team_id, teamName=team_name))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def getPlayers():
        """
        # Get Custom Match Players

        This function gets the custom match players.

        ## Example

        ```python
        await LiveApex.Lobby.getPlayers()
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_GetLobbyPlayers.CopyFrom(events_pb2.CustomMatch_GetLobbyPlayers())

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def movePlayer(team_id: int, hardware_name: str, user_hash: str):
        """
        # Set Team

        This function moves a player to a different team.

        ## Parameters

        :team_id: The ID of the team. team_id=0 is unassigned, team_id=1 is observer, team_id=2 is team 1 and so on.
        :hardware_name: The platform of the player, i.e PC-STEAM.
        :user_hash: The hash of the player. Obtained via LiveApex.Lobby.getPlayers().

        ## Example

        ```python
        await LiveApex.Lobby.movePlayer(2, 'PC-STEAM', 'ad431d95fd8cdaf5e56f2b661cada2fb')
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetTeam.CopyFrom(events_pb2.CustomMatch_SetTeam(teamId=team_id, targetHardwareName=hardware_name, targetNucleusHash=user_hash))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def kickPlayer(hardware_name: str, user_hash: str):
        """
        # Kick Player

        This function kicks a player from the custom match.

        ## Parameters

        :hardware_name: The platform of the player, i.e PC-STEAM.
        :user_hash: The hash of the player.

        ## Example

        ```python
        await LiveApex.Lobby.kickPlayer('PC-STEAM', 'ad431d95fd8cdaf5e56f2b661cada2fb')
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_KickPlayer.CopyFrom(events_pb2.CustomMatch_KickPlayer(targetHardwareName=hardware_name, targetNucleusHash=user_hash))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def getSettings():
        """
        # Get Custom Match Settings

        This function gets the custom match settings.

        ## Example

        ```python
        await LiveApex.Lobby.getSettings()
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_GetSettings.CopyFrom(events_pb2.CustomMatch_GetSettings())
            request.withAck = True

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def setSettings(playlist_name: str, admin_chat: bool, team_rename: bool, self_assign: bool, aim_assist: bool, anon_mode: bool):
        """
        # Set Custom Match Settings

        This function sets the custom match settings.

        ## Parameters

        :playlist_name: The name of the playlist.
        :admin_chat: Whether to enable admin chat.
        :team_rename: Whether to enable team renaming.
        :self_assign: Whether to enable self assign.
        :aim_assist: Whether to enable aim assist.
        :anon_mode: Whether to enable anonymous mode.

        ## Example

        ```python
        await LiveApex.Lobby.setSettings(des_hu_cm, True, True, True, False, False)
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetSettings.CopyFrom(events_pb2.CustomMatch_SetSettings(playlistName=playlist_name, adminChat=admin_chat, teamRename=team_rename, selfAssign=self_assign, aimAssist=aim_assist, anonMode=anon_mode))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def setLegendBan(bans: list[str]):
        """
        # Set Legend Ban

        This function sets legend bans for the lobby. To reset the bans, run this function with an empty list.

        ## Parameters

        :bans: A list of legend names to ban.

        ## Example

        ```python
        await LiveApex.Lobby.setLegendBan(['wraith', 'madmaggie'])
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetLegendBan.CopyFrom(events_pb2.CustomMatch_SetLegendBan(legendRefs=bans))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def getLegendBans():
        """
        # Get Legend Bans

        This function gets the legend bans for the lobby.

        ## Example

        ```python
        await LiveApex.Lobby.getLegendBans()
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_GetLegendBanStatus.CopyFrom(events_pb2.CustomMatch_GetLegendBanStatus())

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def startGame(status: bool):
        """
        # Start Game

        This function starts/stops custom match matchmaking.

        ## Parameters

        :status: Whether to start or stop matchmaking.

        ## Example

        ```python
        await LiveApex.Lobby.startGame(True)
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetMatchmaking.CopyFrom(events_pb2.CustomMatch_SetMatchmaking(enabled=status))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def setDropLocation(team_id: int, drop_location: int):
        """
        # Set Drop Location

        This function sets the drop location of a team.

        ## Parameters

        :team_id: The ID of the team. team_id=0 is unassigned, team_id=1 is observer, team_id=2 is team 1 and so on.
        :drop_location: The POI ID of any POI (this is the same system as the @XX that can also be used to set drop locations).

        ## Example

        ```python
        await LiveApex.Lobby.setDropLocation(2, 20)
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            request.customMatch_SetSpawnPoint.CopyFrom(events_pb2.CustomMatch_SetSpawnPoint(teamId=team_id, spawnPoint=drop_location))

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def setEndRingExclusions(map_region: str):
        """
        # Set End Ring Exclusions

        This function sets the end ring exclusions for the lobby. Run this function multiple times if you want to exclude multiple regions.

        ## Parameters

        :map_region: The map region to exclude. TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT, CENTER or REGIONS_COUNT to reset

        ## Example

        ```python
        await LiveApex.Lobby.setEndRingExclusions('TOP_LEFT')
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            # Construct the Request message
            request = events_pb2.Request()
            if map_region == "TOP_LEFT":
                request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.TOP_LEFT
            elif map_region == "TOP_RIGHT":
                request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.TOP_RIGHT
            elif map_region == "BOTTOM_LEFT":
                request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.BOTTOM_LEFT
            elif map_region == "BOTTOM_RIGHT":
                request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.BOTTOM_RIGHT
            elif map_region == "CENTER":
                request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.CENTER
            elif map_region == "REGIONS_COUNT":
                request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.REGIONS_COUNT
            else:
                raise ValueError("[LiveApexLobby] Invalid map region. Must be one of: TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT, CENTER or REGIONS_COUNT.")

            # Serialize the Request message
            serialized_request = request.SerializeToString()

            # Send the message
            await websocket.send(serialized_request)

    async def changeCamera(selection: str):
        """
        # Change Camera

        This function changes the camera of the observer.

        ## Parameters

        :selection: Player name or cycle to NEXT or PREVIOUS teammate or KILL_LEADER, CLOSEST_ENEMY, CLOSEST_PLAYER, LATEST_ATTACKER.

        ## Example

        ```python
        await LiveApex.Lobby.changeCamera('KILL_LEADER')
        ```
        """

        uri = 'ws://127.0.0.1:7777'
        if selection in ["NEXT", "PREVIOUS", "KILL_LEADER", "CLOSEST_ENEMY", "CLOSEST_PLAYER", "LATEST_ATTACKER"]:
            async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
                # Construct the Request message
                request = events_pb2.Request()
                if selection == "NEXT":
                    request.changeCamera.poi = events_pb2.PlayerOfInterest.NEXT
                elif selection == "PREVIOUS":
                    request.changeCamera.poi = events_pb2.PlayerOfInterest.PREVIOUS
                elif selection == "KILL_LEADER":
                    request.changeCamera.poi = events_pb2.PlayerOfInterest.KILL_LEADER
                elif selection == "CLOSEST_ENEMY":
                    request.changeCamera.poi = events_pb2.PlayerOfInterest.CLOSEST_ENEMY
                elif selection == "CLOSEST_PLAYER":
                    request.changeCamera.poi = events_pb2.PlayerOfInterest.CLOSEST_PLAYER
                elif selection == "LATEST_ATTACKER":
                    request.changeCamera.poi = events_pb2.PlayerOfInterest.LATEST_ATTACKER

        else:
            async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
                # Construct the Request message
                request = events_pb2.Request()
                request.changeCamera.CopyFrom(events_pb2.ChangeCamera(playerName=selection))

                # Serialize the Request message
                serialized_request = request.SerializeToString()

                # Send the message
                await websocket.send(serialized_request)