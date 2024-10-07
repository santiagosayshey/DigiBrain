## 1. Project Overview
- **Group Members:**
  - a1744126
  - a1851092
  - a1810859
  - a1915043

- **Reviewers:**
  - [Reviewer Names]

## 2. Manual Code Review

### Architecture and Design

| **Aspect**                         | **Status** | **Comments**                                                                                                                                                                                                                                                    |
|------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Protocol Implementation Adherence** | ❌ Not Adhered | The provided code does not implement the OLAF/Neighbourhood protocol as specified. Key protocol features such as message signing, encryption, fingerprint verification, and proper routing through neighborhood servers are missing or improperly implemented. For example, the `handle_chat` function does not handle end-to-end encryption as outlined in the protocol. Additionally, the client-server communication does not follow the defined JSON structures for different message types. |
| **Security Measures**              | ⚠️ Partially Implemented | Some basic security measures are present, such as the use of WebSockets for communication. However, critical security features like proper authentication and encryption are either missing or incorrectly implemented. The `vulnerable_authentication` function is a placeholder and does not follow secure practices. Moreover, the use of plaintext messages in public chats contradicts the protocol's emphasis on securing communications.                                                                                                   |

### Code Quality

| **Aspect**                       | **Status**          | **Comments**                                                                                                                                                                                                                                     |
|----------------------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Readability and Organization** | ⚠️ Poor Organization | The code lacks proper structure and modularization. Functions are scattered without clear separation between different components of the system. Additionally, comments indicate placeholder implementations, such as in `encrypt_message_cpp` and `decrypt_message_cpp`, suggesting that the code may have been heavily AI-generated without proper customization.                                                                                                                                                   |
| **Error Handling and Logging**   | ⚠️ Inadequate        | Error handling is minimal and inconsistent. For instance, the `handle_chat` function sends a generic error message if the recipient is not connected but does not handle other potential errors gracefully. Logging is limited to basic `print` statements, which are insufficient for debugging and monitoring in a production environment. Comprehensive logging mechanisms are absent, making it difficult to trace issues or monitor system behavior effectively.                                                                                                                                                                                                                      |

### Security-specific Checks

| **Aspect**                         | **Status**               | **Comments**                                                                                                                                                                                                                                                                         |
|------------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Input Validation**               | ❌ Insufficient          | There is minimal input validation throughout the code. For example, the `vulnerable_authentication` function does not properly sanitize or validate user inputs, making it susceptible to injection attacks. Additionally, message handling functions do not thoroughly validate the structure and content of incoming messages, increasing the risk of processing malformed or malicious data. |
| **Access Control**                 | ❌ Missing                | The code does not implement robust access control mechanisms. Users are not properly authenticated or authorized to perform actions, allowing potential unauthorized access. The `vulnerable_authentication` function uses hardcoded credentials, which can be easily bypassed, and there are no role-based access controls to restrict functionalities based on user privileges. |
| **Cryptographic Implementations**  | ❌ Incorrect Implementation | The cryptographic functions `encrypt_message_cpp` and `decrypt_message_cpp` are placeholders and do not implement the specified encryption protocols (RSA, AES-GCM). Additionally, the use of subprocess calls for encryption is insecure and opens avenues for exploitation. The protocol specifies detailed encryption and signing mechanisms which are not adhered to in the code.                                                                                                                       |
| **Secure Data Storage and Transmission** | ❌ Insecure Transmission | While WebSockets are used for communication, there is no implementation of secure WebSockets (`wss://`). Data transmitted is not adequately encrypted, especially in public chats where messages are sent in plaintext. The protocol emphasizes end-to-end encryption and secure transmission channels, which are not implemented in the current codebase.                                                                                                                           |

