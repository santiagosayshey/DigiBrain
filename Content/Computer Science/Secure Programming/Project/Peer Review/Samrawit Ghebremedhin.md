## 1. Project Overview
- **Group Members:**
  - a1744126
  - a1851092
  - a1810859
  - a1915043

## 2. Manual Code Review

### Architecture and Design

| **Aspect**                            | **Status**               | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Protocol Implementation Adherence** | ❌ Not Adhered            | The provided code does not implement the OLAF/Neighbourhood protocol as specified. Key protocol features such as message signing, encryption, fingerprint verification, and proper routing through neighborhood servers are missing or improperly implemented. For example, the `handle_chat` function does not handle end-to-end encryption as outlined in the protocol. Additionally, the client-server communication does not follow the defined JSON structures for different message types. |
| **Security Measures**                 | ⚠️ Partially Implemented | Some basic security measures are present, such as the use of WebSockets for communication. However, critical security features like proper authentication and encryption are either missing or incorrectly implemented. The `vulnerable_authentication` function is a placeholder and does not follow secure practices. Moreover, the use of plaintext messages in public chats contradicts the protocol's emphasis on securing communications.                                                  |

### Code Quality

| **Aspect**                       | **Status**           | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Readability and Organization** | ⚠️ Poor Organization | The code lacks proper structure and modularization. Functions are scattered without clear separation between different components of the system. Additionally, comments indicate placeholder implementations, such as in `encrypt_message_cpp` and `decrypt_message_cpp`, suggesting that the code may have been heavily AI-generated without proper modification.                                                                                                    |
| **Error Handling and Logging**   | ⚠️ Inadequate        | Error handling is minimal and inconsistent. For instance, the `handle_chat` function sends a generic error message if the recipient is not connected but does not handle other potential errors gracefully. Logging is limited to basic `print` statements, which are insufficient for debugging and monitoring in a production environment. Comprehensive logging mechanisms are absent, making it difficult to trace issues or monitor system behavior effectively. |

### Security-specific Checks

| **Aspect**                               | **Status**                 | **Comments**                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Input Validation**                     | ❌ Insufficient             | There is minimal input validation throughout the code. For example, the `vulnerable_authentication` function does not properly sanitize or validate user inputs, making it susceptible to injection attacks. Additionally, message handling functions do not thoroughly validate the structure and content of incoming messages, increasing the risk of processing malformed or malicious data. |
| **Access Control**                       | ❌ Missing                  | The code does not implement robust access control mechanisms. Users are not properly authenticated or authorized to perform actions, allowing potential unauthorized access. The `vulnerable_authentication` function uses hardcoded credentials, which can be easily bypassed, and there are no role-based access controls to restrict functionalities based on user privileges.               |
| **Cryptographic Implementations**        | ❌ Incorrect Implementation | The cryptographic functions `encrypt_message_cpp` and `decrypt_message_cpp` are placeholders and do not implement the specified encryption protocols (RSA, AES-GCM). Additionally, the use of subprocess calls for encryption is insecure and opens avenues for exploitation. The protocol specifies detailed encryption and signing mechanisms which are not adhered to in the code.           |
| **Secure Data Storage and Transmission** | ❌ Insecure Transmission    | While WebSockets are used for communication, there is no implementation of secure WebSockets (`wss://`). Data transmitted is not adequately encrypted, especially in public chats where messages are sent in plaintext. The protocol emphasizes end-to-end encryption and secure transmission channels, which are not implemented in the current codebase.                                      |

## 3. Static Analysis

The static analysis was performed using **Bandit**, a security-oriented static analysis tool for Python. Below are the findings from the analysis of `chat_server.py`:

