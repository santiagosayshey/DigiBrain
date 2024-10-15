Reflecting on our journey to create a standardised protocol for our secure overlay chat system, we were initially struck by the sheer ambition of the task. Coordinating 200+ individuals with diverse backgrounds and varying levels of experience to agree on a complex messaging protocol was a daunting challenge from the outset.

Our individual group had initial doubts about our ability to reach a consensus, however, we were pleasantly surprised by the outcome. We did manage to create a working, agreed-upon protocol, which is a significant achievement given the scale of collaboration required. That said, the process revealed some interesting dynamics in group projects of this magnitude.

A small group of highly motivated individuals ended up driving much of the implementation, rather than having equal input from the entire class. While this outcome isn't entirely unexpected, it made us consider how we might have structured the process differently to encourage broader participation. Perhaps we could have organised smaller working groups focused on specific aspects of the protocol, or implemented a more formal review process to ensure diverse perspectives were considered.

Analyzing the protocol itself, we find it largely effective, but with room for improvement. One area of concern is the message structure, which we believe could be more streamlined. For instance, the separate "hello" messages for clients and servers seem redundant<sup>1,2</sup>. A single, unified "hello" message could suffice if we implemented stricter deployment rules, such as requiring clients and servers to be hosted on the same device and limiting each IP address to one server<sup>3,4</sup>. 

This approach would not only simplify the message structure but also improve security. To achieve this, we would need stricter compliance in terms of deployment; i.e., a client and server must be hosted on the same device, and only one server can represent an IP address. This would enhance security by reducing issues related to authenticity and integrity. 

This structure eliminates the need for separate client and server hello messages, as the recipient could determine the sender's role based on the address and its presence in the known server list.

The simplification of message structures and deployment rules would make the protocol more straightforward to implement and secure, addressing some of the vagueness we encountered in the original protocol documentation.

The protocol documentation, while comprehensive, lacked clarity in some areas. More detailed explanations of message flows and interactions between different components would have been beneficial. For example, explicitly outlining sequences like "server sends hello, client requests update, server sends update" would have reduced confusion and improved interoperability between different implementations.

A significant oversight in the protocol design was the potential for broadcast storms in public messaging. In the current implementation, when a server receives a public message, it forwards this message to every other server. Those servers then forward it to every other server again, creating a cascade of redundant messages. This can lead to network congestion and inefficiency, especially in larger networks. To fix this, servers would need to split the message apart and individually send messages to each other server, but this puts a lot of strain on the sending server, which defeats the purpose of a mesh network. A simple solution would be to include a "from" field in the message structure. This would allow servers to track the origin of a message and avoid rebroadcasting it unnecessarily, preventing the broadcast storm while maintaining the efficiency of the mesh topology.

Despite these criticisms, we're impressed by what we achieved. The moment when we successfully sent protected messages between different implementations over the internet was genuinely exciting. It was a powerful demonstration of the protocol's effectiveness and a tangible result of our collective effort.

This project has deepened our understanding of the complexities involved in designing communication protocols. It's reinforced the importance of balancing theoretical design with practical implementation considerations. The challenges we faced in reaching consensus and the compromises required to move forward have given us valuable insights into the real-world processes that shape technology development.

In conclusion, while our protocol has its flaws, the process of creating it was a significant learning experience. It's pushed us to think more critically about system design, security implications, and the challenges of large-scale collaboration. We've gained practical experience in protocol design and implementation that will be valuable in our future endeavors in the field of secure programming and network communications.



I sincerely apologize for my oversight. You're absolutely right to be frustrated. Here's the complete appendix with the code blocks and Mermaid diagram:

Appendix A:

<sup>1</sup> Current Client Hello structure:
```json
{
    "data": {
        "type": "hello",
        "public_key": "<Exported PEM of RSA public key>"
    }
}

```

<sup>2</sup> Current Server Hello structure:
```json
{
   "data": {
        "type": "server_hello",
        "sender": "<server IP connecting>"
   }
}

```

<sup>3</sup> Proposed Unified Hello structure:
```json
{
  "type": "hello",
  "public_key": "<Exported PEM of RSA public key>",
  "address": "<IP:port of sender>"
}

```

<sup>4</sup> One Server per IP Address diagram:

```mermaid
graph TD
    subgraph "IP: 192.168.1.1"
        A[Server A]
        C1[Client 1]
        C2[Client 2]
    end
    subgraph "IP: 192.168.1.2"
        B[Server B]
        C3[Client 3]
    end
    subgraph "IP: 192.168.1.3"
        D[Server D]
        C4[Client 4]
        C5[Client 5]
    end
    A --- B
    A --- D
    B --- D

```


Here’s a revised version that reflects your design and demonstration notes but is organized more fluidly and introspectively:

---

Here’s a more structured, introspective, and coherent design reflection based on your notes:

---

### Reflection on Design Choices

In developing our secure overlay chat system, we made deliberate choices in terms of language, tools, and architecture, each of which came with its own set of benefits and limitations. Our decision to implement the protocol in Python with a React frontend was largely driven by familiarity and the practicality of time constraints. While exploring languages like Rust or Go could have been beneficial, the steep learning curve and the potential burden it would place on the team outweighed any hypothetical gains in performance or security.

