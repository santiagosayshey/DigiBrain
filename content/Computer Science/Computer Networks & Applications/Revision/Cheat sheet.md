> [!idea] Introduction to Networks
> A network is a collection of interconnected devices that can communicate and share resources with each other. Networks consist of:
> - Nodes: Devices connected to the network, such as computers, smartphones, servers, routers, and switches.
> - Links: Connections between nodes, which can be wired (e.g., Ethernet) or wireless (e.g., Wi-Fi, cellular).
> - Protocols: Sets of rules and standards that govern the communication between nodes, ensuring interoperability and efficient data transfer.


> [!idea] Postal Analogy
> - The OSI model layers can be likened to Russian nesting dolls, where each layer adds its own "envelope" of header information.
> - As data passes from upper to lower layers, it's encapsulated with protocol-specific information at each stage.
> - The process is reversed at the receiving end, with each layer removing its corresponding header information.

# Application Layer

> [!idea] Delay Types
> | Delay Type         | Description                                                                                                            | Formula                                                 |
> | ------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
> | Propagation Delay  | The time it takes for a signal to travel from point A to point B over a network medium.                                | $$t_p = Distance / Speed$$                              |
> | Transmission Delay | The time required to transmit all the bits of a packet into the network medium.                                        | $$t_T = L / R$$ where L is packet size and R is bandwidth |
> | Queuing Delay      | The time a packet spends waiting in a queue before it can be transmitted due to congestion or prior packet processing. | Depends on queue length and network traffic             |
> | Processing Delay   | The time taken by a network device (e.g., router, switch) to process a packet.                                         | Depends on device and packet complexity                 |

> [!idea] Peer-to-Peer (P2P) Networks
> - Decentralized model where each peer acts as both client and server
> - Peers share resources (files, content, bandwidth) directly without central coordination
> - Torrents (shared resources) are split into chunks; peers send and receive chunks they have/need
> - Rarest chunks are prioritized; peers connect with their 4 most connectable neighbors
> - Trackers monitor torrent swarms and facilitate peer connections
> - P2P performance depends on peer upload/download rates and file distribution among peers

> [!idea] Client-Server vs. Peer-to-Peer (P2P)
> - Client-Server: Centralized model where a server serves multiple clients. Performance depends on server capacity and client-server communication.
> - P2P: Decentralized model where each peer acts as both client and server. Performance depends on peer upload/download rates and file distribution among peers.

> [!idea] DNS (Domain Name System)
> - Translates domain names to IP addresses, enabling user-friendly website access.
> - Hierarchical, distributed database with Root, TLD, and Authoritative servers.
> - Iterative Queries: Contacted server replies with the name of the next server to contact.
> - Recursive Queries: DNS servers handle the complete resolution process on behalf of the client.
> - DNS Records: A (IP address), NS (name server), CNAME (canonical name), MX (mail exchange).

> [!idea] HTTP (Hypertext Transfer Protocol)
> - Request-response protocol for client-server communication.
> 
> | HTTP Version | Characteristics                                                                |
> |--------------|--------------------------------------------------------------------------------|
> | HTTP/1.0     | Non-persistent, each connection used for a single request-response.            |
> | HTTP/1.1     | Persistent, allows connection reuse for multiple requests, reducing overhead. |
> 
> - Caching/Proxies: Stores frequently accessed data closer to clients, reducing server load and response times.
> - Pipelining: Allows multiple requests to be sent without waiting for each response, improving efficiency.

# Transport Layer

> [!idea] Transport Layer Services
> - Provides logical communication between processes on different hosts
> - Key services: multiplexing, demultiplexing, and reliable data transfer
> - Uses port numbers to identify sending and receiving processes
> - Sockets provide the API between the application and transport layers

> [!idea] TCP (Transmission Control Protocol)
> - Connection-oriented, reliable, byte-stream protocol
> - Provides flow control, congestion control, and error recovery
> - Uses three-way handshake for connection establishment and four-way handshake for termination
> - Employs cumulative ACKs and sequence numbers for reliability
> - Implements congestion control mechanisms (slow start, congestion avoidance, fast retransmit, fast recovery)

> [!idea] UDP (User Datagram Protocol)
> - Connectionless, unreliable, message-oriented protocol
> - Provides minimal error checking and no flow or congestion control
> - Suitable for applications that prioritize low latency over reliability (e.g., streaming, gaming)
> - Smaller header size compared to TCP

> [!idea] Multiplexing and Demultiplexing in UDP
> - UDP uses destination IP and port number for demultiplexing
> - Multiple packets with the same destination IP and port are delivered to the same socket
> - Source IP and port are used for sending replies back to the sender

