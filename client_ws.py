# -*- coding: utf-8 -*-

# pip install websocket-client


from websocket import create_connection
ws = create_connection("ws://127.0.0.1:8000/ws/chat")
print("Sending 'Hello, World'...")
ws.send("Hello, World 2")

print("Close")

# ws.close()
