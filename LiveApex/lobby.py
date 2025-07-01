import websockets
import json

### LiveApex Lobby Functions ###
# These functions are used to interact with the lobby and players in the custom match #

class Lobby:
    """
    # Lobby

    This class contains functions to alter or get data on the lobby and it's players.
    """

    async def sendChatMessage(text):
        """
        # Send a Chat Message

        Send a chat message to the pre-game lobby.

        ## Parameters

        :text: (any) The text of the chat message.

        ## Notes

        :sendChatMessage: has a rate limit of ~10 messages in quick succession, any messages after this limit will be ignored by the game.
        Only works while in lobby, Apex ignores this request during games.

        ## Example

        ```python
        await LiveApex.Lobby.sendChatMessage('Hello World!')
        ```
        """

        async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
            await websocket.send(json.dumps({"customMatch_SendChat": {"text": str(text)}}))

    async def togglePause(countdown):
        """
        # Toggle Pause

        Toggle the pause state of the in-progress custom match.

        ## Parameters

        :countdown: (int) The countdown until the match is paused/unpaused. If set to 0, the match pause state will change instantly.

        ## Example

        ```python
        await LiveApex.Lobby.togglePause(5)
        ```
        """

        if isinstance(countdown, int):
            async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
                await websocket.send(json.dumps({"customMatch_TogglePause": {"preTimer": str(countdown)}}))

        else:
            raise ValueError(f"[customMatch_TogglePause] countdown expects int value")

    async def createLobby():
        """
        # Create Lobby

        Create a custom match lobby, these lobbies have player requirements to start.

        ## Example

        ```python
        await LiveApex.Lobby.createLobby()
        ```
        """

        async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
            await websocket.send(json.dumps({"customMatch_CreateLobby": {}}))

    async def joinLobby(lobby_code):
        """
        # Join Lobby

        Send request to join a custom match lobby with specified code.

        ## Parameters

        :lobby_code: (str) The lobby code to join (either admin or player code).

        ## Example

        ```python
        await LiveApex.Lobby.joinLobby('abcd1234')
        ```
        """

        if isinstance(lobby_code, str):
            async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
                await websocket.send(json.dumps({"customMatch_JoinLobby": {"roleToken": lobby_code}}))

        else:
            raise ValueError(f"[customMatch_JoinLobby] lobby_code expects str value")

    async def leaveLobby():
        """
        # Leave Lobby

        Request to leave current custom match lobby.

        ## Example

        ```python
        await LiveApex.Lobby.leaveLobby()
        ```
        """

        async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
            await websocket.send(json.dumps({"customMatch_LeaveLobby": {}}))

    async def setReady(ready):
        """
        # Set Ready

        Change ready state of client

        ## Parameters

        :ready: (bool) The ready state of the client.

        ## Example

        ```python
        await LiveApex.Lobby.setReady(True)
        ```
        """

        if isinstance(ready, bool):
            async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
                await websocket.send(json.dumps({"customMatch_SetReady": {"isReady": ready}}))

        else:
            raise ValueError(f"[customMatch_SetReady] ready expects bool value")

    async def setTeamName(team_id, team_name):
        """
        # Set Team Name

        Sets the name of a requested team.

        ## Parameters

        :team_id: (int) The ID of the team. team_id=0 is unassigned, team_id=1 is observer, team_id=2 is team 1 and so on.
        :team_name: (str) The name of the team.

        ## Notes

        Team names can only be set when using lobby codes from EA/Respawn.

        ## Example

        ```python
        await LiveApex.Lobby.setTeamName(2, 'Awesome Team')
        ```
        """

        if isinstance(team_id, int) and isinstance(team_name, str):
            async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
                await websocket.send(json.dumps({"customMatch_SetTeamName": {"teamId": team_id, "teamName": team_name}}))

        else:
            raise ValueError(f"[customMatch_SetTeamName] One or more of the following values are invaild:\n   [customMatch_SetTeamName] team_id expects int value\n   [customMatch_SetTeamName] team_name expects str value")

    async def getPlayers():
        """
        # Get Custom Match Players

        Requests data for all custom match players.

        ## Example

        ```python
        await LiveApex.Lobby.getPlayers()
        ```
        """

        async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
            await websocket.send(json.dumps({"customMatch_GetLobbyPlayers": {}}))

    async def movePlayer(team_id, hardware_name, user_hash):
        """
        # Set Team

        Move a player to a different team.

        ## Parameters

        :team_id: (int) The ID of the team. team_id=0 is unassigned, team_id=1 is observer, team_id=2 is team 1 and so on.
        :hardware_name: (str) The platform of the player, i.e PC-STEAM.
        :user_hash: (str) The hash of the player. Obtained via LiveApex.Lobby.getPlayers().

        ## Example

        ```python
        await LiveApex.Lobby.movePlayer(2, 'PC-STEAM', 'ad431d95fd8cdaf5e56f2b661cada2fb')
        ```
        """

        if isinstance(team_id, int) and isinstance(hardware_name, str) and isinstance(user_hash, str):
            async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
                await websocket.send(json.dumps({"customMatch_SetTeam": {"teamId": team_id, "targetHardwareName": hardware_name, "targetNucleusHash": user_hash}}))

        else:
            raise ValueError(f"[customMatch_SetTeam] One or more of the following values are invaild:\n   [customMatch_SetTeam] team_id expects int value\n   [customMatch_SetTeam] hardware_name expects str value\n   [customMatch_SetTeam] user_hash expects str value")

    async def kickPlayer(hardware_name, user_hash):
        """
        # Kick Player

        Kick a player from the custom match.

        ## Parameters

        :hardware_name: (str) The platform of the player, i.e PC-STEAM.
        :user_hash: (str) The hash of the player.

        ## Example

        ```python
        await LiveApex.Lobby.kickPlayer('PC-STEAM', 'ad431d95fd8cdaf5e56f2b661cada2fb')
        ```
        """

        if isinstance(hardware_name, str) and isinstance(user_hash, str):
            async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
                await websocket.send(json.dumps({"customMatch_KickPlayer": {"targetHardwareName": hardware_name, "targetNucleusHash": user_hash}}))

        else:
            raise ValueError(f"[customMatch_KickPlayer] One or more of the following values are invaild:\n   [customMatch_KickPlayer] hardware_name expects str value\n   [customMatch_KickPlayer] user_hash expects str value")

    async def getSettings():
        """
        # Get Custom Match Settings

        Gets current custom match settings.

        ## Example

        ```python
        await LiveApex.Lobby.getSettings()
        ```
        """

        async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
            await websocket.send(json.dumps({"customMatch_GetSettings": {}}))

    async def setSettings(playlist_name, admin_chat, team_rename, self_assign, aim_assist, anon_mode):
        """
        # Set Custom Match Settings

        Set custom match settings.

        ## Parameters

        :playlist_name: (str) The name of the playlist.
        :admin_chat: (bool) Enable/Disable admin chat.
        :team_rename: (bool) Enable/Disable team renaming.
        :self_assign: (bool) Enable/Disable self assign.
        :aim_assist: (bool) Enable/Disable aim assist.
        :anon_mode: (bool) Enable/Disable anonymous mode.

        ## Notes

        All parameters need to be supplied each time setSettings() is used.

        ## Example

        ```python
        await LiveApex.Lobby.setSettings(des_hu_cm, True, True, True, False, False)
        ```
        """

        if isinstance(playlist_name, str) and isinstance(admin_chat, bool) and isinstance(team_rename, bool) and isinstance(self_assign, bool) and isinstance(aim_assist, bool) and isinstance(anon_mode, bool):
            async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
                await websocket.send(json.dumps({"customMatch_SetSettings": {"playlistName": playlist_name, "adminChat": admin_chat, "teamRename": team_rename, "selfAssign": self_assign, "aimAssist": aim_assist, "anonMode": anon_mode}}))

        else:
            raise ValueError(f"[customMatch_SetSettings] One or more of the following values are invaild:\n   [customMatch_SetSettings] playlist_name expects str value\n   [customMatch_SetSettings] admin_chat expects bool value\n   [customMatch_SetSettings] team_rename expects bool value\n   [customMatch_SetSettings] self_assign expects bool value\n   [customMatch_SetSettings] aim_assist expects bool value\n   [customMatch_SetSettings] anon_mode expects bool value")

    async def setLegendBan(bans):
        """
        # Set Legend Ban

        Sets legend bans for the lobby. To reset the bans, run this function with an empty list.

        ## Parameters

        :bans: (list[str]) A list of legend names to ban, all list items must be str.

        ## Example

        ```python
        await LiveApex.Lobby.setLegendBan(['wraith', 'madmaggie'])
        ```
        """

        scan = 0
        if isinstance(bans, list):
            for i in bans: # Check if each item is a str
                if isinstance(i, str): pass
                else: scan +=1

            if scan == 0: # If all items are str -> send to websocket
                async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
                    await websocket.send(json.dumps({"customMatch_SetLegendBan": {"legendRefs": ''.join(bans)}}))
            else:
                raise ValueError(f"[customMatch_SetLegendBan] bans expects all list values to be str")

        else:
            raise ValueError(f"[customMatch_SetLegendBan] bans expects list value")

    async def getLegendBans():
        """
        # Get Legend Bans

        Get a list of current legend bans.

        ## Example

        ```python
        await LiveApex.Lobby.getLegendBans()
        ```
        """

        async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
            await websocket.send(json.dumps({"customMatch_GetLegendBanStatus": {}}))

    async def startGame(status):
        """
        # Start Game

        Send request to start/stop custom match matchmaking.

        ## Parameters

        :status: (bool) Start/stop matchmaking.

        ## Example

        ```python
        await LiveApex.Lobby.startGame(True)
        ```
        """

        if isinstance(status, bool):
            async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
                await websocket.send(json.dumps({"customMatch_SetMatchmaking": {"enabled": status}}))

        else:
            raise ValueError(f"[customMatch_SetMatchmaking] status expects bool value")

    async def setDropLocation(team_id, drop_location):
        """
        # Set Drop Location

        This function sets the drop location of a team.

        ## Parameters

        :team_id: (int) The ID of the team. team_id=0 is unassigned, team_id=1 is observer, team_id=2 is team 1 and so on.
        :drop_location: (int) The POI ID of any POI (this is the same system as the @XX that can also be used to set drop locations).

        ## Example

        ```python
        await LiveApex.Lobby.setDropLocation(2, 20)
        ```
        """

        if isinstance(team_id, int) and isinstance(drop_location, int):
            async with websockets.connect(uri="ws://127.0.0.1:7777", ping_interval=20, ping_timeout=20) as websocket:
                await websocket.send(json.dumps({"customMatch_SetSpawnPoint": {"teamId": team_id, "spawnPoint": drop_location}}))

        else:
            raise ValueError(f"[customMatch_SetSpawnPoint] One or more of the following values are invaild:\n   [customMatch_SetSpawnPoint] team_id expects int value\n   [customMatch_SetSpawnPoint] drop_location expects int value")

    ### TEMP DISABLED
    # async def setEndRingExclusions(map_region):
    #     """
    #     # Set End Ring Exclusions

    #     This function sets the end ring exclusions for the lobby. Run this function multiple times if you want to exclude multiple regions.

    #     ## Parameters

    #     :map_region: (str) The map region to exclude. TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT, CENTER or use REGIONS_COUNT to reset

    #     ## Example

    #     ```python
    #     await LiveApex.Lobby.setEndRingExclusions('TOP_LEFT')
    #     ```
    #     """

    #     uri = 'ws://127.0.0.1:7777'
    #     async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
    #         # Construct the Request message
    #         request = events_pb2.Request()
    #         if map_region == "TOP_LEFT":
    #             request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.TOP_LEFT
    #         elif map_region == "TOP_RIGHT":
    #             request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.TOP_RIGHT
    #         elif map_region == "BOTTOM_LEFT":
    #             request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.BOTTOM_LEFT
    #         elif map_region == "BOTTOM_RIGHT":
    #             request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.BOTTOM_RIGHT
    #         elif map_region == "CENTER":
    #             request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.CENTER
    #         elif map_region == "REGIONS_COUNT":
    #             request.customMatch_SetEndRingExclusion.selectionToExclude = events_pb2.MapRegion.REGIONS_COUNT
    #         else:
    #             raise ValueError("[LiveApexLobby] Invalid map region. Must be one of: TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT, CENTER or REGIONS_COUNT.")

    #         # Serialize the Request message
    #         serialized_request = request.SerializeToString()

    #         # Send the message
    #         await websocket.send(serialized_request)

    # async def changeCamera(selection, input):
    #     """
    #     # Change Camera

    #     This function changes the camera of the observer.

    #     ## Parameters

    #     :selection: (str) Player name, nucleusHash or use one of the following poi options: NEXT, PREVIOUS, KILL_LEADER, CLOSEST_ENEMY, CLOSEST_PLAYER, LATEST_ATTACKER.
    #     :input: (str) poi ["NEXT", "PREVIOUS", "KILL_LEADER", "CLOSEST_ENEMY", "CLOSEST_PLAYER", "LATEST_ATTACKER"], player or hash.

    #     ## Example

    #     ```python
    #     await LiveApex.Lobby.changeCamera('KILL_LEADER')
    #     ```
    #     """

    #     uri = 'ws://127.0.0.1:7777'

    #     async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
    #         # Construct the Request message
    #         request = events_pb2.Request()
    #         if input == "poi":
    #             if selection in ["NEXT", "PREVIOUS", "KILL_LEADER", "CLOSEST_ENEMY", "CLOSEST_PLAYER", "LATEST_ATTACKER"]:
    #                 if selection == "NEXT":
    #                     request.changeCamera.poi = events_pb2.PlayerOfInterest.NEXT
    #                 elif selection == "PREVIOUS":
    #                     request.changeCamera.poi = events_pb2.PlayerOfInterest.PREVIOUS
    #                 elif selection == "KILL_LEADER":
    #                     request.changeCamera.poi = events_pb2.PlayerOfInterest.KILL_LEADER
    #                 elif selection == "CLOSEST_ENEMY":
    #                     request.changeCamera.poi = events_pb2.PlayerOfInterest.CLOSEST_ENEMY
    #                 elif selection == "CLOSEST_PLAYER":
    #                     request.changeCamera.poi = events_pb2.PlayerOfInterest.CLOSEST_PLAYER
    #                 elif selection == "LATEST_ATTACKER":
    #                     request.changeCamera.poi = events_pb2.PlayerOfInterest.LATEST_ATTACKER

    #         elif input == "player":
    #             request.changeCamera.name = selection

    #         elif input == "hash":
    #             request.changeCamera.nucleusHash = selection

    #         # Construct the Request message
    #         request = events_pb2.Request()
    #         request.changeCamera.CopyFrom(events_pb2.ChangeCamera(target=selection))

    #         # Serialize the Request message
    #         serialized_request = request.SerializeToString()

    #         # Send the message
    #         await websocket.send(serialized_request)