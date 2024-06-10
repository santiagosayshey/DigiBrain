# Networks

> [!idea] Networks
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
> - Suitable for applications requiring reliable data transmission and integrity, such as email (SMTP, IMAP, POP3), secure web browsing (HTTPS), file transfers (FTP, SFTP), and secure communications (SSH, VPNs).

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

# Network Layer

> [!idea] Network Layer Functions
> - Routing packets across networks from source to destination
> - Providing a best-effort delivery service (no guarantees on reliability or timeliness)
> - Using IP addresses to identify devices and route packets
> - Maintaining routing tables in the data plane to determine the best outgoing link for each packet
> - Building and updating routing tables in the control plane using routing protocols and algorithms

> [!idea] Routing Tables: Data and Control Planes
> - Routers use routing tables in the data plane to determine the best outgoing link for each incoming packet based on its destination address
> - The control plane builds and maintains these routing tables using routing protocols and algorithms
> - The control plane exchanges information between routers to create an accurate network topology view
> - Efficient cooperation between the data and control planes is essential for minimizing latency, congestion, and other network issues


> [!idea] Routing
> Two fundamental types of routing algorithms used by the control plane to build and maintain routing tables
> 
> **Dijkstra's Algorithm (Link State)**
> - Each node independently runs the algorithm on its local link-state database
> - Maintains a set of visited nodes (S) and unvisited nodes (Q)
> - Iteratively selects the node with the minimum distance from the source and updates distances to its neighbors
> - Time complexity: O(n^2) or O((n + m)logn) with a binary heap
> 
> **Distance Vector**
> - Each node maintains a routing table with costs and via information
> - Nodes share their routing tables with neighbors and update based on received information
> - Count-to-infinity problem: Nodes may infinitely increment distances when a link fails
> - Poison reverse: Nodes advertise failed routes with infinite distance to prevent loops
> 
> 
> | Feature | Link State | Distance Vector |
> |---------|------------|-----------------|
> | Approach | Each node has a complete view of the network topology | Nodes only know about their immediate neighbors |
> | Algorithm | Dijkstra's algorithm | Bellman-Ford algorithm |
> | Convergence | Faster, less susceptible to routing loops | Slower, risk of routing loops and count-to-infinity problem |
> | Message Complexity | Lower, only LSAs sent | Higher, full tables sent |
> | Robustness | Naturally higher, precise | Improved with techniques like split horizon and route poisoning |
Here's an expanded callout that combines Classful Addressing, CIDR, Subnetting, and Inter-AS vs Intra-AS Routing:

> [!idea] Addressing
> **Classful Addressing**:
> IP address divided into network and host bits. More host bits allow more devices on the same network. 
> 
> | Class | Leading Bits | Network Bits | Host Bits | Address Range |
> |-------|--------------|--------------|-----------|---------------|
> | A     | 0            | 8            | 24        | 1.0.0.0 to 127.255.255.255 |
> | B     | 10           | 16           | 16        | 128.0.0.0 to 191.255.255.255 |
> | C     | 110          | 24           | 8         | 192.0.0.0 to 223.255.255.255 |
> | D     | 1110         | - | - | 224.0.0.0 to 239.255.255.255 (Multicast) |
> | E     | 1111         | - | - | 240.0.0.0 to 255.255.255.254 (Reserved) |
> 
> - Inefficient due to fixed network/host division and exhaustion of Class B addresses
> - Example: In the classful system, the IP address 192.168.1.1 is a Class C address, where the first 24 bits (192.168.1) represent the network portion, and the last 8 bits (1) represent the host portion.
>  
> **CIDR (Classless Inter-Domain Routing)**:
> - Replaced classful addressing to allow flexible definition of network and host parts
> - CIDR notation: a.b.c.d/x, where x is the number of network bits (subnet mask)
> - Enables more efficient allocation of IP addresses and summarization of routes
> - Example: In CIDR notation, the IP address 192.168.1.1 with a subnet mask of 255.255.255.0 is represented as 192.168.1.1/24, indicating that the first 24 bits are the network portion, and the remaining 8 bits are for host addresses.
>
> **Subnetting**:
> - Process of dividing a larger network into smaller subnetworks
> - Allows better network management and more efficient use of IP address space
> - Subnet mask determines the division between network and host parts within a subnet
> - Subnetting enables hierarchical routing and reduces the size of routing tables
>
> **Inter-AS vs Intra-AS Routing**:
> - Autonomous System (AS): A group of networks under a single administrative domain
> - Intra-AS Routing:
>   - Routing within an AS, also known as Interior Gateway Protocols (IGPs)
>   - Examples: OSPF, IS-IS, RIP
>   - Focus on optimizing internal data paths and minimizing internal network costs
> - Inter-AS Routing:
>   - Routing between ASes, also known as Exterior Gateway Protocols (EGPs)
>   - Example: Border Gateway Protocol (BGP)
>   - Focus on negotiating data paths based on policies, agreements, and external factors
>   - Enables global Internet connectivity by exchanging routing information between ASes

> [!idea] DHCP (Dynamic Host Configuration Protocol)
> - Automatically assigns IP addresses and network configuration parameters to devices
> - Client-server model: Client broadcasts a request, server responds with an offer
> - Simplifies network configuration but has vulnerabilities (e.g., spoofing, rogue DHCP servers)

> [!idea] IP Fragmentation
> - Process of breaking large IP packets into smaller fragments to fit the MTU of the network
> - Fragments are reassembled at the destination based on the Fragment Offset field in the IP header
> - IPv6 does not allow fragmentation by routers, only by the source host

> [!idea] IPv4 vs IPv6
> | Feature | IPv4 | IPv6 |
> |---------|------|------|
> | Address Size | 32 bits | 128 bits |
> | Address Representation | Dotted decimal notation | Hexadecimal notation |
> | Header Size | 20-60 bytes | 40 bytes (fixed) |
> | Fragmentation | Allowed by routers and hosts | Only by source hosts |
> | Security | Optional (IPsec) | Mandatory (IPsec) |
> | Quality of Service (QoS) | Limited support | Improved support with flow labels |
> | Transition Mechanisms | N/A | Dual-stack, tunneling, translation |
>
> We are transitioning to IPv6 because IPv4 address space is becoming exhausted due to the rapid growth of Internet-connected devices. IPv6 provides a much larger address space (128 bits vs. 32 bits in IPv4), allowing for virtually unlimited unique IP addresses and accommodating the increasing demand for Internet connectivity.

> [!idea] Software Defined Networking (SDN)
> - Separates the network's control plane and data plane
> - Control plane: Centralized controller manages network behavior and policies
> - Data plane: Switches forward packets based on flow tables populated by the controller
> - Enables flexible, programmable network management and dynamic adaptation to network conditions
> - OpenFlow protocol facilitates communication between the controller and switches

