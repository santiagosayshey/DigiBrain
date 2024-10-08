## 1. Project Overview
- **Group Members:**
  - Bradley Hill
  - James Nguyen
  - Natanand Akomsoontorn
  - Vincent Scaffidi-Muta

- **Reviewers:** 
  - [Your Name]

## 2. Manual Code Review

### Architecture and Design

| **Aspect**                            | **Status** | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Protocol Implementation Adherence** | ✅ Adhered  | The implementation follows the OLAF/Neighbourhood protocol specifications closely. Key features such as message signing, encryption, fingerprint verification, and proper routing through neighborhood servers are implemented. For instance, the `process_message` function handles different message types (`hello`, `chat`, `public_chat`, etc.) as defined in the protocol. The use of JSON structures aligns with the protocol's requirements for message formatting. |
| **Security Measures**                 | ✅ Adequate | The code incorporates essential security measures, including the use of RSA for asymmetric encryption and AES for symmetric encryption, adhering to the specified padding schemes and key sizes. Additionally, while encryption is implemented, secure WebSocket (wss://) connections are not utilized, potentially exposing data in transit. However, this is fine and shouldn't be implemented until the end of the assignment anyhow.                                   |

### Code Quality

| **Aspect**                       | **Status**       | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Readability and Organization** | ✅ Well Organized | The code is modularized effectively, separating server and client functionalities. Functions are well-defined with clear responsibilities, and the use of classes (e.g., `ClientSession`, `ChatClient`) enhances readability. Comprehensive comments and docstrings are present, explaining the purpose of functions and critical code sections. The use of consistent naming conventions and structured error handling contributes to overall code clarity.<br><br>However, there are only 2 files here, which could make it harder to debug and therefore introduce security issues. |
| **Error Handling and Logging**   | ✅ Adequate       | Error handling is implemented in various parts of the code, such as during message processing and client connections. Exceptions are caught and logged appropriately, preventing the application from crashing unexpectedly. However, logging primarily relies on `print` statements, which are not suitable for production environments. Implementing a more robust logging framework (e.g., Python's `logging` module) would enhance the ability to monitor and debug the application effectively.                                                                                   |

### Security-specific Checks

| **Aspect**                               | **Status**               | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Input Validation**                     | ✅ Adequate               | The code performs necessary input validations, such as verifying message structures and ensuring that required fields are present. Functions like `verify_signature` and `verify_all` enforce the integrity and authenticity of incoming messages. Additionally, the use of JSON parsing inherently provides a layer of validation, mitigating risks associated with malformed or malicious inputs.                                                                   |
| **Access Control**                       | ✅ Implemented            | Access control mechanisms are in place, ensuring that only authenticated users can send and receive messages. The use of public and private keys for user authentication prevents unauthorized access. Additionally, server responsibilities include verifying message signatures and maintaining client lists, which further enforce controlled access within the chat system.                                                                                       |
| **Cryptographic Implementations**        | ✅ Correct Implementation | The cryptographic implementations adhere to the protocol specifications. RSA is used for asymmetric encryption with OAEP padding and SHA-256 hashing, while AES-GCM is employed for symmetric encryption with appropriate key sizes and initialization vectors. Functions like `encrypt_aes_key`, `decrypt_aes_key`, `encrypt_message`, and `decrypt_message` correctly implement the required cryptographic operations, ensuring data confidentiality and integrity. |

## 3. Static Analysis

The static analysis was performed using **Bandit**, a security-oriented static analysis tool for Python. Below are the findings from the analysis of `server.py`:

| **Issue**                         | **Severity** | **Confidence** | **Location**        | **Description**                                                                                                                                                                  | **Recommendation**                                                                                                             | **More Info**                                                                                              |
|-----------------------------------|--------------|-----------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| **B201: flask_debug_true**        | High         | Medium          | server.py:429       | A Flask app appears to be run with `debug=True`, which exposes the Werkzeug debugger and allows the execution of arbitrary code.                                                | Set `debug=False` in production environments to prevent the exposure of the debugger and potential arbitrary code execution. | [B201: Flask debug mode](https://bandit.readthedocs.io/en/latest/plugins/b201_flask_debug_true.html) |

## 4. Dynamic Analysis
*Placeholder for Dynamic Analysis. Please conduct dynamic testing including functional testing, security testing, and penetration testing as per the assignment guidelines.*

## 5. Backdoor/Vulnerability Assessment

Based on the provided code and the assignment requirements, the following backdoors and vulnerabilities have been identified:


4. **Potential Replay Attack Vulnerability:**
   - **Location:** `server.py` in the `verify_all` function
   - **Description:** While counters are used to mitigate replay attacks, the current implementation updates the counter after verifying the message. There might be a window where an attacker could resend a valid message before the counter is updated, especially in high-throughput scenarios.
   - **Impact:** Low to Medium. Replay attacks can lead to duplicate messages or unintended actions if not adequately mitigated.
   - **Recommendation:** Ensure atomicity in updating and verifying counters to eliminate any window of opportunity for replay attacks. Consider implementing additional mechanisms such as nonce usage or timestamp validation for enhanced security.

5. **Insecure File Upload Endpoint:**
   - **Location:** `server.py` in the `/api/upload` route
   - **Description:** The file upload endpoint does not enforce authentication or authorization, allowing any client to upload files without verification. Additionally, the server does not validate or sanitize uploaded file contents, potentially enabling the upload of malicious files.
   - **Impact:** High. Unauthenticated file uploads can be exploited to store and distribute malicious files, leading to server compromise or distribution of malware.
   - **Recommendation:** Implement authentication and authorization checks for file upload endpoints. Validate and sanitize uploaded files to prevent the storage and distribution of malicious content. Consider implementing file type restrictions and scanning uploaded files for malware.

## 6. Results Summary
*Placeholder for Results Summary. To be completed after conducting dynamic analysis.*

## 7. Recommendations
*Placeholder for Recommendations. To be completed after conducting dynamic analysis.*