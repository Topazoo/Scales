#! /usr/bin/env python

import asyncio, websockets, threading, json, random

class Socket_Stream_Server():
    '''
        "Advantageous" WebSocket streaming server that constantly streams data from a 
        passed generator and attempts to read streamed data from the client
        in the same loop. * Use .run() to start the server *

        --> [str] path - The URL to broadcast the socket server (e.g. '127.0.0.1')\n
        --> [int] port - The port to broadcast the socket server (e.g. 5001)\n
        --> [callable] generator - The generator function that supplies values to be
                                   streamed to the client.\n
        --> [callable] callback - A function to call if data is received from the client.
        --> [bool] daemon - Runs the socket as a daemon (In the background but cleaned when the script completes)
    '''

    def __init__(self, path:str = '127.0.0.1', port:int = 5001, generator:callable = None, callback:callable = None, daemon:bool=False):
        self.daemon = daemon
        self.event_loop = asyncio.get_event_loop()
        self.socket_server = websockets.serve(self.send, path, port)
        self.generator = generator if generator else self.sample_generator
        self.callback = callback

    def run_socket(self):
        ''' 
            Run the socket server indefinitely using asyncio to prevent blocking while waiting for
            data to be sent or read. * Don't call directly, use run() *
        '''

        try:
            self.event_loop.run_until_complete(self.socket_server)
            self.event_loop.run_forever()
        except Exception as e:
            pass

    def run(self):
        '''
            Run the entire server on a thread to ensure it doesn't block other 
            running Python servers (like Flask) that could be running with the socket
            server.
        '''

        t = threading.Thread(target=self.run_socket)
        t.daemon = self.daemon                                 # Allows Keyboard Interrupts
        t.start()

    async def send(self, websocket, path):
        '''
            Send data from the generator to the client and simultaneously check for 
            data from the client.
        '''

        for data in self.generator():
            await websocket.send(json.dumps(data))
            try:
                if self.callback:
                    await asyncio.wait_for(self.receive(websocket), timeout=.0001)
            except Exception as e:
                continue

    async def receive(self, websocket):
        '''
            Call the callback when data is retrieved from the server.
        '''

        data = await websocket.recv()
        if data:
            self.callback(json.loads(data))

    def sample_generator(self):
        '''
            A demo generator.
        '''

        while True:
            yield random.choice([{'data': 'Hello'}, {'data': 'World'}])
