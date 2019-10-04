#! /usr/bin/env python

from backend.Drivers.Stream_Socket_Driver import Socket_Stream_Server
from backend.Drivers.Load_Cell_Driver import Dummy_Load_Cell

class Load_Cell_Socket(Socket_Stream_Server):
    '''
        "Advantageous" WebSocket streaming server that constantly streams data from a 
        passed generator and attempts to read streamed data from the client
        in the same loop. * Use .run() to start the server *

        --> [str] path - The URL to broadcast the socket server (e.g. '127.0.0.1')\n
        --> [int] port - The port to broadcast the socket server (e.g. 5001)\n
        --> [callable] generator - The generator function that supplies values to be
                                   streamed to the client.\n
        --> [callable] callback - A function to call if data is received from the client.
    '''

    def __init__(self, path:str = '127.0.0.1', port:int = 5001, generator:callable = None, callback:callable = None):
        self.load_cell = Dummy_Load_Cell()

        if not callback:
            callback = self.client

        if not generator:
            generator = self.load_cell.read_weight

        super().__init__(path, port, generator, callback)
        

    def set_callback(self, callback:callable):
        this.callback = callback

    def client(self, socket_request):
        print(socket_request)
        action = socket_request['action']

        if action:
            if action == 'connect':
                self.load_cell.connect()

        print(action)
