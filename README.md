# LiveApex 
A Python library that handles the connection between a websocket and the game client

## Setup
```pip install LiveApex```

Requires Python 3.12 or higher

Include ```+cl_liveapi_enabled 1 +cl_liveapi_ws_servers "ws://127.0.0.1:7777" +cl_liveapi_use_protobuf 0``` in your steam launch options

## Docs
All LiveAPIEvents, possible responses and functions are documented in the [wiki tab](https://github.com/CatotronExists/LiveApex/wiki)

## Protobuf Generated File
events_pb2.py (Located in LiveApex) is generated from protoc using the .proto file located in the Apex Legends LiveAPI directory.\
`(steamapps/common/Apex Legends/LiveAPI/events.proto)`

This file will be regenerated each time the LiveAPI is updated!

## Limitations
The LiveAPI is only avaliable in custom games, this will not work for public or ranked games.\
Some functions will only work in lobby codes provided by EA/Respawn.

## Versioning
LiveApex version is v1.2.0. LiveAPI version is v2.3\
This library will keep removed/deprecated functions for 2 seasons after they are removed from the LiveAPI. This is to allow for example data to not be outated as quickly.

## Disclaimer
I am not responsible for any missuse of the Apex Legends LiveAPI, use this library responsibly, at your own risk.