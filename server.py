#! /usr/bin/env python

from Backend.Server.App import App_Server
from Backend.Server.Load_Cell_Socket import Load_Cell_Socket
    
if __name__ == '__main__':
    Load_Cell_Socket().run()
    App_Server.run(debug = True)
