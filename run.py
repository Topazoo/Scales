#! /usr/bin/env python

from Application.Server import Application
from Load_Cell_WebSocket.Socket_Server import Load_Cell_Socket
    
if __name__ == '__main__':
    Load_Cell_Socket().run()
    Application.run()
