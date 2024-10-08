## 1. Project Overview

- **Group Members:**
  - Bradley Hill
  - James Nguyen
  - Natanand Akomsoontorn
  - Vincent Scaffidi-Muta

- **Reviewers:**
  - Samuel Chau

---

## 2. Manual Code Review

### Architecture and Design

#### Protocol Implementation Adherence

| **Aspect**                        | **Status**             | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Protocol implementation adherence | ✅ **Adhered**          | The implementation closely follows the OLAF/Neighbourhood protocol v1.1.3. Key protocol features such as message types (`hello`, `chat`, `public_chat`, `client_list_request`, `client_update`), message signing, encryption, and proper routing through servers are correctly implemented. The client and server handle message signing, encryption, and decryption according to the protocol specifications. The network topology is respected, and messages are routed appropriately through the home server and neighboring servers. |

#### Security Measures (Encryption, Authentication, etc.)

| **Aspect**          | **Status**                | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Encryption          | ✅ **Implemented Correctly** | The code utilizes RSA for asymmetric encryption and signing, and AES in CBC mode for symmetric encryption. Keys are generated securely using appropriate key sizes (2048 bits for RSA, 256 bits for AES). Messages are encrypted end-to-end, and symmetric keys are exchanged securely using RSA encryption.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Authentication      | ✅ **Implemented**         | Clients authenticate with the server by sending a signed `hello` message containing their public key. The server verifies the signature and establishes the client's identity. Message counters are used to prevent replay attacks, ensuring that each message has a unique counter value that is greater than the previous one from the same sender.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Message Integrity   | ✅ **Ensured**             | Messages are signed using RSA signatures, and signatures are verified upon receipt to ensure that the message has not been tampered with. The use of message counters adds an additional layer of integrity and helps prevent replay attacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Confidentiality     | ✅ **Maintained**          | Messages are encrypted using AES symmetric encryption, with keys securely exchanged using RSA asymmetric encryption. This ensures that only intended recipients can decrypt and read the messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Key Management      | ✅ **Properly Handled**    | RSA key pairs are generated for each client and server. Public keys are exchanged and stored securely. Fingerprints of public keys are computed using SHA-256 and Base64 encoding, as specified in the protocol, and used for identifying clients. Symmetric AES keys are generated per message and encrypted with recipients' public keys.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Secure Transmission | ⚠️ **Partially Implemented**  | While message contents are encrypted, the communication channels (sockets) are not secured using TLS/SSL. Communication occurs over plain TCP sockets, which could expose metadata (e.g., IP addresses, ports) and be susceptible to interception. Implementing TLS/SSL for socket communication would enhance security by encrypting the transport layer and protecting against man-in-the-middle attacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Error Handling      | ⚠️ **Needs Improvement**    | Error handling is present but could be improved. Exceptions are caught and printed to the console, but the program could benefit from more robust error handling mechanisms. For example, adding try-except blocks where exceptions might occur, and providing user-friendly error messages or proper logging for debugging purposes. In some cases, exceptions are printed but not handled, which could lead to unexpected behavior or crashes.                                                                                                                                                                                                                                                                                                                                                                                                                    |

---

### Code Quality

#### Readability and Organization

| **Aspect**                | **Status**               | **Comments**                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Readability and Organization | ✅ **Well Organized**     | The code is structured in a clear and logical manner. Functions and classes are appropriately used to encapsulate functionality. Variable and function names are descriptive and follow consistent naming conventions. The separation of concerns between the client and server code is well-maintained, enhancing readability and maintainability.                                                       |
| Comments and Documentation   | ⚠️ **Moderate**           | While the code includes some comments and documentation, there are areas where additional comments would enhance understanding, especially in complex sections like encryption/decryption processes and message handling. Adding docstrings to functions and more inline comments would aid future developers or reviewers in comprehending the codebase more effectively.                                      |
| Dependency Management        | ✅ **Adequate**           | The required dependencies are clearly listed in the "Dependencies" section of the code comments. Installation instructions are provided in the README, ensuring that users can set up the environment correctly. The code checks for necessary modules and handles imports appropriately.                                                                             |
| Code Formatting              | ✅ **Consistent**         | The code follows consistent formatting practices, with proper indentation and spacing, making it easy to read.                                                                                                                                                                                                                                                    |

