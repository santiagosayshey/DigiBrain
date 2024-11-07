**Week 1 Cheat Sheet**

- **Critical Need for Security Engineering**: Software vulnerabilities in critical systems pose severe risks.
  - **Examples**:
    - **Therac-25 (1985-1987)**: Software bug caused radiation overdoses, resulting in deaths.
    - **Equifax Breach (2017)**: Single vulnerability exposed data of 147 million consumers.

- **Kerckhoff's Principle**: A system should be secure even if everything about it, except the key, is public knowledge. Security should rely on key secrecy, not system secrecy.

- **Risk Formula**:  
  **Risk = Threats × Vulnerabilities × Consequences**

- **Threat Modeling**: Structured process to identify and address security risks.
  - **Steps**:
    1. **Identify Assets**: Determine valuable assets (data, systems).
    2. **Create Architectural Overview**: Understand system components and data flows.
    3. **Identify Threats**: Use models like STRIDE to find potential threats.
    4. **Identify Vulnerabilities**: Find weaknesses in the system.
    5. **Model Attacks**: Analyze how threats can exploit vulnerabilities.
    6. **Perform Risk Analysis**: Assess the likelihood and impact of each threat.
    7. **Plan Mitigations**: Propose measures to reduce risks.

- **Attack Trees**: Diagrams showing how attackers achieve goals.
  - **Structure**: Root (attacker's goal), branches (methods), leaves (specific actions).
  - **Purpose**: Visualize attack paths to prioritize defenses.

- **OWASP Top 10 Web Application Security Risks (2021)**:

| #  | Vulnerability                          | Description                                           | Example                                                      |
|----|----------------------------------------|-------------------------------------------------------|--------------------------------------------------------------|
| 1  | **Broken Access Control**              | Improper enforcement of access restrictions           | 2018 Facebook breach: Attackers stole access tokens          |
| 2  | **Cryptographic Failures**             | Weak or misused encryption                            | 2017 Equifax breach: Unencrypted data exposed                |
| 3  | **Injection**                          | Untrusted data sent to an interpreter                 | 2014 TweetDeck XSS: JavaScript in tweets executed            |
| 4  | **Insecure Design**                    | Flaws in design patterns and architecture             | 2021 Twitch leak: Misconfigured server exposed data          |
| 5  | **Security Misconfiguration**          | Incorrect security settings                           | 2019 Capital One breach: Misconfigured firewall              |
| 6  | **Vulnerable and Outdated Components** | Use of components with known vulnerabilities          | 2017 Equifax breach: Outdated Apache Struts exploited        |
| 7  | **Identification and Authentication Failures** | Weak authentication mechanisms               | 2012 Dropbox breach: Reused passwords compromised            |
| 8  | **Software and Data Integrity Failures** | Lack of integrity checks on software/data             | 2020 SolarWinds attack: Compromised updates used             |
| 9  | **Security Logging and Monitoring Failures** | Inadequate logging and incident response       | 2014 Yahoo breach: Undetected for two years                  |
| 10 | **Server-Side Request Forgery (SSRF)** | Application fetches URL without validation            | 2019 Capital One breach: SSRF exploited AWS metadata service |

- **Responding to Risks**:

| Strategy         | Explanation                                                             | Real-Life Example                                                     |
| ---------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Avoidance**    | Eliminate the risk entirely by removing its cause.                      | **Apple's removal of Flash support** due to security issues.          |
| **Transference** | Shift the risk to a third party better equipped to handle it.           | **Using cloud services like AWS**, transferring infrastructure risks. |
| **Mitigation**   | Reduce the likelihood or impact of the risk through proactive measures. | **Implementing HTTPS** across all websites to secure communications.  |
| **Acceptance**   | Acknowledge and accept the risk without action, often for minor risks.  | **Accepting minor UI bugs** in a non-critical application.            |

- **Opponents in Cybersecurity**:

| Strategy         | Explanation                                                             | Real-Life Example                                                     |
| ---------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Avoidance**    | Eliminate the risk entirely by removing its cause.                      | **Apple's removal of Flash support** due to security issues.          |
| **Transference** | Shift the risk to a third party better equipped to handle it.           | **Using cloud services like AWS**, transferring infrastructure risks. |
| **Mitigation**   | Reduce the likelihood or impact of the risk through proactive measures. | **Implementing HTTPS** across all websites to secure communications.  |
| **Acceptance**   | Acknowledge and accept the risk without action, often for minor risks.  | **Accepting minor UI bugs** in a non-critical application.            |


| Opponent Type       | Motives/Actions                                                                 | Real-Life Example                                                                 |
| ------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Nation-States**   | Espionage, sabotage, political gain through advanced persistent threats (APTs). | **Stuxnet (2010)**: Malware attack on Iranian nuclear facilities.                 |
| **Cybercriminals**  | Financial gain via ransomware, data theft, fraud.                               | **WannaCry (2017)**: Ransomware affecting 200,000+ systems globally.              |
| **Hacktivists**     | Ideological motives, protest via DDoS attacks, defacements.                     | **Anonymous (2010)**: Attacks on PayPal and others supporting anti-piracy.        |
| **Insider Threats** | Employees causing harm intentionally or accidentally.                           | **Edward Snowden (2013)**: Leaked classified NSA documents.                       |
| **Script Kiddies**  | Novices using existing tools for fun or recognition.                            | **TalkTalk Hack (2015)**: Teenager exploited vulnerabilities causing data breach. |

**Injection Flaws: Types, Examples, and Mitigations**

| **Attack Type**                       | **Description**                                    | **Vulnerable Code Example**                                          | **Attack Input**                               | **Effect**                                                             | **Mitigation Example**                                                               |
| ------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **SQL Injection**                     | Untrusted input alters SQL queries                 | `query = "SELECT * FROM users WHERE username = '" + username + "'";` | `username = "' OR '1'='1"`                     | Bypasses authentication; attacker logs in without credentials          | Use parameterized queries: `query = "SELECT * FROM users WHERE username = ?";`       |
| **Command Injection**                 | Untrusted input executed as system commands        | `exec("ping " + ipAddress);`                                         | `ipAddress = "8.8.8.8; rm -rf /"`              | Executes unintended commands; system compromise                        | Validate input: ensure `ipAddress` is a valid IP; avoid using `exec` with user input |
| **XSS (Cross-Site Scripting)**        | Malicious scripts injected into webpages           | Renders user input directly: `<div>User: ` + userInput + `</div>`    | `userInput = "<script>alert('XSS');</script>"` | Attacker's script runs in users' browsers                              | Encode output: escape `userInput` before rendering                                   |
| **CSRF (Cross-Site Request Forgery)** | Unauthorized actions performed on behalf of a user | Sensitive actions without CSRF protection                            | User visits malicious site with hidden form    | Attacker forces user to execute unwanted actions (e.g., fund transfer) | Implement CSRF tokens: include in forms and verify server-side                       |

**Consequences of Injection Attacks**:

- Data breaches (e.g., **Sony PSN breach 2011** via SQL injection exposed 77 million accounts)
- Unauthorized access and data manipulation
- Service disruptions and system compromises

**Mitigation Strategies**:

- **Parameterized Queries/Prepared Statements**: Prevent SQL injection by separating code from data
- **Input Validation and Sanitization**: Ensure inputs match expected patterns
- **Output Encoding**: Escape data before rendering to prevent XSS
- **Use Safe APIs**: Avoid executing shell commands with user input
- **Implement CSRF Protection**: Use tokens to validate legitimate requests
- **Principle of Least Privilege**: Limit permissions to minimize potential damage

I apologize for not following your instructions earlier. I will avoid one-line bullet points and unnecessary headings, and include all the mitigations within the tables to maximize space.

**Week 3 Cheat Sheet**

---

**Diffie-Hellman Key Exchange**

- **Issue**: Securely share a secret key over an insecure channel without exchanging the key itself.
- **Solution**: Both parties generate a shared secret using public and private components.

**Example:**

| Step | Alice                                                        | Bob                                                         |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| 1    | Agree on public base `g=5` and prime `p=23`.                 | Same                                                        |
| 2    | Selects private `a=6`, computes `A = g^a mod p = 8`.         | Selects private `b=15`, computes `B = g^b mod p = 19`.      |
| 3    | Receives `B=19`, computes shared secret `s = B^a mod p = 2`. | Receives `A=8`, computes shared secret `s = A^b mod p = 2`. |
| 4    | Shared secret `s=2`.                                         | Shared secret `s=2`.                                        |


| Step | Alice                                                        | Bob                                                         |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| 1    | Agree on public base `g=5` and prime `p=23`.                 | Same                                                        |
| 2    | Selects private `a=6`, computes `A = g^a mod p = 8`.         | Selects private `b=15`, computes `B = g^b mod p = 19`.      |
| 3    | Receives `B=19`, computes shared secret `s = B^a mod p = 2`. | Receives `A=8`, computes shared secret `s = A^b mod p = 2`. |
| 4    | Shared secret `s=2`.                                         | Shared secret `s=2`.                                        |

---

**Authentication Factors, Attacks, and Mitigations**

| **Factor**             | **Attack Methods**                                            | **Examples**                                                                 | **Mitigations**                                                                                                                                  |
| ---------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Something You Know** | Stealing passwords via phishing, keyloggers, network sniffing | Phishing emails, keylogger malware, intercepted credentials                  | Use strong, unique passwords; enable multi-factor authentication (MFA); avoid transmitting passwords in plaintext; educate users about phishing. |
| **Something You Have** | Cloning tokens, SIM swapping                                  | Duplicating access cards, SIM cloning                                        | Secure physical tokens; use tamper-resistant devices; monitor account activity; implement hardware security modules (HSMs).                      |
| **Something You Are**  | Replicating biometrics                                        | Fake fingerprints, 3D-printed fingerprints, masks to fool facial recognition | Implement liveness detection in biometric systems; combine with other factors (MFA); regularly update and secure biometric templates.            |

---

**Challenge-Response Authentication**

- **Issue**: Verify identity without revealing the shared secret; prevent replay attacks.
- **Solution**: Use a nonce and hash function to authenticate.

**Process:**

| Step | Description                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------------------|
| 1    | Sender generates a random nonce and sends it to the recipient.                                                               |
| 2    | Recipient computes `hash(nonce + shared_secret)` and sends the hash back.                                                    |
| 3    | Sender computes the expected hash and verifies it matches the received hash.                                                 |
| 4    | If hashes match, identity is verified; else, authentication fails.                                                           |

**Key Concepts**: Nonce ensures uniqueness; shared secret is not transmitted; hash function protects the secret; prevents replay attacks.

---

**Common Exploits and Mitigations**

| **Exploit**              | **Description**                                                            | **Example Vulnerability**                                                              | **Consequences**                                                            | **Mitigation Strategies**                                                                                                                                                                                                                                                                                 |
| ------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Buffer Overflow**      | Writing beyond buffer boundaries, overwriting adjacent memory              | `char buf[64]; strcpy(buf, input);` (no bounds checking)                               | Data corruption; control flow hijacking; arbitrary code execution           | **Use safe functions** like `strncpy(dest, src, n)` ensuring `n` is the buffer size; **validate input lengths** before copying; **avoid dangerous functions** like `gets()`; **enable stack protections** such as stack canaries and ASLR (Address Space Layout Randomization).                           |
| **Integer Overflow**     | Arithmetic exceeds integer limits, causing wraparound or unexpected values | `unsigned int size = user_value + 10;` (if `user_value` is large, `size` may overflow) | Incorrect calculations; buffer overflows; allocation of insufficient memory | **Validate input ranges** to ensure they are within expected bounds; **check for overflows** before operations (e.g., `if (user_value > UINT_MAX - 10)`); **use larger data types** like `unsigned long long` if necessary; **use safe arithmetic functions** that detect overflows.                      |
| **Format String Attack** | User-controlled format strings in functions like `printf`                  | `printf(user_input);` (user input used directly as format string)                      | Information disclosure; memory corruption; code execution                   | **Always specify format strings** explicitly (e.g., `printf("%s", user_input);`); **sanitize user input** to remove or escape format specifiers like `%`; **use compiler warnings** and flags (`-Wformat -Wformat-security`); **disable dangerous format specifiers** if not needed (e.g., disable `%n`). |

---

*Note: All mitigations are included within the tables to maximize space and avoid unnecessary headings or bullet points.*

---

| **Exploit**              | **Description**                                                            | **Example Vulnerability**                                                              | **Consequences**                                                            | **Mitigation Strategies**                                                                                                                                                                                                                                                                                 |
| ------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Buffer Overflow**      | Writing beyond buffer boundaries, overwriting adjacent memory              | `char buf[64]; strcpy(buf, input);` (no bounds checking)                               | Data corruption; control flow hijacking; arbitrary code execution           | **Use safe functions** like `strncpy(dest, src, n)` ensuring `n` is the buffer size; **validate input lengths** before copying; **avoid dangerous functions** like `gets()`; **enable stack protections** such as stack canaries and ASLR (Address Space Layout Randomization).                           |
| **Integer Overflow**     | Arithmetic exceeds integer limits, causing wraparound or unexpected values | `unsigned int size = user_value + 10;` (if `user_value` is large, `size` may overflow) | Incorrect calculations; buffer overflows; allocation of insufficient memory | **Validate input ranges** to ensure they are within expected bounds; **check for overflows** before operations (e.g., `if (user_value > UINT_MAX - 10)`); **use larger data types** like `unsigned long long` if necessary; **use safe arithmetic functions** that detect overflows.                      |
| **Format String Attack** | User-controlled format strings in functions like `printf`                  | `printf(user_input);` (user input used directly as format string)                      | Information disclosure; memory corruption; code execution                   | **Always specify format strings** explicitly (e.g., `printf("%s", user_input);`); **sanitize user input** to remove or escape format specifiers like `%`; **use compiler warnings** and flags (`-Wformat -Wformat-security`); **disable dangerous format specifiers** if not needed (e.g., disable `%n`). |
**Authentication Vulnerabilities**

| **Category**          | **Attacks**                  | **Examples**                      | **Mitigations**                                       |
|-----------------------|------------------------------|-----------------------------------|-------------------------------------------------------|
| **Something You Know** | Phishing, keyloggers, sniffing | Phishing emails, malware          | Strong unique passwords, MFA, user education          |
| **Something You Have** | Token cloning, SIM swapping    | Duplicated access cards, SIM cloning | Secure/tamper-resistant tokens, monitor accounts, HSMs |
| **Something You Are**  | Biometric spoofing            | Fake/3D-printed fingerprints, masks | Liveness detection, MFA, secure biometric data        |
