## 1. Project Overview
- **Group Members:**
  - a1744126
  - a1851092
  - a1810859
  - a1915043

- **Reviewers:**
  - Samuel Chau (a1799298)

## 2. Manual Code Review

### Architecture and Design

| **Aspect**                         | **Status**          | **Comments**                                                                                                                                                                                                                                                    |
|------------------------------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Protocol Implementation Adherence** | ❌ Not Adhered      | The provided code does not implement the OLAF/Neighbourhood protocol as specified. Key protocol features such as message signing, encryption, fingerprint verification, and proper routing through neighborhood servers are missing or improperly implemented. For example, the `handle_chat` function does not handle end-to-end encryption as outlined in the protocol. Additionally, the client-server communication does not follow the defined JSON structures for different message types. |
| **Security Measures**              | ⚠️ Partially Implemented | Some basic security measures are present, such as the use of WebSockets for communication. However, critical security features like proper authentication and encryption are either missing or incorrectly implemented. The `vulnerable_authentication` function is a placeholder and does not follow secure practices. Moreover, the use of plaintext messages in public chats contradicts the protocol's emphasis on securing communications.                                                                                                   |

### Code Quality

| **Aspect**                       | **Status**           | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Readability and Organization** | ⚠️ Poor Organization | The code lacks proper structure and modularization. Functions are scattered without clear separation between different components of the system. Additionally, comments indicate placeholder implementations, such as in `encrypt_message_cpp` and `decrypt_message_cpp`, suggesting that the code may have been heavily AI-generated without proper modification.                                                                                                    |
| **Error Handling and Logging**   | ⚠️ Inadequate        | Error handling is minimal and inconsistent. For instance, the `handle_chat` function sends a generic error message if the recipient is not connected but does not handle other potential errors gracefully. Logging is limited to basic `print` statements, which are insufficient for debugging and monitoring in a production environment. Comprehensive logging mechanisms are absent, making it difficult to trace issues or monitor system behavior effectively. |

### Security-specific Checks

| **Aspect**                         | **Status**               | **Comments**                                                                                                                                                                                                                                                                         |
|------------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Input Validation**               | ❌ Insufficient          | There is minimal input validation throughout the code. For example, the `vulnerable_authentication` function does not properly sanitize or validate user inputs, making it susceptible to injection attacks. Additionally, message handling functions do not thoroughly validate the structure and content of incoming messages, increasing the risk of processing malformed or malicious data. |
| **Access Control**                 | ❌ Missing                | The code does not implement robust access control mechanisms. Users are not properly authenticated or authorized to perform actions, allowing potential unauthorized access. The `vulnerable_authentication` function uses hardcoded credentials, which can be easily bypassed, and there are no role-based access controls to restrict functionalities based on user privileges. |
| **Cryptographic Implementations**  | ❌ Incorrect Implementation | The cryptographic functions `encrypt_message_cpp` and `decrypt_message_cpp` are placeholders and do not implement the specified encryption protocols (RSA, AES-GCM). Additionally, the use of subprocess calls for encryption is insecure and opens avenues for exploitation. The protocol specifies detailed encryption and signing mechanisms which are not adhered to in the code.                                                                                                                       |
| **Secure Data Storage and Transmission** | ❌ Insecure Transmission | While WebSockets are used for communication, there is no implementation of secure WebSockets (`wss://`). Data transmitted is not adequately encrypted, especially in public chats where messages are sent in plaintext. The protocol emphasizes end-to-end encryption and secure transmission channels, which are not implemented in the current codebase.                                                                                                                           |

## 3. Static Analysis
- **Recommended Tools:**

  ### **Bandit (for Python)**
  - **Description:** A security-oriented static analysis tool that scans Python code to find common security issues.
  - **Usage:** `bandit -r path/to/code`

  ### **SonarQube**
  - **Description:** A platform for continuous inspection of code quality and security vulnerabilities across multiple programming languages.
  - **Usage:** Integrate with CI/CD pipelines or run locally for detailed reports.

  ### **Flake8**
  - **Description:** A tool for enforcing coding standards and identifying syntax errors and potential bugs in Python code.
  - **Usage:** `flake8 path/to/code`

  ### **Pylint**
  - **Description:** An extensive code analysis tool that checks for errors, enforces a coding standard, and looks for code smells.
  - **Usage:** `pylint path/to/code`

## 4. Dynamic Analysis
- **Recommended Tools:**

  ### **OWASP ZAP (Zed Attack Proxy)**
  - **Description:** A full-featured security tool for finding vulnerabilities in web applications through automated and manual testing.
  - **Usage:** Run the proxy, configure the application to use it, and perform various attacks to identify security flaws.

  ### **Burp Suite**
  - **Description:** An integrated platform for performing security testing of web applications, offering a range of tools like a proxy, scanner, and intruder.
  - **Usage:** Use the proxy to intercept and manipulate traffic, and the scanner to automate vulnerability detection.

  ### **Wireshark**
  - **Description:** A network protocol analyzer that captures and interactively browses the traffic running on a computer network.
  - **Usage:** Monitor and analyze network traffic to identify insecure data transmission or unexpected behaviors.

  ### **Fuzzers (e.g., AFL, Peach Fuzzer)**
  - **Description:** Tools that automate the input of large amounts of random data to applications to uncover vulnerabilities like buffer overflows and crashes.
  - **Usage:** Configure the fuzzer to target specific functions or APIs within the chat application.

  ### **Metasploit Framework**
  - **Description:** A powerful tool for developing and executing exploit code against a remote target machine.
  - **Usage:** Use existing modules or create custom exploits to test the security of the chat application.

## 5. Backdoor/Vulnerability Assessment

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
- **TODO**

## 7. Recommendations
- **TODO**