#### Error Handling and Logging

| **Aspect**         | **Status**               | **Comments**                                                                                                                                                                                                                                                                                                                |
|--------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Error Handling     | ⚠️ **Needs Improvement** | Error handling is basic, with exceptions often caught and printed without further action. In some cases, exceptions are not caught at all, which could cause the application to crash unexpectedly. Implementing more comprehensive error handling, including specific exception types and graceful recovery mechanisms, would enhance stability. |
| Logging            | ⚠️ **Basic**              | The code uses `print` statements for logging, which is acceptable for development but not ideal for production environments. Implementing a logging framework using Python's `logging` module would provide better control over log levels and allow logging to different outputs (console, file, etc.) as needed.              |

---

### Security-specific Checks

#### Input Validation

| **Aspect**           | **Status**                | **Comments**                                                                                                                                                                                                                                                                                                                               |
|----------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input Validation     | ⚠️ **Limited**            | Input validation is minimal. The code assumes that incoming messages are correctly formatted and does not thoroughly validate the structure or content before processing. This could lead to exceptions or vulnerabilities if malformed or malicious data is received. Implementing strict input validation would improve security and robustness. |

#### Access Control

| **Aspect**           | **Status**                | **Comments**                                                                                                                                                                                                                                                                                                                                |
|----------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access Control       | ⚠️ **Basic**              | Access control is based on public key verification and message signatures. However, there are no roles or permissions implemented beyond this. All authenticated users have the same level of access. Introducing role-based access control or permissions could be beneficial if the application is expanded with additional features.          |

#### Cryptographic Implementations

| **Aspect**                 | **Status**                  | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RSA Key Generation         | ✅ **Correct**               | RSA keys are generated using a key size of 2048 bits and a public exponent of 65537, as recommended.                                                                                                                                                                                                                                                                                                                                                      |
| AES Encryption             | ⚠️ **Uses CBC Mode Instead of GCM** | The code uses AES in CBC mode for symmetric encryption, whereas the protocol specifies AES in GCM mode. AES-GCM provides authenticated encryption with associated data (AEAD), offering both confidentiality and integrity. Using CBC mode without additional integrity checks (e.g., HMAC) could make the system vulnerable to certain attacks, such as padding oracle attacks. It is recommended to update the code to use AES-GCM as specified in the protocol. |
| RSA Signature Scheme       | ⚠️ **Uses PKCS1v15 Instead of PSS** | The code uses RSA with PKCS1v15 padding for signatures, while the protocol specifies RSA-PSS with SHA-256 and a salt length of 32 bytes. RSA-PSS is more secure and recommended for new applications. Updating the signature scheme to use RSA-PSS would enhance security by providing probabilistic signatures that are less susceptible to forgery.                                                              |
| Hashing Algorithms         | ✅ **SHA-256 Used**           | The code correctly uses SHA-256 for hashing operations, consistent with the protocol specifications.                                                                                                                                                                                                                                                                                                                                                      |
| Key Exchange and Management | ✅ **Properly Handled**       | Symmetric AES keys are generated per message and securely exchanged by encrypting them with recipients' RSA public keys. The handling of multiple recipients in group messages is correctly implemented, ensuring that each recipient receives the encrypted AES key intended for them.                                                                                                                               |

#### Secure Data Storage and Transmission

| **Aspect**              | **Status**               | **Comments**                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Secure Data Storage     | ✅ **Adequate**           | Private keys are stored securely within the application's memory during runtime and are not written to disk or exposed. Sensitive data such as decrypted messages and keys are handled appropriately and not logged or displayed unnecessarily.                                                                                                                                                               |
| Secure Transmission     | ⚠️ **Needs Improvement** | While messages are encrypted end-to-end, the communication channels (sockets) are not secured using TLS/SSL. Implementing secure sockets (e.g., using `ssl` module in Python) would protect against potential man-in-the-middle attacks and ensure that all communication, including metadata and headers, is encrypted.                                                                                         |

