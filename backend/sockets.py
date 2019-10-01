#! /usr/bin/env python

import asyncio
import datetime
import random
import websockets
import threading
import json

loop = asyncio.get_event_loop()

async def time(websocket, path):
    while True:
        #now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(json.dumps({'weight': random.random()}))
        await asyncio.sleep(random.random() * 3)

def run_socket(loop):
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(time, '127.0.0.1', 5001)
    loop.run_until_complete(start_server)
    loop.run_forever()

SOCKET = threading.Thread(target=run_socket, args=(loop,))