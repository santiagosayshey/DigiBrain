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

| #  | Vulnerability                            | Description                                               | Example                                                        |
|----|------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------|
| 1  | **Broken Access Control**                | Improper enforcement of access restrictions               | 2018 Facebook breach: Attackers stole access tokens            |
| 2  | **Cryptographic Failures**               | Weak or misused encryption                                | 2017 Equifax breach: Unencrypted data exposed                  |
| 3  | **Injection**                            | Untrusted data sent to an interpreter                     | 2014 TweetDeck XSS: JavaScript in tweets executed              |
| 4  | **Insecure Design**                      | Flaws in design patterns and architecture                 | 2021 Twitch leak: Misconfigured server exposed data            |
| 5  | **Security Misconfiguration**            | Incorrect security settings                               | 2019 Capital One breach: Misconfigured firewall                |
| 6  | **Vulnerable and Outdated Components**   | Use of components with known vulnerabilities              | 2017 Equifax breach: Outdated Apache Struts exploited          |
| 7  | **Identification and Authentication Failures** | Weak authentication mechanisms                       | 2012 Dropbox breach: Reused passwords compromised              |
| 8  | **Software and Data Integrity Failures** | Lack of integrity checks on software/data                 | 2020 SolarWinds attack: Compromised updates used               |
| 9  | **Security Logging and Monitoring Failures** | Inadequate logging and incident response             | 2014 Yahoo breach: Undetected for two years                    |
| 10 | **Server-Side Request Forgery (SSRF)**   | Application fetches URL without validation                | 2019 Capital One breach: SSRF exploited AWS metadata service   |

- **Responding to Risks**:
  - **Avoidance**: Eliminate the risk (remove risky features).
  - **Transference**: Shift risk to another party (use third-party services).
  - **Mitigation**: Reduce risk likelihood or impact (implement controls).
  - **Acceptance**: Acknowledge and accept minor risks.

- **Opponents in Cybersecurity**:
  - **Nation-States**: Espionage, sabotage.
  - **Cybercriminals**: Financial gain.
  - **Hacktivists**: Ideological motives.
  - **Insider Threats**: Employees causing harm.
  - **Script Kiddies**: Novices using existing tools.

---

*This condensed cheat sheet includes detailed Threat Modeling steps, key points on attack trees, and a concise OWASP Top 10 table with examples, all formatted to maximize space and avoid unnecessary headings or one-word lines.*