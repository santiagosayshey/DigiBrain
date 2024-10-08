










































































static analysis
- bandit results

/SEP-server_final-1/SEP-server_final ] $ bandit -r client.py
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.12.3
[node_visitor]  INFO    Unable to find qualified name for module: client.py
Run started:2024-10-08 22:12:37.899124

Test results:
>> Issue: [B413:blacklist] The pyCrypto library and its module AES are no longer actively maintained and have been deprecated. Consider using pyca/cryptography library.
   Severity: High   Confidence: High
   Location: client.py:14
   More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b413-import-pycrypto
13      from cryptography.hazmat.primitives import serialization, hashes
14      from Crypto.Cipher import AES
15      from Crypto.Random import get_random_bytes

--------------------------------------------------
>> Issue: [B413:blacklist] The pyCrypto library and its module get_random_bytes are no longer actively maintained and have been deprecated. Consider using pyca/cryptography library.
   Severity: High   Confidence: High
   Location: client.py:15
   More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b413-import-pycrypto
14      from Crypto.Cipher import AES
15      from Crypto.Random import get_random_bytes
16
17      SERVER_ADDR = "127.0.0.1:8080"

--------------------------------------------------

Code scanned:
        Total lines of code: 247
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 2.0
        Total issues (by confidence):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 2.0
Files skipped (0):
(myenv) [ 1 08:42:37 sam-chau ~/Documents/OMesh/Venkata Vishnubhatla/SEP-server_final-1/SEP-server_final ] $ bandit -r server.py
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.12.3
[node_visitor]  INFO    Unable to find qualified name for module: server.py
Run started:2024-10-08 22:12:44.292452

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 217
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
        Total issues (by confidence):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
Files skipped (0):
(myenv) [ 0 08:42:44 sam-chau ~/Documents/OMesh/Venkata Vishnubhatla/SEP-server_final-1/SEP-server_final ] $ 

dynamic analysis
- instructions arent clear, had to email group just to figure out which files to run
- code written in python and c for some reason
- most of code isnt even used and irrelavant to the actual working code

- ports and addresses hardcoded, which means i can only have 1 server and 1 client
- no readme provided to actually say how to use the program
	- during dynamic analysis making assumptions on how it works by reading code, may or may not be correct

- client update breaks when sent manually

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

- seems that connecting two clients to the same server is possible even if they have the same public key?
  
```
User added. Total Users in Local List: 2
Global User List Size : 0
User added. Total Users in Global List: 1
Global User List Size : 1
Global User List Size : 1
Global User List Size : 0
User added. Total Users in Global List: 1
Global User List Size : 1
Global User List Size : 1
```

- fingerprints are encoded wrong, this is not base 64. looks like an excerpt of the PEM key
- client update list only shows "key" of 1 connected client, not both

![[Pasted image 20241009083709.png]]

- public chats do not work

![[Pasted image 20241009083857.png]]

- /exit seems to work client side, but server does not recognise this or send out any updates

![[Pasted image 20241009083942.png]]

- error handling does not handle non graceful shutdowns

![[Pasted image 20241009084023.png]]

- chat system is completely broken. There needs to be a better way of selecting options. Using find within a message string is extremely dangerous. What if someone had "public:" in their private message to someone? this would broadcast their private message to everybody