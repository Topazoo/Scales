#! /usr/bin/env python

from Backend.App_Server import App_Server
from Backend.Socket_Server import Socket_Server
    
if __name__ == '__main__':
    Socket_Server().run()
    App_Server.run(debug = True)
