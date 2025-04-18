# LiveApex Dev Branch
Dev versions are unfinshed and untested

## Setup
*Due to the Dev Branch being on TestPyPI each package has to be downloaded seperatly!*

### Requirements
Python 3.6 or higher

### Installing Websockets
```pip install websockets==12.0```

### Installing Protobuf
```pip install protobuf==6.30.1```

### Installing Library
```pip install -i https://test.pypi.org/simple/ LiveApex```\
...and thats it!

## Docs
All LiveAPIEvents, possible responses and functions are documented in the [wiki tab](https://github.com/CatotronExists/LiveApex/wiki)

## Protobuf Generated File
events_pb2.py (Located in LiveApex) is generated from protoc using the .proto file located in the Apex Legends LiveAPI directory.\
`(steamapps/common/Apex Legends/LiveAPI/events.proto)`

This file will be regenerated each time the LiveAPI is updated!

## Limitations
The LiveAPI is only avaliable in custom games, this will not work for public or ranked games.\
Some functions will only work in HP lobbies (provided by EA/Respawn).

## Versioning
LiveApex version is v0.5.0. LiveAPI version is v2.3\
This library will keep removed/deprecated functions for 2 seasons after they are removed from the LiveAPI. This is to allow for example data to not be outated as quickly.

## Disclaimer
I am not responsible for any missuse of the Apex Legends LiveAPI, use this library responsibly, at your own risk.