| Issue | Severity | Confidence | Location          | Description                                                                                    | Recommendation                                                                                                                                            | More Info                                                                                                |
| ----- | -------- | ---------- | ----------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| B404  | Low      | High       | chat_server.py:4  | Usage of the `subprocess` module can lead to security vulnerabilities if not handled properly. | Avoid using subprocess with untrusted input or ensure that all inputs are properly sanitized.                                                             | [Link](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b404-import-subprocess) |
| B603  | Low      | High       | chat_server.py:71 | Subprocess calls without `shell=True` can be exploited if untrusted input is passed.           | Avoid using `subprocess.run` with untrusted input or use safer alternatives. If `shell=True` is necessary, ensure that the input is thoroughly sanitized. | [Link](https://bandit.readthedocs.io/en/latest/plugins/b603_subprocess_without_shell_equals_true.html)   |
| B603  | Low      | High       | chat_server.py:76 | Same as above.                                                                                 | Same as above.                                                                                                                                            | [Link](https://bandit.readthedocs.io/en/latest/plugins/b603_subprocess_without_shell_equals_true.html)   |

## 4. Dynamic Analysis

The provided code is unfinished and poorly documented, so dynamic analysis was not suitable for this review. The reviewer did attempt to get the application running and send messages, however, most of the protocol remains in a placeholder state so nothing substantial can be said about the application. 

## 5. Backdoor/Vulnerability Assessment

Note that the following vulnerabilities are only *theoretically* possible because the application seems mostly unfinished and doesn't actually implement the protocol. The reviewer has written this section under the implication that these functions exist and operate in a finished implementation.

1. **Subprocess Command Execution:**
   - **Location:** `encrypt_message_cpp` and `decrypt_message_cpp` functions.
   - **Description:** These functions utilize `subprocess.run` to execute external encryption/decryption programs. This allows for the execution of arbitrary commands if user input is not properly sanitized.
   - **Example:** A malicious user could send a specially crafted message that includes shell commands, potentially leading to remote code execution. For instance, sending a message like `"; rm -rf / #` could exploit the subprocess call to delete critical server files.

2. **Vulnerable Authentication Mechanism:**
   - **Location:** `vulnerable_authentication` function.
   - **Description:** The authentication function uses hardcoded credentials (`username == "admin" && password == "password"`), making it trivial for attackers to gain unauthorized access.
   - **Example:** An attacker can easily bypass authentication by using the known credentials, gaining access to administrative functionalities or sensitive data. This could *potentially* allow the attacker to send fraudulent messages, manipulate user lists, or disrupt the chat service.

3. **Lack of Proper Encryption:**
   - **Location:** Throughout the message handling functions.
   - **Description:** Messages, especially public chats, are sent in plaintext without proper encryption, contrary to the protocol's specifications. This allows any eavesdropper to read the messages easily.
   - **Example:** An attacker monitoring the network traffic can intercept and read all public chat messages, compromising user privacy and the integrity of communications.

## 6. Results Summary

| **Category**            | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Strengths**           | - **Basic Functionality:** The code includes initial setups like a WebSocket server and basic message handling functions.<br>- **Understanding of Chat Application Needs:** Shows awareness of features like message sending and client management.                                                                                                                                                                                                                                                                                                                                                                             |
| **Areas for Improvement** | - **Protocol Non-Adherence:** Does not implement the OLAF/Neighbourhood protocol, missing essential features like message signing and proper encryption.<br>- **Security Shortcomings:** Lacks proper authentication, encryption, and input validation; uses hardcoded credentials and insecure subprocess calls.<br>- **Code Organization:** Poor structure with scattered functions and placeholder implementations; lacks modularity and clear separation of concerns.<br>- **Error Handling:** Minimal and inconsistent error handling; insufficient logging for debugging and monitoring. |
| **Critical Issues**     | - **Insecure Authentication:** Hardcoded credentials in `vulnerable_authentication` function pose a high security risk.<br>- **Unsafe Subprocess Usage:** `encrypt_message_cpp` and `decrypt_message_cpp` functions use subprocess calls that can be exploited for code injection.<br>- **Plaintext Transmission:** Messages are sent without encryption, exposing them to interception and violating protocol requirements.<br>- **Lack of Input Validation:** Increases susceptibility to injection attacks and processing of malicious data.                                                                 |

## 7. Recommendations

| **Recommendation Category**     | **Actions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Implement Protocol Specifications** | - Fully adhere to the OLAF/Neighbourhood protocol, including message signing, end-to-end encryption with RSA and AES-GCM, and correct message routing.                                                                                                                                                                                                                                                                                                                                         |
| **Enhance Security Measures**           | - Replace hardcoded credentials with a secure authentication system using hashed and salted passwords.<br>- Sanitize and validate all user inputs to prevent injection attacks.<br>- Secure subprocess calls or replace them with safe, integrated cryptographic functions.<br>- Use secure WebSocket connections (`wss://`) to encrypt data in transit.                                                                                                                                                              |
| **Improve Code Quality**                | - Refactor the codebase for better organization, separating concerns into modules or classes.<br>- Remove placeholder functions and implement fully functional features.<br>- Introduce robust error handling and comprehensive logging mechanisms.                                                                                                                                                                                                                                              |
| **Conduct Comprehensive Testing**       | - Perform thorough static analysis with tools like Bandit to identify and fix vulnerabilities.<br>- Carry out dynamic analysis, including penetration testing and fuzzing, to uncover runtime issues.<br>- Implement unit and integration tests to ensure all components function correctly.<br>- Regularly conduct peer code reviews to maintain code quality and security standards.                                                                                                                    |