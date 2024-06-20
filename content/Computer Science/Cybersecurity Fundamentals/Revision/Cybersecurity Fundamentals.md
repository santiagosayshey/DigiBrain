> [!summary] Week 1
> - **Cybercrime Existence**: Heavy reliance on IT systems, exploitation for profit, diverse motivations, and ease of execution.
> - **Asymmetric Sides**: Attackers have advantages in time, money, law, and success factors compared to defenders.
> - **Hacker vs. Cracker**: "Crackers" are cybercriminals, while "hackers" originally referred to skilled programmers.
> - **Ethical Hackers**: Use their skills to protect and defend against cyber attacks.
> - **Hacker Hats**: Black hat (illegal activities), white hat (defensive security), and grey hat (between legal and illegal).

> [!summary] Week 2
> - **Cryptography**: Practical development and study of encryption systems.
> - **Cryptology**: Academic study of encryption and their properties, cryptographical systems, and cryptanalysis.
> - **Cipher Types**: Caesar, Vigenère, Substitution, Polygraphic Substitution, and Transposition ciphers.
> - **XOR Cipher**: Performs XOR operation on plaintext and key, forming the basis of the "one-time pad" cipher.
> - **Symmetric Ciphers**: Use the same key for encryption and decryption, with modes like ECB and CBC.
> - **Key Exchanges**: Diffie-Hellman and RSA enable secure key exchange over insecure channels.
> - **Hashes**: Used for password security and verifying digital signatures.

> [!summary] Week 3
> - **C.I.A**: Cybersecurity protects Confidentiality, Integrity, and Availability of systems and data.
> - **Breaching C.I.A**: Achieved through targeting systems and humans using various techniques.
> - **Protecting C.I.A**: Involves security testing, firewalls, IPS, antimalware, education, secure design, and more.
> - **Security Assessment Types**: Black box, white box, automated, manual, dynamic, static, application-specific, and open-ended.
> - **Penetration Testing**: Simulated cyberattack to evaluate the security of a system, involving planning, reconnaissance, scanning, exploitation, and reporting.
> - **Vulnerability Assessment**: Identifying known security issues using automated tools, with credentialed and non-credentialed scanning.

> [!summary] Week 4
> - **The Internet**: A global network providing best-effort delivery of packets between connected hosts.
> - **Network Protocols**: Define how hosts communicate, with layers like application, transport, network, data link, and physical.
> - **IP, ARP, and DHCP**: Protocols for packet forwarding, address resolution, and dynamic IP assignment.
> - **Ports**: Identify applications on a host machine, with well-known ports for specific services.
> - **UDP and TCP**: Transport layer protocols, with UDP being connectionless and TCP using a three-way handshake.
> - **TCP Connection Termination**: Involves the exchange of FIN and ACK segments to gracefully close a connection.
> - **Scanning**: Methodical process to uncover network structure, hosts, and applications, revealing vulnerabilities and aiding in exploitation.

> [!summary] Week 5
> - **Control Hijacking Attacks**: Attempt to take over the target machine by exploiting vulnerabilities to execute arbitrary code.
> - **Buffer Overflow**: Occurs when a program writes more data to a buffer than it can hold, potentially corrupting important data or allowing code execution.
> - **Format String Attacks**: Exploit improper handling of user input in output functions, leading to information disclosure or code execution.
> - **Integer Overflow**: Happens when an arithmetic operation creates a numeric value outside the representable range, causing unexpected behavior or vulnerabilities.
> - **Heap Exploits**: Techniques like heap overflow, vtable corruption, heap spraying, and use-after-free to manipulate the heap and execute malicious code.
> - **Defense Mechanisms**: Address Space Layout Randomization (ASLR), stack canaries, non-executable memory (DEP), and Control Flow Integrity (CFI) help mitigate exploitation.

> [!summary] Week 6
> - **Heap vs. Stack Memory**: Heap is dynamically allocated, stores objects and large data structures, and is manually managed. Stack is fixed, stores local variables and function calls, and is automatically managed.
> - **Heap Overflow Vulnerabilities**: Occur when a program writes more data to a heap-allocated buffer than it can hold, potentially corrupting adjacent data or allowing code execution.
> - **Virtual Table (vtable) Corruption**: Exploits the virtual function table in C++ objects to hijack the object's behavior and execute malicious code.
> - **Heap Spraying**: Technique to increase the reliability and exploitability of memory corruption vulnerabilities by filling the heap with malicious code.
> - **Use-After-Free (UAF) Exploits**: Occur when a program continues to use a pointer to an object after it has been freed, leading to undefined behavior and potential exploitation.

