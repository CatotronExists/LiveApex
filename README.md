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

## Protobuf Generated File
events_pb2.py (Located in LiveApex) is generated from protoc using the .proto file located in the Apex Legends LiveAPI directory.\
`(steamapps/common/Apex Legends/LiveAPI/events.proto)`

This file will be regenerated each time the LiveAPI is updated!

## Versioning
LiveApex version is v0.3.0. LiveAPI version is v2.3