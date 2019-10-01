#! /usr/bin/env python

import asyncio, websockets, threading, json, random

class Socket_Server():
    def __init__(self, path='127.0.0.1', port=5001, generator=None):
        self.event_loop = asyncio.get_event_loop()
        self.socket_server = websockets.serve(self.send_message, path, port)
        self.generator = generator if generator else self.sample_generator

    def run_socket(self):
        try:
            self.event_loop.run_until_complete(self.socket_server)
            self.event_loop.run_forever()
        except Exception as e:
            pass

    def run(self):
        t = threading.Thread(target=self.run_socket)
        t.daemon = True
        t.start()

    async def send_message(self, websocket, path):
        for data in self.generator():
            await websocket.send(json.dumps(data))

    def sample_generator(self):
        while True:
            yield random.choice([{'data': 'Hello'}, {'data': 'World'}])
