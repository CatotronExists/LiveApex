from .core import Core

### LiveApex Lobby Functions ###
# These functions are used to interact with the lobby and players in the custom match #

class Lobby:
    """
    # Lobby

    This class contains functions to alter or get data on the lobby and it's players.
    """

    async def joinPartyServer():
        """
        # Join Party Server

        Proceeds game client to the lobby screen from the title screen.

        ## Notes
        This is a super powerful function that allows full automation when it comes to setting up custom matches.
        However, using any follow up commands, such as creating a lobby wont work until the game client has fully loaded into the lobby screen.
        Allow 10-20 seconds after using this command before sending any other lobby related commands.
        See an example of an automated lobby setup script at https://github.com/CatotronExists/LiveApex/tree/main/examples

        ## Example

        ```python
        await LiveApex.Lobby.joinPartyServer()
        ```
        """

        Core.sendWebSocketCommand({"joinPartyServer": {}})

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

        Core.sendWebSocketCommand({"customMatch_SendChat": {"text": str(text)}})

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
            Core.sendWebSocketCommand({"customMatch_TogglePause": {"preTimer": str(countdown)}})
        else:
            raise ValueError(f"[customMatch_TogglePause] countdown expects int value")

    async def createLobby():
        """
        # Create Lobby

        Creates a 'free' custom match lobby, these lobbies have player requirements to start.

        ## Example

        ```python
        await LiveApex.Lobby.createLobby()
        ```
        """

        Core.sendWebSocketCommand({"customMatch_CreateLobby": {}})

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
            Core.sendWebSocketCommand({"customMatch_JoinLobby": {"roleToken": lobby_code}})
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

        Core.sendWebSocketCommand({"customMatch_LeaveLobby": {}})

    async def setReady(ready):
        """
        # Set Ready

        Change ready state of client, to start/stop matchmaking.

        ## Parameters

        :ready: (bool) The ready state of the client.

        ## Example

        ```python
        await LiveApex.Lobby.setReady(True)
        ```
        """

        if isinstance(ready, bool):
            Core.sendWebSocketCommand({"customMatch_SetReady": {"isReady": ready}})
        else:
            raise ValueError(f"[customMatch_SetReady] ready expects bool value")

    async def setTeamName(team_id, team_name):
        """
        # Set Team Name

        Sets name of the requested team.

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
            Core.sendWebSocketCommand({"customMatch_SetTeamName": {"teamId": team_id, "teamName": team_name}})
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

        Core.sendWebSocketCommand({"customMatch_GetLobbyPlayers": {}})

    async def movePlayer(team_id, hardware_name, user_hash):
        """
        # Move Player

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
            Core.sendWebSocketCommand({"customMatch_SetTeam": {"teamId": team_id, "targetHardwareName": hardware_name, "targetNucleusHash": user_hash}})
        else:
            raise ValueError(f"[customMatch_SetTeam] One or more of the following values are invaild:\n   [customMatch_SetTeam] team_id expects int value\n   [customMatch_SetTeam] hardware_name expects str value\n   [customMatch_SetTeam] user_hash expects str value")

    async def kickPlayer(hardware_name, user_hash):
        """
        # Kick Player

        Kick the requested player from the custom match.

        ## Parameters

        :hardware_name: (str) The platform of the player, i.e PC-STEAM.
        :user_hash: (str) The hash of the player. Obtained via LiveApex.Lobby.getPlayers().

        ## Example

        ```python
        await LiveApex.Lobby.kickPlayer('PC-STEAM', 'ad431d95fd8cdaf5e56f2b661cada2fb')
        ```
        """

        if isinstance(hardware_name, str) and isinstance(user_hash, str):
            Core.sendWebSocketCommand({"customMatch_KickPlayer": {"targetHardwareName": hardware_name, "targetNucleusHash": user_hash}})
        else:
            raise ValueError(f"[customMatch_KickPlayer] One or more of the following values are invaild:\n   [customMatch_KickPlayer] hardware_name expects str value\n   [customMatch_KickPlayer] user_hash expects str value")

    async def getSettings():
        """
        # Get Custom Match Settings

        Get current custom match settings.

        ## Example

        ```python
        await LiveApex.Lobby.getSettings()
        ```
        """

        Core.sendWebSocketCommand({"customMatch_GetSettings": {}})

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
            Core.sendWebSocketCommand({"customMatch_SetSettings": {"playlistName": playlist_name, "adminChat": admin_chat, "teamRename": team_rename, "selfAssign": self_assign, "aimAssist": aim_assist, "anonMode": anon_mode}})
        else:
            raise ValueError(f"[customMatch_SetSettings] One or more of the following values are invaild:\n   [customMatch_SetSettings] playlist_name expects str value\n   [customMatch_SetSettings] admin_chat expects bool value\n   [customMatch_SetSettings] team_rename expects bool value\n   [customMatch_SetSettings] self_assign expects bool value\n   [customMatch_SetSettings] aim_assist expects bool value\n   [customMatch_SetSettings] anon_mode expects bool value")

    async def setLegendBan(bans):
        """
        # Set Legend Bans

        Set legend bans for the lobby.

        ## Parameters

        :bans: (list[str]) A list of legend names to ban, all list items must be str. Or an empty list to reset bans.

        ## Example

        ```python
        await LiveApex.Lobby.setLegendBan(['wraith', 'madmaggie']) # bans wraith and mad maggie
        await LiveApex.Lobby.setLegendBan([]) # resets bans
        ```
        """

        scan = 0
        if isinstance(bans, list):
            for i in bans: # Check if each item is a str
                if isinstance(i, str): pass
                else: scan +=1

            if scan == 0: # If all items are str -> send to websocket
                Core.sendWebSocketCommand({"customMatch_SetLegendBan": {"legendRefs": ''.join(bans)}})
            else:
                raise ValueError(f"[customMatch_SetLegendBan] bans expects all list values to be str")
        else:
            raise ValueError(f"[customMatch_SetLegendBan] bans expects list value")

    async def getLegendBans():
        """
        # Get Legend Bans

        Get list of current legend bans.

        ## Example

        ```python
        await LiveApex.Lobby.getLegendBans()
        ```
        """

        Core.sendWebSocketCommand({"customMatch_GetLegendBanStatus": {}})

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
            Core.sendWebSocketCommand({"customMatch_SetMatchmaking": {"enabled": status}})
        else:
            raise ValueError(f"[customMatch_SetMatchmaking] status expects bool value")

    async def setDropLocation(team_id, drop_location):
        """
        # Set Drop Location

        Define a drop location of a specified team.

        ## Parameters

        :team_id: (int) The ID of the team. team_id=0 is unassigned, team_id=1 is observer, team_id=2 is team 1 and so on.
        :drop_location: (int) The POI ID of any POI (this is the same system as the @XX that can also be used to set drop locations).

        ## Example

        ```python
        await LiveApex.Lobby.setDropLocation(2, 20)
        ```
        """

        if isinstance(team_id, int) and isinstance(drop_location, int):
            Core.sendWebSocketCommand({"customMatch_SetSpawnPoint": {"teamId": team_id, "spawnPoint": drop_location}})
        else:
            raise ValueError(f"[customMatch_SetSpawnPoint] One or more of the following values are invaild:\n   [customMatch_SetSpawnPoint] team_id expects int value\n   [customMatch_SetSpawnPoint] drop_location expects int value")