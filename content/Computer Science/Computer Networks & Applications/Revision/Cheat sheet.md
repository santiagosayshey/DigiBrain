> [!idea] Postal Analogy
> - The OSI model layers can be likened to Russian nesting dolls, where each layer adds its own "envelope" of header information.
> - As data passes from upper to lower layers, it's encapsulated with protocol-specific information at each stage.
> - The process is reversed at the receiving end, with each layer removing its corresponding header information.

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

> [!idea] Transport Layer Services
> - Provides logical communication between processes on different hosts
> - Key services: multiplexing, demultiplexing, and reliable data transfer
> - Uses port numbers to identify sending and receiving processes
> - Sockets provide the API between the application and transport layers

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

Here are the updated condensed notes for the Transport Layer, including the missing topics:

> [!idea] Key Components of Reliable Data Transfer
> - Sequence numbers: Identify and order packets
> - Acknowledgments (ACKs): Confirm successful receipt of packets
> - Negative Acknowledgments (NAKs): Indicate errors or missing packets
> - Checksums: Detect data corruption
> - Window sizes: Determine the number of packets that can be sent without waiting for an ACK
> - Timeouts: Trigger retransmission of lost or delayed packets, calculated based on Round-Trip Time (RTT)

I apologize for my oversight. Here is the updated section on TCP Congestion Control, including the original TCP, Tahoe, and Reno:

> [!idea] TCP Congestion Control
> - Original TCP:
>   - Slow Start: 
>     - Gradually increases the congestion window (cwnd) size until a loss event occurs
>     - cwnd is initialized to a small value and doubled every RTT until a threshold (ssthresh) is reached
>   - Congestion Avoidance:
>     - Increases cwnd more slowly (linearly) after ssthresh is reached
>     - If a loss event occurs, ssthresh is set to half of the current cwnd, and cwnd is reset to its initial value
> - Tahoe (builds upon Original TCP):
>   - Introduces Fast Retransmit:
>     - Triggers retransmission of a lost packet after receiving a specified number of duplicate ACKs (usually 3)
>     - Avoids waiting for a timeout to retransmit lost packets
> - Reno (builds upon Tahoe):
>   - Introduces Fast Recovery:
>     - After fast retransmit, cwnd is set to ssthresh plus the number of duplicate ACKs received
>     - Allows for faster recovery of lost packets without entering slow start

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