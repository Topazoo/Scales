#! /usr/bin/env python
if __name__ == '__main__':
    from Drivers.Stream_Socket_Driver import Socket_Stream_Server
    from Drivers.Load_Cell_Driver import Dummy_Load_Cell
else:
    from Load_Cell_WebSocket.Drivers.Stream_Socket_Driver import Socket_Stream_Server
    from Load_Cell_WebSocket.Drivers.Load_Cell_Driver import Dummy_Load_Cell

class Load_Cell_Socket(Socket_Stream_Server):
    '''
        "Advantageous" WebSocket streaming server that constantly streams data from a 
        passed generator and attempts to read streamed data from the client
        in the same loop. * Use .run() to start the server *

        --> [str] path - The URL to broadcast the socket server (e.g. '127.0.0.1')\n
        --> [int] port - The port to broadcast the socket server (e.g. 5001)\n
        --> [callable] generator - The generator function that supplies values to be
                                   streamed to the client.\n
        --> [callable] callback - A function to call if data is received from the client.\n
        --> [bool] daemon - Runs the socket as a daemon (In the background but cleaned when the script completes).
    '''

    def __init__(self, path:str = '127.0.0.1', port:int = 5001, generator:callable = None, callback:callable = None, daemon:bool=False):
        self.path = path
        self.port = port
        self.load_cell = Dummy_Load_Cell()

        if not callback:
            callback = self.client

        if not generator:
            generator = self.load_cell.read_weight

        super().__init__(path, port, generator, callback, daemon)
        
    def set_callback(self, callback:callable):
        this.callback = callback

    def client(self, socket_request):
        action = socket_request['action']

        if action:
            if action == 'connect':
                self.load_cell.connect()

if __name__ == '__main__':
    websocket_server = Load_Cell_Socket()
    websocket_server.run()

    print(' * Started Load Cell Websocket Server !')
    print('    * Path: {}'.format(websocket_server.path))
    print('    * Port: {}'.format(websocket_server.port))
