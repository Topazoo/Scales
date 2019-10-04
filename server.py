#! /usr/bin/env python

from backend.Server.App import App_Server
from backend.Server.Load_Cell_Socket import Load_Cell_Socket
    
if __name__ == '__main__':
    Load_Cell_Socket().run()
    App_Server.run(debug = True)
