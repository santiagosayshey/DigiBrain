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


### Design Choices

For our protocol implementation, we opted to write the entire backend in Python and use a React frontend, all deployed using Vite and Docker. The decision to use Docker played a pivotal role in our deployment strategy, enabling us to dynamically configure deployment parameters like message retention, ports, and IP addresses. Docker's containerization not only ensures consistency across different environments but also mitigates many of the dependency issues that were prevalent in the other implementations we reviewed. This approach allows our solution to be deployed seamlessly, with minimal setup required beyond Docker itself.

A significant benefit of using Docker was its ability to eliminate device-specific issues by packaging everything into containers. Many other implementations faced challenges with missing dependencies or ambiguous setup instructions, but Docker resolves these by bundling the entire environment. This also means our implementation could, theoretically, be deployed straight out of the box.

In terms of language choices, we stuck to those we were most familiar with, primarily Python for the backend. While I considered experimenting with Rust or Go to gain some hands-on experience with those languages, the limited timeframe and the need to keep the codebase accessible to my team deterred me from doing so. Instead, I focused on ensuring that our implementation was as modular as possible. We created shared utilities, such as message structure and cryptographic compliance modules, which could be independently unit tested before being integrated into the larger system. This approach aligns with the test-driven development (TDD) methodology we followed, where our tests ensured compliance with the protocol and security standards even before the client-server architecture was fully built.

A particular challenge we faced was addressing the issue of public chat broadcast storms, as we had to strictly adhere to the protocol without introducing extra fields. To prevent broadcast storms, we implemented a strategy where public messages were split into individual messages with a specific recipient in mind. This design ensured that once a server received a message, it wouldn’t forward it, avoiding the broadcast loop that would have otherwise occurred.

Our implementation can also run headlessly, without the React frontend, which means that the API layer is robust enough to allow direct interaction with clients. However, this decision introduced a tradeoff between security and functionality, particularly with regard to the choice of using Flask's API versus WebSockets for communication. While Flask simplifies the architecture, it could potentially be a weaker point in terms of security, though we ensured that it remains protocol-compliant and secure for the majority of use cases.

### Code Demonstration

For this section, I will walk through the actual deployment steps rather than the simplified ones we used for testing purposes, where premade Docker Compose files and setup scripts were provided to streamline the process for reviewers.

1. **Initial Setup**: Users need to configure their Docker Compose files according to their preferred settings—such as IP addresses, ports, and message retention policies. While this process could be more user-friendly, it wasn't feasible within the project timeline to implement a more seamless solution. Ideally, the client-server module could be unified, reducing the number of settings users need to adjust.
   
   - _Note_: Users unfamiliar with Docker or Compose may find this setup slightly challenging, though this was not flagged as an issue during peer reviews.
   
2. **Deployment**: Once the Compose files are configured, users can create the necessary client containers, which gives them full access to the application. After setting up the containers, users can navigate to the web interface and begin messaging with other clients.
   
   _In hindsight, integrating the clients and servers into a single module would simplify the user experience, especially for those less familiar with Docker. This is something we would have liked to explore further given more time._

3. **Interaction**: The system supports both public and private messaging, as well as file transfers between clients. Below is an example of the system running with three clients, demonstrating public chats visible to all participants, private chats between two clients, and a public file transfer.

- Placeholder for image 1 (showing 3 clients communicating)
- Placeholder for image 2 (showing public file transfer)

### Interoperability Testing

Our testing process involved manual exchanges of public keys, IP addresses, and ports, as specified by the protocol. To facilitate this, we added routes for sharing internal public keys and downloading external ones. I set up an external Hetzner server running a basic Ubuntu virtual machine to host the client-server for these tests. All tests were conducted in an isolated environment.

Once the necessary information was exchanged, the servers attempted to establish WebSocket connections, and we tested message exchanges and file transfers. We performed interoperability testing with five different groups, and the results are detailed below.

#### Group 38 (Chun Hon Chan, Lok To Lo, Yin Cyrus Hui, Zachary Sobarzo)
- Our initial testing revealed significant issues for both our group and theirs. Our group mistakenly sent base64-encoded client updates and hellos, rather than PEM-encoded lists, causing issues with client lists on both sides. On the other hand, their group failed to include counters in their messages, which triggered our system’s replay attack detection, preventing those messages from being processed.

- Placeholder for image 3 (showing message interactions and discrepancies)

#### Group 17 (Gregorius Baswara Wira Nuraga, Kyle Johnston, Ivan Tranquilan)
- After addressing the issues from the previous tests, this group’s testing was much smoother. A minor issue we identified in our implementation was the need to request client updates when connecting, rather than waiting for one to be sent. Their group had issues with generating public/private keys for receiving private messages and adding signatures to private messages, but these were quickly resolved.

- Placeholder for image 4 (showing private message exchange)
- Placeholder for image 5 (showing successful connection and message exchange)

#### Test 4  
(Placeholder for results)

#### Test 5  
(Placeholder for results)

This section outlines the major interoperability testing we conducted. More details, including images and specific examples of successful message exchanges, are provided in the appendices and README documentation.