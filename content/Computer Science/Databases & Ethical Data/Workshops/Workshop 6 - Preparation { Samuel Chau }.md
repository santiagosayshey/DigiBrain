## Question 1

```
List four physical threats and how you would protect from attacks on those vectors.
```



## Question 2

```
List four digital threats and how you would protect from attacks on those vectors.
```

1. Network Attacks:
   - **Threat**: These involve unauthorized actions targeted at disrupting, degrading, or destroying the integrity of data in transit over a network. Examples include Denial of Service (DoS) attacks, Man-in-the-Middle (MitM) attacks, and packet sniffing.
   - **Protection**: Implement robust network security measures such as firewalls and secure network protocols like HTTPS and SSL/TLS for data transmission. Regularly update and patch network devices. Also, conduct routine network security assessments and penetration testing.

2. Console Attacks:
   - **Threat**: Console attacks are direct attacks on a system, usually gained by having physical access to a device or remote access to the system console. Once access is gained, an attacker can execute malicious commands or alter system configurations.
   - **Protection**: Use strong access controls for system consoles, including multi-factor authentication. Regularly update and patch operating systems and applications. 

3. Worms:
   - **Threat**: Worms are malware that replicate themselves to spread to other computers over a network, often causing harm by consuming bandwidth or sending spam.
   - **Protection**: Employ updated antivirus and antimalware software on all systems and perform regular system scans. Use firewalls to control network traffic. Conduct regular security awareness training for employees to prevent phishing attacks, which are often used to deliver worms. Also, keep all systems patched and up-to-date.

4. Backdoors:
   - **Threat**: Backdoors are typically malicious software or hardware mechanisms designed to bypass normal authentication or encryption in a system, allowing unauthorized remote access.
   - **Protection**: Regularly perform security audits and code reviews to detect backdoors in software and hardware. Employ comprehensive endpoint security solutions and maintain updated firewalls. 

## Question 3 

```
Give an example of data inconsistency and how it could occur.
```

- Consider a banking transaction involving two accounts: Account A transfers an amount of x dollars to Account B. A data inconsistency would arise if the amount is deducted from Account A but not credited to Account B.

- This inconsistency can occur due to a variety of reasons, such as system crashes or failures during the transaction process, database write errors, or a break in the transaction sequence due to network issues. If there isn't a proper mechanism in place to ensure atomicity (where the whole transaction is either completed fully or rolled back entirely), such inconsistencies can persist, leading to discrepancies in account balances and potential issues in account reconciliation.
## Question 4  

```
Give an example of a NOSQL database and its uses.
```

MongoDB is a popular NoSQL database that is document-oriented, comprising of sets of key-value pairs. 

In the context of a hospital setting, MongoDB can be highly beneficial for maintaining patient records. Given the diverse range of data associated with patients (medical histories, diagnostic test results, imaging data, prescription records, etc.), MongoDB's dynamic schema allows hospitals to store a wide variety of patient data without having to define a fixed structure first. This makes it easier to incorporate new types of data as medical practices evolve or mould to different patients that require different information to be stored.
## Question 5

```
What are the overheads of NOSQL databases when compared against SQL databases? What are the benefits?
```

**Disadvantage - Consistency Models:** Many NoSQL databases use eventual consistency instead of the strict consistency model used in SQL databases. While this supports high availability, it may lead to temporary inconsistencies in data, which could be problematic for applications that require real-time consistent data.

**Advantage - Flexibility:** NoSQL databases, especially document-oriented ones, offer a flexible schema. This is advantageous for datasets that evolve over time, allowing developers to work without stringent constraints.