---

## 3. Static Analysis

- **Tool(s) used:** Bandit (version X.X.X)

### Key Findings:

#### Potential Vulnerabilities:

| **Issue ID** | **Severity** | **Confidence** | **Location**      | **Description**                                                                                                                                                    | **Recommendation**                                                                                                                                                                               | **More Info**                                                                                   |
|--------------|--------------|----------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| B201         | High         | Medium         | `server.py:429`   | A Flask app appears to be run with `debug=True`, which exposes the Werkzeug debugger and allows the execution of arbitrary code.                                    | Disable debug mode in production by setting `debug=False` when running the Flask app. This prevents the exposure of the interactive debugger to end-users and mitigates potential security risks. | [Bandit B201 - Flask Debug Mode](https://bandit.readthedocs.io/en/latest/plugins/b201_flask_debug_true.html) |

#### Code Quality Issues:

- **Use of `print` Statements for Logging:**
  - **Description:** The code extensively uses `print` statements for logging and debugging purposes.
  - **Recommendation:** Replace `print` statements with Python's `logging` module to provide better control over log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) and allow logging to different outputs (console, files, etc.). This change enhances maintainability and allows easier debugging in different environments.

#### Security Misconfigurations:

- **Flask Debug Mode Enabled:**
  - **Description:** The Flask application in `server.py` is run with `debug=True`, which is not recommended for production environments.
  - **Recommendation:** Set `debug=False` when deploying the application. Debug mode should only be used during development.

---

## 4. Dynamic Analysis

Since the dynamic analysis is not to be filled in yet, here are suggestions on what you can do for this section:

- **Testing Environment Setup:**
  - Set up multiple server instances on different ports to simulate the neighborhood network topology.
  - Run clients connected to different servers to test inter-server communication.
  - Use virtual machines or Docker containers to simulate different network environments if necessary.

- **Functional Testing:**
  - **Message Sending and Receiving:**
    - Test private messaging between clients connected to the same server and different servers.
    - Test group messaging functionality, ensuring that messages are correctly delivered to all intended recipients.
    - Verify public messaging and ensure that all clients receive public messages regardless of their connected server.

  - **File Transfer:**
    - Test file uploads and downloads using the provided Flask API endpoints.
    - Ensure that files are correctly saved and retrieved, and that unauthorized access to files is prevented.

  - **Client List Retrieval:**
    - Test the `client_list_request` functionality to ensure clients receive accurate and up-to-date lists of connected clients across servers.

  - **Edge Cases and Error Conditions:**
    - Test behavior when clients disconnect unexpectedly.
    - Verify that the system handles network interruptions gracefully.
    - Check how the application behaves when invalid or malformed messages are received.

- **Security Testing:**
  - **Network Traffic Analysis:**
    - Use tools like Wireshark or tcpdump to capture and analyze network traffic.
    - Confirm that message contents are encrypted and that no sensitive data is transmitted in plaintext.
    - Verify that message signatures and encryption prevent unauthorized reading or tampering.

  - **Penetration Testing Attempts:**
    - **Replay Attacks:**
      - Attempt to resend captured messages with the same counter value and observe if the system correctly rejects them.
    - **Man-in-the-Middle Attacks:**
      - Try intercepting and modifying messages between clients and servers to see if tampering is detected.
    - **Injection Attacks:**
      - Send malformed or malicious data to test input validation and error handling.

  - **Fuzz Testing:**
    - Use fuzzing tools to send random or unexpected inputs to the server and clients.
    - Observe if the application crashes or behaves unexpectedly, indicating potential vulnerabilities.

- **Performance Testing:**
  - Assess how the application performs under load with multiple clients sending messages simultaneously.
  - Monitor resource usage (CPU, memory) to identify potential bottlenecks.

By conducting these tests, you will gain insights into the application's robustness, security posture, and areas that may require improvement. Document your findings, including any issues discovered and steps taken to reproduce and address them, in the dynamic analysis section.

---

[Please proceed to conduct the dynamic analysis based on the above suggestions. Once completed, we can work together to fill in the remaining sections, including the results summary and recommendations.]