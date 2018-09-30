print("Scrapping Mode ON")

import websocket

if __name__ == "__main__":
    ws = websocket.WebSocketApp('wss://api.bitfinex.com/ws/2')
    ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBTCUSD"}')
    ws.on_message = lambda self, evt:  print (evt)