> [!idea] Multiplexing and Demultiplexing in TCP
> - TCP uses a 4-tuple (source IP, source port, destination IP, destination port) for demultiplexing
> - Each unique 4-tuple combination is delivered to a separate socket
> - Allows multiple sockets to be associated with the same port number on a host

> [!idea] Go-Back-N (GBN) Protocol
> - Sender can transmit multiple packets without waiting for individual ACKs
> - Receiver sends cumulative ACKs and discards out-of-order packets
> - Sender maintains a window of sent but unacknowledged packets
> - If a packet is lost, sender retransmits all packets starting from the lost one

> [!idea] Selective Repeat (SR) Protocol
> - Sender can transmit multiple packets without waiting for individual ACKs
> - Receiver sends individual ACKs for each correctly received packet, even if out of order
> - Sender only retransmits lost or corrupted packets
> - Requires larger sequence number range (at least twice the window size) to avoid ambiguity

> [!idea] Key Components of Reliable Data Transfer
> - Sequence numbers: Identify and order packets
> - Acknowledgments (ACKs): Confirm successful receipt of packets
> - Negative Acknowledgments (NAKs): Indicate errors or missing packets
> - Checksums: Detect data corruption
> - Window sizes: Determine the number of packets that can be sent without waiting for an ACK
> - Timeouts: Trigger retransmission of lost or delayed packets, calculated based on Round-Trip Time (RTT)

> [!idea] TCP Congestion Control
> - Original TCP:
>   - Slow Start: 
>     - cwnd is initialized to 1 MSS (Maximum Segment Size)
>     - For each ACK received, cwnd is increased by 1 MSS, effectively doubling cwnd every RTT
>     - Slow start continues until cwnd reaches ssthresh or a loss event occurs
>   - Congestion Avoidance:
>     - When cwnd exceeds ssthresh, TCP enters congestion avoidance phase
>     - For each ACK received, cwnd is increased by (MSS × MSS) / cwnd, resulting in a linear increase
>     - If a timeout occurs due to packet loss, ssthresh is set to half of the current cwnd, and cwnd is reset to 1 MSS
> - Tahoe (builds upon Original TCP):
>   - Introduces Fast Retransmit:
>     - If the sender receives three duplicate ACKs, it assumes a packet has been lost
>     - The sender immediately retransmits the missing packet without waiting for a timeout
>     - After fast retransmit, Tahoe performs slow start by setting cwnd to 1 MSS and ssthresh to half of the previous cwnd
> - Reno (builds upon Tahoe):
>   - Introduces Fast Recovery:
>     - After fast retransmit, instead of setting cwnd to 1 MSS, Reno sets cwnd to ssthresh plus 3 MSS
>     - For each additional duplicate ACK received, cwnd is increased by 1 MSS
>     - When an ACK for the retransmitted packet is received, cwnd is set to ssthresh, and TCP enters congestion avoidance phase
>   - Fast recovery allows Reno to maintain a higher cwnd and avoid entering slow start after a single packet loss


> [!idea] TCP Congestion Control
> **Tahoe:**
> - Slow Start: Gradually increases the congestion window (CongWin) until a loss event occurs. CongWin is initialized to 1 MSS and doubled every RTT until it reaches the slow-start threshold (ssthresh).
> - Congestion Avoidance: When CongWin exceeds ssthresh, TCP enters the congestion avoidance phase. CongWin grows more slowly (linearly) to probe for available capacity while avoiding further congestion.
> - On timeout: ssthresh is set to half of the current CongWin, and CongWin is reset to 1 MSS.
> 
> **Reno:**
> - Fast Retransmit: When three duplicate ACKs are received, indicating a packet loss, Reno retransmits the packet immediately without waiting for a timeout.
> - Fast Recovery: After fast retransmit, instead of starting slow start again, Reno halves the CongWin and continues with congestion avoidance, avoiding the lower throughput of starting from scratch.
> 
> ![[Evolution-of-TCPs-congestion-window-Tahoe-and-Reno-10.png]]

> [!idea] Flow Control
> - Prevents the sender from overwhelming the receiver's buffer
> - Receiver advertises its available buffer space (receiver window) in the ACK packets
> - Sender limits its sending rate based on the receiver window size

> [!idea] Connection Establishment and Termination
> - Three-way Handshake (Connection Establishment):
>   1. Client sends a SYN packet to the server
>   2. Server responds with a SYN-ACK packet
>   3. Client sends an ACK packet to acknowledge the SYN-ACK
> - Four-way Handshake (Connection Termination):
>   1. Client sends a FIN packet to the server
>   2. Server responds with an ACK packet
>   3. Server sends a FIN packet to the client
>   4. Client responds with an ACK packet