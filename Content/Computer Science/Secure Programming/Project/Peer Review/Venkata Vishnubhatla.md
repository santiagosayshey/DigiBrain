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

| **Aspect**                      | **Status**              | **Comments**                                                                                                                                                                                                                                                                                                    |
|---------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Protocol Implementation Adherence** | ❌ Not Fully Adhered     | The protocol is mostly correct; however, there is an issue with client update lists. Clients are sent as base64-encoded PEM strings instead of raw PEMs. Specifically, in the `send_client_list_response` function, public keys are base64-encoded before inclusion, which deviates from the specification requiring PEM-formatted lists. This needs correction and will be verified during dynamic analysis. |
| **Security Measures (encryption, authentication, etc.)** | ⚠️ Partially Implemented | Public keys are exchanged correctly using RSA, and encryption methods like AES-CBC are implemented. However, the role of the `is_server` variable is unclear and may impact access control. Its usage needs thorough review to ensure it does not inadvertently bypass security mechanisms.                                               |

### Code Quality

| **Aspect**                    | **Status**               | **Comments**                                                                                                                                                                                                                               |
|-------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Readability and Organization** | ⚠️ Needs Improvement      | The code is moderately organized but suffers from redundant imports and lack of modularization. Better structuring and comprehensive comments would enhance readability and maintainability.                                                          |
| **Error Handling and Logging**   | ⚠️ Inadequate             | Basic error handling is present, primarily using print statements. Implementing a robust logging framework would improve debugging and monitoring capabilities, making the system more resilient and easier to maintain.                        |

### Security-specific Checks

| **Aspect**                           | **Status**               | **Comments**                                                                                                                                                                                                                                                                                    |
|--------------------------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Input Validation**                 | ❌ Insufficient           | Input validation is minimal. The system assumes well-formed JSON messages without thorough checks, which could allow malicious inputs to exploit vulnerabilities. Functions like `process_message` should include stricter validation of incoming data structures and content.                |
| **Access Control**                   | ⚠️ Potential Issues      | Access control mechanisms are not clearly enforced. The `is_server` variable differentiates server sessions, but its impact on restricting access rights is unclear. This could potentially allow unauthorized actions if not properly managed. A thorough review is necessary to ensure robust access control. |
| **Cryptographic Implementations**    | ⚠️ Partially Correct      | Cryptographic functions adhere to protocol specifications, utilizing secure padding schemes and encryption modes (RSA-OAEP, AES-CBC). However, handling of cryptographic keys and potential side-channel attacks should be reviewed to ensure complete security.                                       |
| **Secure Data Storage and Transmission** | ❌ Insecure Transmission | Data transmission uses standard WebSockets and HTTP for file transfers without implementing secure WebSockets (wss://), potentially exposing data to interception. Additionally, file uploads lack authentication, which could allow unauthorized file access. Secure transmission protocols need to be enforced. |

---

*Note: Further sections will be completed following the assignment requirements.*