> [!summary] Week 7
> - **Sniffing**: The process of capturing and analyzing network traffic using packet analyzers, which can be used for legitimate purposes or maliciously to capture sensitive data.
> - **Man-in-the-Middle (MITM) Attacks**: Involve intercepting communication between two parties by exploiting the Address Resolution Protocol (ARP) and manipulating the ARP cache of network devices.
> - **DHCP Attacks**: Similar to ARP spoofing, attackers can spoof DHCP responses to provide malicious configurations to clients.
> - **DDoS Attacks**: Attempt to disrupt the normal traffic of a targeted system by overwhelming it with a flood of Internet traffic from multiple sources, often using botnets.
> - **DNS Attacks**: Include DNS poisoning (or spoofing) and DNS hijacking, which exploit vulnerabilities in the Domain Name System to redirect traffic to malicious servers.
> - **WiFi Attacks**: Exploit weaknesses in WiFi security protocols like WEP and WPA/WPA2, using techniques such as WEP cracking, dictionary attacks, and exploiting weak PSKs.
> - **Firewalls and IDS**: Network security devices that monitor and control network traffic based on predetermined security rules and detect suspicious activities.

> [!summary] Week 8
> - **The Web**: A collection of interconnected documents and resources, accessible over the internet using web browsers and served by web servers.
> - **URL Anatomy**: URLs consist of a scheme, domain, path, and optional query parameters to uniquely identify and access web resources.
> - **Web Application Analysis**: Involves using developer tools (like Chrome DevTools) and local proxy tools (like Burp Suite) to inspect, debug, and analyze web applications.
> - **PHP**: A server-side scripting language used to create dynamic web pages, interact with databases, and handle user input.
> - **SQL Injection (SQLi)**: A web application vulnerability that allows attackers to inject malicious SQL queries into application inputs, potentially leading to data breaches and unauthorized access.
> - **Preventing Web Attacks**: Techniques include input validation, parameterized queries, sanitization, using safe APIs, applying the least privilege principle, and keeping software up to date.

> [!summary] Week 9
> 
> 1. **JavaScript and Web Exploits**: JavaScript's versatility and browser support make it a target for attackers seeking to exploit web applications through techniques like Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF).
> 
> 2. **Cross-Site Scripting (XSS)**: XSS vulnerabilities allow attackers to inject malicious scripts into web pages viewed by other users. There are two main types of XSS:
>    - Stored XSS: Malicious scripts are injected into a website's database and delivered to users' browsers.
>    - Reflected XSS: Malicious scripts are injected through URL parameters or form inputs and reflected back to the user's browser.
> 
> 3. **Session Hijacking via XSS**: XSS attacks can facilitate session hijacking by stealing session cookies and sending them to a malicious server, allowing attackers to impersonate victims and access their accounts.
> 
> 4. **Cross-Site Request Forgery (CSRF)**: CSRF attacks exploit the trust a website has in a user's browser. Attackers trick authenticated users into performing unwanted actions on a target website without their knowledge or consent.
> 
> 5. **Server-Side Request Forgery (SSRF)**: SSRF vulnerabilities arise when a web application accepts user-supplied input to make requests to other systems or resources on the server-side, allowing attackers to access internal resources or perform unauthorized actions.
> 
> 6. **Forced Browsing and Directory Bursting**: These techniques involve manually crafting URLs or using automated tools to discover and access restricted web pages, directories, or files that are not intended to be public.
> 
> To mitigate these vulnerabilities, it is crucial to implement proper input validation, output encoding, secure cookie handling, CSRF protection, and follow best practices for web application security.