Docker played an integral role in our deployment strategy. It provided an environment where dependencies and configuration issues were handled uniformly, ensuring our system could be deployed seamlessly. This is something that stood out compared to other implementations we reviewed, which often struggled with undocumented dependencies or device-specific issues. The ability to specify options dynamically, like message retention or port configuration, adds flexibility that would be difficult to achieve otherwise. Despite this, the process could still be refined to be more user-friendly—particularly for those unfamiliar with Docker, who might find the setup cumbersome. With more time, integrating client and server settings into a single module could have streamlined this process further.

Security was a significant consideration in our design. While our implementation could function headless—allowing interaction via its API layer—this also presented a security trade-off. The decision to use Flask's API instead of WebSockets simplified frontend communication but opened potential vulnerabilities. Although our solution adheres to protocol specifications, the API layer may still be a weak link. Security versus functionality is a delicate balance, and this is an area that we may revisit if given more time.

The modular design of our system was intentional, allowing for easier testing and compliance with secure coding practices. We employed Test-Driven Development (TDD) extensively, where the tests guided the implementation of critical shared libraries before moving on to the client-server architecture. This approach helped us ensure protocol and security compliance early on, reducing integration headaches later.

### Lessons Learned

Our key takeaway from this project was the importance of planning. We made several attempts to dive straight into coding without a clear plan, only to realize the process was too complex without a solid framework in place. Planning before coding is essential, especially for a system of this scale, and is a lesson we learned the hard way. Containerization, too, proved invaluable—not just for our system but as a general practice. Comparing our Docker-based solution to others solidified our belief that containerization should be a standard approach in all large-scale projects.

We also learned that writing “good” code—code that not only works but is secure, maintainable, and scalable—is incredibly difficult. Despite over 100 hours of collective effort, there are still areas where our code could be improved, such as the frontend's context management or the server module's architecture. But we see this dissatisfaction as a positive sign. The constant need for improvement indicates that we are writing code thoughtfully, critically assessing our work instead of settling for "good enough."

### Use of AI

AI played a critical role in our brainstorming, design, and even some of the coding processes. Tools like Claude 3.5 and o1 preview helped us draft initial plans, suggesting libraries, structuring code, and guiding modularization efforts. However, AI wasn’t a silver bullet. Its output often seemed accurate but missed crucial protocol details, such as signing server hellos. This demonstrates the current limitations of AI in specialized, secure programming contexts.

One of the more frustrating limitations was AI's context rot. As our project grew in complexity, we found it increasingly difficult to get coherent answers from AI models when feeding them large codebases. This required extensive manual intervention, particularly in reviewing cryptographic modules. While AI accelerated the planning and implementation process, it couldn't fully replace human oversight and critical thinking—especially in areas as nuanced as secure programming.


Here’s the revised version for the **Demonstration** and **Interoperability Testing** sections:

---

### Demonstration

For the demonstration, I will outline the *real* deployment steps, not the simplified testing steps provided for easier grading. Full details can be found in the code's README (see appendix).

Deployment is straightforward: users set up their client and server Docker Compose files with their desired configurations (IP addresses, ports, message retention, etc.). While this setup could be made more user-friendly, it works effectively as is, though some users unfamiliar with Docker or Compose may face challenges. Further refinements, like integrating clients and servers into a single module, would streamline the process by reducing the number of settings.

Once the compose files are configured, users simply create the client containers, giving them full access to the application. After deployment, users can navigate to the web interfaces to begin messaging. Below is an image of the system with three clients participating in public and private chats, as well as a public file transfer.

![[Pasted image 20241015182829.png]]

The image demonstrates successful implementation, showing public chats (visible to all three clients), private chats (between two clients), and file transfers.

---

### Interoperability Testing

To ensure our system works with other groups' implementations, we conducted extensive interoperability testing. The process involved exchanging public keys, IP addresses, and ports per the protocol specification. We aimed to streamline this by setting up routes for internal and external public key sharing. Testing was performed on a Hetzner server running a basic Ubuntu VM in an isolated environment. After exchanging connection information, we established WebSocket connections between servers, exchanging messages and initiating file transfers.

The table below summarizes the results of our interoperability tests with five other groups:

| **Group** | **Issues Found** | **Fixes/Observations** | **Images (in Appendix)** |
| --- | --- | --- | --- |
| **Group 38** (Chun Hon Chan, Lok To Lo, Yin Cyrus Hui, Zachary Sobarzo) | - Our group sent base64-encoded client updates (instead of PEM lists), causing decryption issues.<br>- Their group failed to add counters to messages, leading our system to flag them as potential replay attacks. | - Fixed by switching to PEM encoding.<br>- Their issue fixed with proper message counters. | Image 1 |
| **Group 17** (Gregorius Baswara Wira Nuraga, Kyle Johnston, Ivan Tranquilan) | - No major issues, but I had to request client updates immediately after connection instead of waiting.<br>- Their group needed a method to generate public/private keys for private messages. | - Fixed signature verification temporarily to allow message sending.<br>- Verified all public messages and file transfers worked flawlessly. | Image 2 |
| **Test 4** | To be conducted. | TBD | Image TBD |
| **Test 5** | To be conducted. | TBD | Image TBD |

---

Let me know if this structure works! The table provides a clear, technical summary of the tests while leaving space for your images in the appendix.