### Additional Observations
- **Placeholder Implementations:** Many functions, such as `vulnerable_authentication`, `encrypt_message_cpp`, and `decrypt_message_cpp`, appear to be placeholders and do not fulfill the protocol requirements. This suggests that the code may have been heavily AI-generated without proper customization or completion.
- **Protocol Misalignment:** The overall architecture does not align with the OLAF/Neighbourhood protocol. Critical elements like message signing, fingerprint verification, and proper routing through neighborhood servers are absent, leading to non-compliance with the specified protocol.
- **Ethical Backdoors:** The intentional vulnerabilities mentioned in the README, such as the execution of arbitrary commands via subprocess calls, are present. However, their implementation is rudimentary and easily detectable, reducing the challenge for peer reviewers. For example, the `encrypt_message_cpp` and `decrypt_message_cpp` functions use subprocess calls without proper input sanitization, making them straightforward targets for exploitation.

## 3. Static Analysis
- **TODO**

## 4. Dynamic Analysis
- **TODO**

## 5. Backdoor/Vulnerability Assessment

### Suspected Backdoors or Vulnerabilities

1. **Subprocess Command Execution:**
   - **Location:** `encrypt_message_cpp` and `decrypt_message_cpp` functions.
   - **Description:** These functions utilize `subprocess.run` to execute external encryption/decryption programs. This allows for the execution of arbitrary commands if user input is not properly sanitized.
   - **Example:** A malicious user could send a specially crafted message that includes shell commands, potentially leading to remote code execution. For instance, sending a message like `"; rm -rf / #` could exploit the subprocess call to delete critical server files.

2. **Vulnerable Authentication Mechanism:**
   - **Location:** `vulnerable_authentication` function.
   - **Description:** The authentication function uses hardcoded credentials (`username == "admin" && password == "password"`), making it trivial for attackers to gain unauthorized access.
   - **Example:** An attacker can easily bypass authentication by using the known credentials, gaining access to administrative functionalities or sensitive data. This could allow the attacker to send fraudulent messages, manipulate user lists, or disrupt the chat service.

3. **Lack of Proper Encryption:**
   - **Location:** Throughout the message handling functions.
   - **Description:** Messages, especially public chats, are sent in plaintext without proper encryption, contrary to the protocol's specifications. This allows any eavesdropper to read the messages easily.
   - **Example:** An attacker monitoring the network traffic can intercept and read all public chat messages, compromising user privacy and the integrity of communications.

### Methods Used for Identification

- **Code Inspection:** Manually reviewing the code to identify functions that handle sensitive operations such as authentication and encryption.
- **Comment Analysis:** Noting the presence of comments indicating vulnerabilities and placeholder implementations, such as in the `vulnerable_authentication` function.
- **Functionality Testing:** Understanding the flow of data through the `encrypt_message_cpp` and `decrypt_message_cpp` functions revealed the use of subprocess calls, which are inherently insecure.
- **Protocol Comparison:** Comparing the implemented features against the OLAF/Neighbourhood protocol specifications highlighted significant discrepancies and missing security measures.

### Potential Impact

1. **Subprocess Command Execution:**
   - **Impact:** High. Allows attackers to execute arbitrary commands on the server, leading to potential full system compromise.
   - **Exploitation Scenario:** An attacker could inject commands that read, modify, or delete server files, install malware, or pivot to other systems within the network.

2. **Vulnerable Authentication Mechanism:**
   - **Impact:** High. Enables unauthorized access to the system, potentially exposing all user data and allowing the attacker to manipulate chat messages or user lists.
   - **Exploitation Scenario:** An attacker could log in as an admin, send fraudulent messages, or disrupt the chat service by modifying the client list, leading to a loss of trust and service availability.

3. **Lack of Proper Encryption:**
   - **Impact:** Medium to High. Compromises the confidentiality and integrity of user communications.
   - **Exploitation Scenario:** An attacker can intercept and read all public chat messages, potentially extracting sensitive information, personal data, or confidential discussions.

## 6. Results Summary
- **TODO**

## 7. Recommendations
- **TODO**