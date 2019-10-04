#! /usr/bin/env python

from Application.Server import Application
from Load_Cell_WebSocket.Socket_Server import Load_Cell_Socket
    
if __name__ == '__main__':
    websocket_server = Load_Cell_Socket(daemon=True)
    websocket_server.run()
    
    print(' * Started Load Cell Websocket Server !')
    print('    * Path: {}'.format(websocket_server.path))
    print('    * Port: {}'.format(websocket_server.port))

    Application.run()