> [!summary] Week 10
> 
> - **DFIR**: Digital forensics and incident response involve identifying, preserving, analyzing, and presenting digital evidence while managing the aftermath of cyber-attacks.
> - **DFIR Phases**: Identification, preservation, analysis, documentation, and presentation.
> - **DFIR Areas**: Computer forensics, network forensics, mobile device forensics, cloud forensics, and malware forensics.
> - **CIRT**: A Cyber Incident Response Team (CIRT) is a group of professionals tasked with responding to and managing cybersecurity incidents.
> - **Logs**: Records of activities and events on a system or network, essential for understanding incidents and identifying involved parties.
> - **Forensic Tools**: Tools for file format identification (`file`), file carving (`dd`), searching for plaintext (`strings`) and binary/hex strings (`hexdump`), and extracting metadata (`exiftool`).
> - **Packet Traces**: Capturing and analyzing raw network packets using tools like Wireshark to identify malicious activity.
> - **Network Logs**: Records of activities on network devices like firewalls, routers, and intrusion detection systems, useful for tracing an attacker's actions and timeline.
> - **Steganography**: The practice of concealing secret information within non-secret data, such as in text, images (spatial or frequency domain), or videos.
> - **Steganalysis**: The process of detecting the presence of steganography within files using techniques like statistical analysis, pixel pattern examination, machine learning algorithms, and carrier file analysis.
> - **x86 Architecture**: Specifies how software and hardware interact, determining instruction processing and data management. Important for reverse engineering due to prevalence, documentation, and compatibility.
> - **x86 Registers**: EIP (instruction pointer), ESP (stack pointer), and EBP (base pointer) are crucial for managing execution flow and stack operations.
> - **Reverse Engineering**: The process of analyzing a software system to identify components and interrelationships, creating higher-level representations. Involves disassembly, decompilation, static analysis, and dynamic analysis.
> - **Disassemblers and Decompilers**: Tools for converting machine code into assembly language (disassemblers) or high-level code (decompilers) for analysis and understanding.
> - **Static vs. Dynamic Analysis**: Static analysis examines code without execution, while dynamic analysis observes runtime behavior.
> - **Ghidra**: A powerful open-source reverse engineering tool supporting disassembly, decompilation, and interactive analysis.

> [!summary] Week 11
> - **Security Engineering**: The practice of designing, implementing, and maintaining software systems with a focus on protecting against potential security threats.
> - **Security Engineering Principles**: Include keeping security simple, making it usable, applying least privilege, defense in depth, zero trust, security by default, fail securely, and risk-informed decision making.
> - **Information Security and Risk Management**: Involves protecting the confidentiality, integrity, and availability of information assets by efficiently deploying security controls.
> - **Assessing and Treating Risks**: Risks are identified, assessed based on likelihood and impact, and treated through acceptance, transfer, mitigation, or avoidance.
> - **Security Controls**: Measures put in place to mitigate risks, categorized as administrative, physical, or technical, and functioning as preventive, detective, or corrective.
> - **Security Operations**: Manages and protects an organization's information systems through continuous monitoring, detection, and response to security threats and incidents.

> [!summary] Week 12
> - **Importance of Cyber Ethics and Legality**: In the digital age, understanding and navigating the ethical and legal implications of cyber activities is crucial to avoid unintended consequences and maintain trust.
> - **Cyber Ethics vs. Cyber Legality**: Cyber ethics deals with moral principles guiding digital behavior, while cyber legality encompasses laws and regulations governing online activities.
> - **Ethical Reasoning Approaches**: Teleology focuses on consequences, deontology emphasizes moral duties, and Ross' list of prima facie duties includes fidelity, reparation, gratitude, justice, beneficence, self-improvement, and non-maleficence.
> - **Relationship between Ethics and Law**: Ethical principles may align with, conflict with, or lead to adherence to laws while advocating for change.
> - **Case Study: ERP Vulnerability in Healthcare**: Illustrates the complex interplay between ethical considerations (patient care, security) and legal obligations (GDPR compliance) in cybersecurity.
> - **Ethical Considerations in Penetration Testing**: Authorization, transparency, confidentiality, and responsibility are key ethical principles to maintain trust and uphold the integrity of the profession.
> - **Legal vs. Ethical Issues**: Examples demonstrate that while some cyber issues are clearly illegal or unethical, others may fall into a gray area where legal and ethical dimensions do not perfectly align.

![[1.1 Cybersecurity Overview]]

