# LiveApex
A Python library that handles the connection between a websocket and the game client

## Setup
```pip install LiveApex```

Requires Python 3.12 or higher

Include one set of the following in your launch options for Apex Legends:\
To Use Protobuf (Recommended): ```+cl_liveapi_enabled 1 +cl_liveapi_ws_servers "ws://127.0.0.1:7777"```\
To Use JSON (Legacy): ```+cl_liveapi_enabled 1 +cl_liveapi_ws_servers "ws://127.0.0.1:7777" +cl_liveapi_use_protobuf 0```

## Docs
All LiveAPIEvents, possible responses and functions are documented in the [wiki tab](https://github.com/CatotronExists/LiveApex/wiki).

## Protobuf Generated File
events_pb2.py (Located in LiveApex) is generated from protoc using the .proto file located in the Apex Legends LiveAPI directory.\
`(steamapps/common/Apex Legends/LiveAPI/events.proto)`

This file will be regenerated each time the LiveAPI is updated!

## Limitations
The LiveAPI is only avaliable in custom games, this will not work for public or ranked games.\
Some functions will only work in lobby codes provided by EA/Respawn.

## Versioning
LiveApex version is v2.0.0-WIP. LiveAPI version is v2.4 (Season 28: Breach | Split 1)

## Disclaimer
I am not responsible for any missuse of the Apex Legends LiveAPI, use this library responsibly, at your own risk.