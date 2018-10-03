print("Scrapping Mode ON")

from websocket import create_connection
ws = create_connection("wss://api.bitfinex.com/ws/2")
print("Sending 'Hello, World'...")
ws.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBTCUSD"}')
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
#ws.send()
result =  ws.recv()
print("Received '%s'" % result)
result =  ws.recv()
print("Received '%s'" % result)
ws.close()

"""
import websocket

if __name__ == "__main__":
    ws = websocket.WebSocketApp('wss://api.bitfinex.com/ws/2')
    ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBTCUSD"}')
    event=ws.on_open(ws);
    ws.on_message = lambda self, evt:  print (evt)
    ws.on_message(ws,event);
"""