![[2.1 Applied Cryptography]]

![[3.1 Security Assessment and Testing]]

![[4.1 Networks]]

![[4.2 Scanning]]

![[5.1 Control Hijacking Attacks]]

![[5.2 Buffer Overflow]]

![[5.3 Format String Attacks]]

![[5.4 Integer Overflow]]

![[6.1 Heap Exploits]]

![[6.2 Defence]]

![[7.1 Sniffing]]

![[7.2 Man in the Middle]]

![[7.3 DHCP]]

![[7.4 DDoS]]

![[7.5 DNS Attacks]]

![[7.6 WiFi Security]]

![[7.7 Firewalls & IDS]]

![[8.1 The Web]]

![[8.2 HTTP]]

![[8.3 Analysing Web Apps]]

![[8.4 PHP]]

![[8.5 SQLi]]

![[9.1 Javascript]]

![[9.2 Cross Site Scripting]]

![[9.3 Cross-Site Request Forgery]]

![[9.4 Server-Side Request Forgery]]

![[9.5 Directory Bursting]]

![[10.1 Digital Forensics]]

![[10.2 Stenography]]

![[10.3 Assembly]]

![[10.4 Reverse Engineering]]

![[11.1 Security Engineering]]

![[11.2 Information Security and Risk Management]]

![[11.3 Security Operations]]

![[12.1 Cyber Legality]]

![[12.2 Cyber Ethics]]

![[12.3 Legal vs. Ethical]]


| Operator      | Description                                               | Example                                      |
|---------------|-----------------------------------------------------------|----------------------------------------------|
| `site:`       | Searches only within a specified site or domain.          | `site:example.com`                           |
| `intitle:`    | Finds pages that include a specific word in their title.  | `intitle:recipe`                             |
| `inurl:`      | Finds pages that include a specific word in their URL.    | `inurl:profile`                              |
| `intext:`     | Searches for words in the text of the page.               | `intext:"important dates"`                   |
| `filetype:`   | Searches for files of a specific filetype.                | `filetype:pdf`                               |
| `related:`    | Finds websites related to a specified URL.                | `related:example.com`                        |
| `cache:`      | Shows the most recent cached version of a webpage.        | `cache:example.com`                          |
| `-"keyword"`  | Excludes pages containing a specific keyword.             | `Jaguar speed -car`                          |
| `"keyword"`   | Searches for the exact phrase matched.                    | `"famous speech"`                            |
| `AROUND(N)`   | Finds pages that have two words or phrases within N words of each other. | `solar AROUND(4) energy` |

Here's a simple markdown table with common web attacks, their explanations, examples, and prevention methods:

| Attack | Explanation | Example | Prevention |
|--------|-------------|---------|------------|
| SQL Injection (SQLi) | Inserting malicious SQL code into application queries | `' OR '1'='1` in a login form | Use parameterized queries |
| Cross-Site Scripting (XSS) | Injecting malicious scripts into web pages | `<script>alert('XSS')</script>` in a comment field | Sanitize user input, use Content Security Policy |
| Cross-Site Request Forgery (CSRF) | Tricking users into performing unwanted actions | `<img src="http://bank.com/transfer?amount=1000&to=attacker">` | Use CSRF tokens, SameSite cookies |
| Server-Side Request Forgery (SSRF) | Making the server perform unintended requests | `http://internal-api/delete-user?id=1` | Validate and sanitize user-supplied URLs |
| Man-in-the-Middle (MITM) | Intercepting communication between two parties | ARP spoofing to redirect traffic | Use HTTPS, certificate pinning |
| Directory Traversal | Accessing files outside the intended directory | `../../../etc/passwd` in a file path | Sanitize file paths, use whitelists |


| Framework | Main Purpose | Certification |
|-----------|--------------|---------------|
| ISO/IEC 27000 Series | Information security management framework | Yes (ISO 27001) |
| NIST Cybersecurity Framework | Best practices for managing and reducing cybersecurity risk | No |
| CIS Critical Security Controls | Specific actions for cyber defense | No |
| ACSC Essential 8 | Baseline strategies for mitigating cyber incidents | No |
| PCI-DSS | Security standard for organizations handling credit card data | Yes |
| COBIT | Framework for IT management and governance | No* |
