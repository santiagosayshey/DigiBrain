## 1. Project Overview
- Group Members:
	- a1744126
	- a1851092
	- a1810859
	- a1915043
- Reviewers: 
	- Samuel Chau (a1799298)

## 2. Manual Code Review
- Architecture and Design:
  - Protocol implementation adherence
    - The code does not implement the OLAF/Neighbourhood protocol at all. It appears to be a generic WebSocket chat application.
    - Example of missing protocol implementation:
      ```python
      # Missing required message structure, e.g.:
      # {
      #     "type": "signed_data",
      #     "data": {  },
      #     "counter": 12345,
      #     "signature": "<Base64 encoded (signature of (data JSON concatenated with counter))>"
      # }
      ```
  - Security measures (encryption, authentication, etc.)
    - Encryption is not implemented according to protocol specifications.
    - Authentication is weak and not used:
      ```python
      def vulnerable_authentication(username, password):
          if username == "admin" and password == "password":
              return True
          return False
      ```
- Code Quality:
  - Readability and organization
    - Code appears to be AI-generated and lacks coherence.
    - Unused functions present:
      ```python
      def generate_aes_key():
          return os.urandom(32)

      def generate_iv():
          return os.urandom(16)
      ```
  - Error handling and logging
    - Minimal error handling, no logging implemented.
- Security-specific checks:
  - Input validation
    - Almost non-existent, e.g., in handle_chat function:
      ```python
      async def handle_chat(data, websocket):
          recipient_id = data["recipient_id"]
          message = data["message"]
          # No validation of recipient_id or message
      ```
  - Access control
    - Not implemented
  - Cryptographic implementations
    - Insecure use of subprocess for encryption:
      ```python
      def encrypt_message_cpp(message):
          result = subprocess.run(['./encryption_program', 'encrypt', message], capture_output=True, text=True)
          return result.stdout.strip()
      ```
  - Secure data storage and transmission
    - No implementation of secure storage or transmission as per protocol requirements

## 3. Static Analysis
- Tool(s) used:
- Key findings:
  - Potential vulnerabilities:
  - Code quality issues:
  - Security misconfigurations:

## 4. Dynamic Analysis
- Testing environment:
- Functional testing:
  - Basic functionality (message sending, file transfer, etc.)
  - Error handling and edge cases
- Security testing:
  - Network traffic analysis
  - Fuzzing results
  - Penetration testing attempts

## 5. Backdoor/Vulnerability Assessment
- Suspected backdoors or vulnerabilities:
  1. Command injection vulnerability in encryption functions:
     ```python
     def encrypt_message_cpp(message):
         result = subprocess.run(['./encryption_program', 'encrypt', message], capture_output=True, text=True)
         return result.stdout.strip()
     ```
  2. Weak, unused authentication function:
     ```python
     def vulnerable_authentication(username, password):
         if username == "admin" and password == "password":
             return True
         return False
     ```
  3. Lack of input validation throughout the code
  4. Insecure WebSocket communication (ws:// instead of wss://)

- Methods used for identification:
  - Manual code review

- Potential impact:
  - Command injection could lead to unauthorized system access
  - Lack of proper authentication and input validation leaves the system open to various attacks
  - Insecure communication could expose user messages to interception

## 6. Results Summary
- Strengths:
- Areas for improvement:
- Critical issues:

## 7. Recommendations
- Security enhancements:
- Code quality improvements:
- Additional testing suggested:

Recommendations for tools in steps 3 and 4:

For Static Analysis (step 3):
1. Bandit
2. Pylint
3. SonarQube

For Dynamic Analysis (step 4):
1. OWASP ZAP
2. Burp Suite
3. Wireshark