dynamic analysis
- instructions arent clear, had to email group just to figure out which files to run
- code written in python and c for some reason
- most of code isnt even used and irrelavant to the actual working code
- no readme provided to actually say how to use the program
- ports and addresses hardcoded, which means i can only have 1 server and 1 client

client update breaks

```
# Client
Enter message: client update:
Enter message: Task exception was never retrieved
future: <Task finished name='Task-5' coro=<receive_messages() done, defined at /home/sam-chau/Documents/OMesh/Venkata Vishnubhatla/SEP-server_final-1/SEP-server_final/client.py:167> exception=ConnectionClosedError(Close(code=1011, reason=''), Close(code=1011, reason=''), True)>
Traceback (most recent call last):
  File "/home/sam-chau/Documents/OMesh/Venkata Vishnubhatla/SEP-server_final-1/SEP-server_final/client.py", line 172, in receive_messages
    response = await websocket.recv()
               ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/sam-chau/Documents/OMesh/Venkata Vishnubhatla/myenv/lib/python3.12/site-packages/websockets/legacy/protocol.py", line 562, in recv
    await self.ensure_open()
  File "/home/sam-chau/Documents/OMesh/Venkata Vishnubhatla/myenv/lib/python3.12/site-packages/websockets/legacy/protocol.py", line 938, in ensure_open
    raise self.connection_closed_exc()
websockets.exceptions.ConnectionClosedError: received 1011 (internal error); then sent 1011 (internal error)

# Server

Traceback (most recent call last):
  File "/home/sam-chau/Documents/OMesh/Venkata Vishnubhatla/myenv/lib/python3.12/site-packages/websockets/legacy/server.py", line 245, in handler
    await self.ws_handler(self)
  File "/home/sam-chau/Documents/OMesh/Venkata Vishnubhatla/SEP-server_final-1/SEP-server_final/server.py", line 325, in websocket_handler
    await handle_message(message, websocket)
  File "/home/sam-chau/Documents/OMesh/Venkata Vishnubhatla/SEP-server_final-1/SEP-server_final/server.py", line 308, in handle_message
    await handle_client_update(data, websocket)
  File "/home/sam-chau/Documents/OMesh/Venkata Vishnubhatla/SEP-server_final-1/SEP-server_final/server.py", line 182, in handle_client_update
    client_keys = data["clients"]
                  ~~~~^^^^^^^^^^^
KeyError: 'clients'

```