## 1. Manual Code Review

### Architecture and Design

| **Aspect**                            | **Status**    | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Protocol Implementation Adherence** | ❌ Not Adhered | The codebase is extremely disorganized, containing remnants from previous iterations that do not integrate with the actual application. Critical components of the OLAF/Neighbourhood protocol are missing or incorrectly implemented. For instance, fingerprints are not correctly encoded, which is vital for user identification as per the protocol. Public chats do not function, and the chat system is largely non-operational. The absence of a proper README makes it difficult to set up and use the application, hindering any attempts to verify protocol adherence effectively. Hardcoded addresses and ports limit testing to a single server and client, preventing the evaluation of multi-server communication as required by the protocol. Overall, the code fails to implement the essential features specified in the protocol documentation.<br><br>This section is bad. rewrite it. It needs to completely focus on protocol adherance. Review the code, and review the protocol. Clearly and concisely outline the differences. You may mention that the conflicting code written / rewritten over and over has clearly affected this. |
| **Security Measures**                 | ❌ Inadequate  | Remove this row and move it all to security specific checks. <br><br>Specifically mention the issues with crypto library and if it follows the protocol. Mention the use of message parsing and the use of find. for instance using find on public message could false interepet a theorertical private message as public and broadcast it to everyone in the neighborhood. mention the deprecated pycrypto library. Please review the code and stop spouting made up shit that sounds correct.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Code Quality

| **Aspect**                       | **Status**           | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Readability and Organization** | ⚠️ Poor Organization | The codebase is disorganized and difficult to navigate. It contains code from previous iterations that are not relevant to the current implementation, leading to confusion. There is a lack of modularization, and functions are not well-separated or documented. The absence of a README or documentation makes it challenging to understand how to set up and run the application. Hardcoded addresses and ports are scattered throughout the code, making it inflexible and hard to configure for different environments. Overall, the code lacks structure and clarity, impeding maintainability and scalability. |
| **Error Handling and Logging**   | ⚠️ Inadequate        | Error handling is insufficient and inconsistent. The application will almost **certainly** crash when unexpected inputs are provided or when network errors occur, without graceful recovery or informative error messages. Logging is minimal, relying primarily on print statements that are not systematically used throughout the code. This makes debugging and monitoring the application difficult. Critical errors are not properly caught, and exceptions can lead to the application terminating unexpectedly, which poses reliability and security concerns.                                                 |

### Security-specific Checks

| **Aspect**                               | **Status**                 | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Input Validation**                     | ❌ Insufficient             | There is minimal input validation across the application. User inputs are not properly sanitized or validated, increasing the risk of injection attacks and crashes due to unexpected inputs. The code assumes well-formed inputs, which is not safe in a production environment. For example, message parsing relies on specific formats, and deviations can cause the application to fail or behave unpredictably. The method of parsing commands by searching for substrings (e.g., using `find` within a message string) is particularly dangerous, as it can be easily manipulated by crafted inputs, leading to unintended behaviors.                                                                                                                                                                                                                                    |
| **Access Control**                       | ❌ Missing                  | The application lacks proper access control mechanisms. Any user can connect to the server without authentication, and there are no checks to prevent unauthorized actions. This opens up the application to potential abuse, where malicious users could send arbitrary messages or commands. The absence of authentication and authorization controls is a critical security flaw that needs to be addressed. Additionally, multiple clients can connect using the same public key, which should not be permitted, as it undermines the ability to uniquely identify and authenticate users.                                                                                                                                                                                                                                                                                 |
| **Cryptographic Implementations**        | ❌ Incorrect Implementation | The cryptographic implementations are incorrect and do not comply with the protocol specifications. The fingerprints are not correctly calculated, as they are not properly base64-encoded SHA-256 hashes of the public keys. Instead, they appear to be excerpts of the PEM keys. The code uses outdated and insecure cryptographic libraries (e.g., PyCrypto, which is deprecated) instead of recommended ones like PyCA's cryptography library. This raises concerns about the security and integrity of the cryptographic operations performed by the application. Furthermore, the encryption and decryption processes are not properly implemented, leading to non-functional or insecure communication.<br><br>Wrong. PLEASE REVIEW THE CODE. THE PEM STUFF IS ONLY FOR CLIENT UPDATES, YOU DONT KNOW IF ITS FOR THE ENTIRE THING IF YOU DONT ACTUALLY REVIEW THE CODE. |
| **Secure Data Storage and Transmission** | ❌ Insecure Transmission    | Data transmission is insecure due to the use of hardcoded addresses and ports, which cannot be easily configured for secure channels. The application does not use TLS or any form of transport layer security, leaving the data susceptible to interception. Additionally, public chats are not operational, and when attempted, they do not function correctly, indicating issues with data handling and transmission. The lack of secure communication protocols undermines the confidentiality and integrity of the data exchanged between clients and the server. Private chats have not been implemented.                                                                                                                                                                                                                                                                |

## 2. Static Analysis

The static analysis was performed using **Bandit**, a security-oriented static analysis tool for Python. Below are the findings from the analysis:

### `client.py`

| **Issue ID** | **Severity** | **Confidence** | **Location** | **Description**                                                                                                                                                      | **Recommendation**                                                                                     | **More Info**                                                                                          |
| ------------ | ------------ | -------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| B413         | High         | High           | client.py:14 | The `pyCrypto` library and its module `AES` are deprecated and no longer maintained. Using deprecated libraries can introduce security vulnerabilities.              | Replace `pyCrypto` with a maintained library such as `pyca/cryptography` for cryptographic operations. | [Link](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b413-import-pycrypto) |


### `server.py`

No issues identified.

## 3. Dynamic Analysis

### Testing Environment Setup

Due to the lack of documentation and absence of a README file, setting up the testing environment was challenging. The code base contains many files and seemingly a sub folder containing an entire previous iteration. This made it extremely difficult to figure out how to actually run the application and where to start. After contacting group members, I was informed that only client.py and server.py were needed to run the application. This was of course appreciated, but stuff like this needs to be clear in documentation. 


Moreover, the hardcoded addresses and ports limit the ability to test the application in a multi-server or multi-client setup. After inspecting the code, the reviewer attempted to run the `server.py` and `client.py` files to evaluate the application's functionality.

### Functional Testing Observations

| **Aspect**                              | **Observation**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Application Setup**                   | The instructions for setting up and running the application are not provided. The reviewer had to contact the group members for guidance, but received insufficient information. Consequently, assumptions were made based on the code to attempt running the application.                                                                                                                                                                                                                                          |
| **Hardcoded Addresses and Ports**       | The application uses hardcoded addresses and ports (`127.0.0.1:8080`), which restricts testing to a single server and client. This limitation prevents testing of the application's behavior in a distributed environment, which is essential for the OLAF/Neighbourhood protocol that involves multiple servers and clients.                                                                                                                                                                                         |
| **Client Update Handling**              | Sending a client update manually from the client causes the application to crash. The client and server output the following errors:                                                                                                                                                                                                                                                                                                                                                                               |

Client Output:

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
```

Server Output:

```
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

| **Multiple Clients with Same Public Key** | The application allows multiple clients to connect to the same server using the same public key. This should not be permitted, as each client should have a unique key pair to ensure proper identification and secure communication. The server output indicates that two users with the same public key are added to the local and global user lists. |

Server Output:

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

| **Incorrect Fingerprint Encoding**        | The fingerprints are not correctly encoded. Instead of being base64-encoded SHA-256 hashes of the public keys, they appear to be excerpts of the PEM keys. This deviates from the protocol specification and can lead to identification issues.                                                                                                                                                                                                                                                                        |
| **Incomplete Client Update List**         | The client update list only shows the "key" of one connected client, even when multiple clients are connected. This indicates a problem with the synchronization of client states across the server and clients. |

![[Pasted image 20241009083709.png]]

| **Public Chats Non-functional**           | Public chats do not work as intended. Attempting to send a public chat results in errors or no action at all. This feature is crucial for the application's functionality as per the protocol. |

![[Pasted image 20241009083857.png]]

| **Exit Command Handling**                 | The `/exit` command works on the client side, closing the client application. However, the server does not recognize the client's disconnection or send out any updates to other clients or servers. This lack of communication about client disconnections can lead to inconsistent client lists and stale state information across the network. |

![[Pasted image 20241009083942.png]]

| **Error Handling on Shutdown**            | The application does not handle non-graceful shutdowns properly. If a client or server terminates unexpectedly, the other side does not handle the exception gracefully, leading to unhandled exceptions and potential crashes. |

![[Pasted image 20241009084023.png]]

| **Message Parsing Vulnerability**         | The method of parsing commands by searching for substrings (e.g., using `find` within a message string) is dangerous. If a user includes certain keywords (e.g., "public:") in their message, it can trigger unintended behaviors, such as broadcasting a private message publicly. This represents a significant security and privacy concern. |

### Summary of Dynamic Analysis

The dynamic analysis reveals that the application is largely non-functional and does not adhere to the expected behavior as defined by the OLAF/Neighbourhood protocol. Critical features such as public chats, client updates, and proper handling of client connections are either broken or not implemented correctly. The lack of proper error handling and input validation leads to crashes and inconsistent states, making the application unreliable and insecure for practical use.










































































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