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
> | Propagation Delay  | The time it takes for a signal to travel from point A to point B over a network medium.                                | $$D_p = Distance / Speed$$                              |
> | Transmission Delay | The time required to transmit all the bits of a packet into the network medium.                                        | $$D_T = L / R$$ where L is packet size and R is bandwidth |
> | Queuing Delay      | The time a packet spends waiting in a queue before it can be transmitted due to congestion or prior packet processing. | Depends on queue length and network traffic             |
> | Processing Delay   | The time taken by a network device (e.g., router, switch) to process a packet.                                         | Depends on device and packet complexity                 |
> | Collision Occurrence | If the propagation delay between two nodes is less than the transmission delay $D_p < D_T$, a collision will occur when both nodes start transmitting their packets simultaneously. This happens because the signal carrying the packet from one node reaches the other node before it finishes transmitting its own packet, causing the packets to overlap in time and collide on the shared medium. The corrupted packets need to be retransmitted, reducing network efficiency and increasing latency. | Collision if $$D_p < D_T$$ |



> [!idea] Peer-to-Peer (P2P) Networks
> - Decentralized model where each peer acts as both client and server
> - Peers share resources (files, content, bandwidth) directly without central coordination
> - Torrents (shared resources) are split into chunks; peers send and receive chunks they have/need
> - Rarest chunks are prioritized; peers connect with their 4 most connectable neighbors
> - Trackers monitor torrent swarms and facilitate peer connections
> - P2P performance depends on peer upload/download rates and file distribution among peers


> [!idea] Client-Server vs. Peer-to-Peer (P2P)
> **Client-Server**: Centralized model where a server serves multiple clients. Performance depends on server capacity and client-server communication.
> $$
> \begin{align*}
> &D_{cs} \geq \max \left( \frac{NF}{u_s}, \frac{F}{d_{min}} \right) \\[10pt]
> &\text{where:} \\[10pt]
> &D_{cs} \text{: Distribution time for all peers to download the file.} \\[10pt]
> &N \text{: Number of peers that want to obtain a copy of the file.} \\[10pt]
> &F \text{: Size of the file to be distributed (in bits).} \\[10pt]
> &u_s \text{: Upload rate of the server's access link.} \\[10pt]
> &d_{min} \text{: Download rate of the peer with the lowest download rate.}
> \end{align*}
> $$
>**P2P**: Decentralized model where each peer acts as both client and server. Performance depends on peer upload/download rates and file distribution among peers.
> $$
> \begin{align*}
> &D_{p2p} \geq \max \left( \frac{F}{u_s}, \frac{F}{d_{min}}, \frac{NF}{u_s + \sum_{i=1}^{N} u_i} \right) \\[10pt]
> &\text{where:} \\[10pt]
> &D_{p2p} \text{: Distribution time for all peers to download the file.} \\[10pt]
> &F \text{: Size of the file to be distributed (in bits).} \\[10pt]
> &N \text{: Number of peers that want to obtain a copy of the file.} \\[10pt]
> &u_s \text{: Upload rate of the server.} \\[10pt]
> &d_{min} \text{: Download rate of the peer with the lowest download rate.} \\[10pt]
> &u_i \text{: Upload rate of the i-th peer.} \\[10pt]
> &\sum_{i=1}^{N} u_i \text{: Sum of the upload rates of all N peers.}
> \end{align*}
> $$

> [!idea] DNS (Domain Name System)
> - Translates domain names to IP addresses, enabling user-friendly website access.
> - Hierarchical, distributed database with Root, TLD, and Authoritative servers.
> - Iterative Queries: Contacted server replies with the name of the next server to contact.
> - Recursive Queries: DNS servers handle the complete resolution process on behalf of the client.
> - DNS Records: A (IP address), NS (name server), CNAME (canonical name), MX (mail exchange).
>
> | Query Type   | Advantages                                            |
> |--------------|-------------------------------------------------------|
> | Iterative    | - Reduces load on each DNS server.                    |
> |              | - Client controls the query process and pace.         |
> |              | - Can provide resilience against certain DNS failures by allowing the client to query alternative servers if one fails. |
> | Recursive    | - Simpler for the client, as the DNS server manages all aspects of the resolution. |
> |              | - Can be faster from the user's perspective because all DNS resolution is handled by the server. |
> |              | - Reduces the number of DNS queries that need to be handled directly by the client. |

This table highlights the benefits of each type of DNS query, providing a clear distinction between their operational advantages.

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

> [!idea] Multiplexing and Demultiplexing
> - Multiplexing is the process of combining multiple data streams from different applications into a single stream of packets, which can be transmitted over a shared network channel.
> - Demultiplexing is the process of separating the single stream of packets received from the network channel into multiple data streams and delivering them to the appropriate applications.
>
>![[Plexing.png]]

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
> - If a packet is lost, sender retransmits all packets in the current window starting from the lost one

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


> [!idea]+ TCP Timeouts
>
> When you send data over the internet, there's always a chance that some of it might get lost or delayed. TCP, the protocol responsible for reliable data transfer, uses timeouts to figure out when to resend this data.
>
> To set the right timeout value, TCP keeps track of how long it usually takes for data to be sent and acknowledged, which is called the Round-Trip Time (RTT). It also considers how much the RTT varies over time.
>
> Here's how TCP calculates the timeout:
>
> 1. **Estimate the typical RTT**: TCP updates its estimate of the typical RTT (called EstimatedRTT) every time it measures a new RTT. It gives more importance to recent measurements, so the estimate stays up-to-date with the current network conditions.
>    $$ \text{EstimatedRTT} = (1 - \alpha) \times \text{Previous EstimatedRTT} + \alpha \times \text{SampleRTT} $$
>    where $\alpha$ is a small number (typically 0.125) that determines how much weight is given to the most recent RTT measurement (SampleRTT).
>
> 2. **Measure the variability of the RTT**: TCP also keeps track of how much the RTT changes from one measurement to another. This is called the Deviation. A high Deviation means that the RTT is changing a lot, while a low Deviation means the RTT is more stable.
>    $$ \text{Deviation} = (1 - \alpha) \times \text{Previous Deviation} + \alpha \times |\text{SampleRTT} - \text{EstimatedRTT}| $$
>
> 3. **Set the Timeout value**: To determine the Timeout, TCP takes the EstimatedRTT and adds four times the Deviation to it. This extra time accounts for the variability in the RTT.
>    $$ \text{Timeout} = \text{EstimatedRTT} + 4 \times \text{Deviation} $$
>
> By including the Deviation in the Timeout calculation, TCP can adapt to changing network conditions. When the RTT is more variable (high Deviation), the Timeout will be longer, giving more time for acknowledgments to arrive before resending data. When the RTT is more stable (low Deviation), the Timeout will be shorter, allowing faster detection of lost data.
>
> If the Deviation wasn't included in the Timeout calculation, and the Timeout was set to just the EstimatedRTT, TCP might struggle to adapt to changes in network conditions. In situations where the RTT becomes more variable, the Timeout would be too short, causing TCP to resend data unnecessarily. This would lead to increased network traffic and reduced efficiency. On the other hand, if the RTT becomes more stable, the Timeout would be too long, causing TCP to wait longer than necessary before resending lost data, which could slow down the data transfer.
>
> This clever approach helps TCP strike a balance between resending data too soon (which could lead to unnecessary network traffic) and waiting too long to resend lost data (which could slow down the data transfer).

> [!idea] TCP Congestion Control
> **Tahoe:**
> - Slow Start: Increase CongWin exponentially until a loss event or ssthresh is reached.
> - Congestion Avoidance: Increase CongWin linearly after ssthresh is reached.
> - On timeout: Set ssthresh to half of the current CongWin and reset CongWin to 1 MSS.
> 
> **Reno:**
> - Fast Retransmit: Retransmit the lost packet immediately upon receiving three duplicate ACKs.
> - Fast Recovery: After fast retransmit, halve CongWin and continue with congestion avoidance.
> 
> **Calculation of ssthresh:**
> - Initial value: Set to a large value at the beginning of a connection.
> - On timeout or fast retransmit: Set to half of the current CongWin.
> 
> **Why Fast Retransmit and Fast Recovery are better:**
> - Faster recovery from packet loss: Fast retransmit allows quick retransmission of lost packets without waiting for a timeout, reducing the time spent in recovery.
> - Maintaining higher throughput: Fast recovery avoids the slow start phase after packet loss, allowing the sender to maintain a higher sending rate and better utilize the available bandwidth.
> - Improved performance: The combination of fast retransmit and fast recovery in Reno results in faster convergence to the optimal congestion window size and higher overall throughput compared to Tahoe.
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
> - Note: During data transfer, if the receiver has no data to send back to the sender, it will still send standalone ACK packets to acknowledge the received data. These ACKs are sent as separate control segments, even if they cannot be piggybacked on data segments.

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
> - Time complexity: $O(n^2)$ or $O((n + m)logn)$ with a binary heap
>
> **Procedure:**
> 1. Initialize distances to all nodes as infinity, starting node as 0
> 2. Add starting node to visited set S 
> 3. For each unvisited neighbor v:
>    - Calculate distance from current node to v
>    - Update v's distance if new distance is smaller
> 4. Select unvisited node u with smallest distance, add to S
> 5. Repeat step 3 for all unvisited neighbors of u
> 6. Repeat step 4 until all nodes visited
>
> **Distance Vector**  
> - Each node maintains a routing table with costs and via information
> - Nodes share their routing tables with neighbors and update based on received information
> - Count-to-infinity problem: Nodes may infinitely increment distances when a link fails
> - Poison reverse: Nodes advertise failed routes with infinite distance to prevent loops
>
> **Procedure:**
> 1. Each node initialises own routing table with costs to neighbors
> 2. Send routing table to all neighbors
> 3. Receive routing tables from neighbors
> 4. For each neighbor's routing table:
>    - Update own table if route is better
> 5. Repeat steps 2-4 periodically
>
> | Feature | Link State | Distance Vector |
> |---------|------------|-----------------|
> | Performance / Advantages / Disadvantages | Faster convergence, less overhead, precise routing / Higher memory and CPU requirements, more complex | Slower convergence, routing loops, count-to-infinity problem / Simple, distributed, no need for global topology |
> | When to Use | Link State is better for networks with high performance and reliability requirements, where complete topology knowledge and faster convergence are crucial. It is recommended for large, complex networks with high bandwidth and low CPU/memory constraints. | Distance Vector is better for smaller, less complex networks where simplicity and distributed operation are priorities, and performance requirements are not as stringent. It is recommended for networks with lower bandwidth and higher CPU/memory constraints. |

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
> - DHCP is a network protocol used to automatically assign IP addresses and other network configuration parameters to devices on a network.
> - DHCP works in a client-server model:
>   - DHCP servers manage a pool of IP addresses and configuration parameters.
>   - DHCP clients (devices) request an IP address and other settings from the DHCP server.
>
> - DHCP Procedure:
>   1. **DHCP Discover**: Client broadcasts a DHCP Discover message to locate available DHCP servers.
>   2. **DHCP Offer**: DHCP server responds with a DHCP Offer message, offering an IP address and other configuration parameters.
>   3. **DHCP Request**: Client sends a DHCP Request message to the selected server, requesting the offered IP address and parameters.
>   4. **DHCP Acknowledgment**: The server acknowledges the request with a DHCP Acknowledgment message, confirming the lease of the IP address and parameters.
>   5. **DHCP Renewal**: The client periodically renews the lease by sending a DHCP Request message to the server before the lease expires.
>   6. **DHCP Release**: When the client no longer needs the IP address, it sends a DHCP Release message to the server to release the lease.


> [!idea] IP Fragmentation
> - Process of breaking large IP packets into smaller fragments to fit the MTU (Maximum Transmission Unit) of the network
> - Fragments are reassembled at the destination based on the Fragment Offset field in the IP header
> - IPv6 does not allow fragmentation by routers, only by the source host
> - IP Header Fields used for Fragmentation:
>
> | Field | Description |
> |-------|-------------|
> | Identification | Unique value to identify the original IP packet |
> | Flags | 3 bits: Reserved (1 bit), Don't Fragment (1 bit), More Fragments (1 bit) |
> | Fragment Offset | Offset of this fragment from the start of the original IP packet (in 8-byte units) |
> | Total Length | Total length of the original IP packet (before fragmentation) |
>
> - Fragmentation Process:
>   1. If the packet size exceeds the MTU of the outgoing interface, it is fragmented
>   2. Each fragment has the same Identification, Source, and Destination addresses as the original packet
>   3. The More Fragments flag is set to 1 for all fragments except the last one
>   4. The Fragment Offset field indicates the position of the fragment in the original packet
>   5. The Total Length field indicates the length of the original packet
> - Reassembly Process:
>   1. The destination host receives the fragments
>   2. It uses the Identification, Source, and Destination addresses to identify the original packet
>   3. The Fragment Offset field is used to reassemble the fragments in the correct order
>   4. When all fragments are received (More Fragments = 0), the original packet is reassembled
>
> Note: IP fragmentation can cause performance issues and security vulnerabilities (e.g., overlapping fragments), so it is often avoided by using Path MTU Discovery or setting the Don't Fragment bit.


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

# Data Link Layer

> [!idea] Data Link Layer Functions
> - Encapsulates data into frames (header, payload, trailer)
> - Provides link access and reliable transport between adjacent nodes
> - Error detection and correction (checksum, CRC, parity)
>   - Checksum: Sender calculates sum of data bits, receiver verifies integrity
>   - Cyclic Redundancy Check (CRC): Polynomial division to generate checksum
>   - Parity: Extra bits to ensure even/odd number of 1s
>     - 1D Parity: Single parity bit for error detection
>     - 2D Parity: Arranges data in grid, adds parity bits for each row and column

> [!idea] Spanning Tree Protocol (STP) and Minimum Spanning Trees (MSTs)
> - STP prevents loops in switched networks by creating a logical tree topology
> - Redundant paths are identified and blocked to ensure a single active path
> - MST algorithms (Prim's, Kruskal's) find the spanning tree with minimum total cost
> - STP acts like traffic lights, blocking potential loops and enabling efficient data flow

> [!idea] Multiple Access Approaches
>
> **Channel Partitioning**:
> - Bandwidth divided into smaller, dedicated channels
> - Each node assigned a specific channel to avoid collisions
> - Examples:
>   - TDMA (Time Division Multiple Access): time divided into slots, each node assigned a specific time slot
>   - FDMA (Frequency Division Multiple Access): frequency spectrum divided into non-overlapping channels, each node assigned a specific frequency band
>   - CDMA (Code Division Multiple Access): nodes share the same frequency channel but are assigned unique codes for simultaneous communication without interference
> - Best suited for high load scenarios where fairness and collision avoidance are crucial
>
> **Random Access**:
> - Nodes access the shared channel randomly when they have data to send
> - Collisions possible, requiring detection and recovery mechanisms
> - Examples:
>   - ALOHA: nodes transmit whenever they have data, colliding frames are discarded and retransmitted after random delay
>     - Pure ALOHA: nodes transmit immediately
>     - Slotted ALOHA: time divided into slots, nodes transmit only at the beginning of a slot, reducing collision probability
>   - CSMA (Carrier Sense Multiple Access): nodes listen to the channel before transmitting, attempting to avoid collisions
>     - CSMA/CD (Collision Detection): wired networks, nodes stop transmission upon detecting collision (jam signal to tell everyone to stop) and retransmit after random delay
>     - CSMA/CA (Collision Avoidance): wireless networks, nodes use RTS/CTS handshake to reserve channel before transmitting
> - Suitable for low to moderate loads with unpredictable traffic patterns
>
> **Taking Turns**:
> - Nodes access the shared channel in a predetermined order
> - Collisions avoided by granting exclusive access to one node at a time
> - Examples:
>   - Token Passing: nodes organized in a logical ring, a token is passed from node to node, granting permission to transmit
>   - Polling: central controller polls each node for data, granting transmission opportunities based on node responses
> - Suitable for moderate, predictable load scenarios with a fixed number of nodes


> [!idea] LAN Topologies and Ethernet
> **Bus Topology**: 
> - Devices connected to a single shared medium
> - Data transmitted by one device is received by all others on the bus
> - Prone to collisions and reduced performance at high speeds
>  
> **Star Topology and Ethernet**:
> - Devices connected to a central switch or hub
> - Ethernet: standardized protocol for wired LAN communication in a star topology
> - Frame structure: Preamble (clock sync), SFD (start of frame), MAC addresses, EtherType, payload, CRC
> - Advantages: reduced collision domain, improved reliability, easier troubleshooting, increased bandwidth


> [!idea] Switches in Ethernet Networks
> **Key Functions**:
> - Filtering: examining destination MAC address to determine output port(s)
> - Storing: temporarily holding frames in buffer memory
> - Forwarding: sending frames to appropriate output port based on MAC address
>   - If destination MAC is known, forward to corresponding port
>   - If unknown, flood to all ports except incoming port
>   
> **Switch Self-Learning and MAC Address Table**:
> - Switches build and maintain MAC address table through self-learning
> - Associate source MAC address with incoming port
> - Allows efficient forwarding of frames to intended recipients
> 
> **Benefits**:
> - Dedicated bandwidth for each device, reducing collisions
> - Improved performance and efficiency through intelligent filtering and forwarding
> - Plug-and-play connectivity for easy device addition/removal
> - Enhanced security by limiting data frame propagation to necessary ports

> [!idea] Address Resolution Protocol (ARP)
> - Maps IP addresses to MAC addresses within a LAN
> - Sender broadcasts ARP request, receiver responds with MAC address
> - ARP table (cache) stores IP-to-MAC mappings for a short period


> [!idea] MPLS (Multiprotocol Label Switching)
> - Directs data based on short path labels rather than long network addresses
> - Label Switch Routers (LSRs) perform label switching, Label Edge Routers (LERs) assign and remove labels
> - Enables flexible routing, traffic engineering, and fast reroute for resilience

> [!idea] ICMP (Internet Control Message Protocol)
> - Used by hosts and routers to communicate network-layer information
> - Primary use: error reporting (e.g., "Destination network unreachable")
> - ICMP messages are carried as IP payload, like TCP or UDP segments
> 
> ICMP Message Format:
> 
> | Field | Description |
> |-------|-------------|
> | Type  | Specifies the type of ICMP message |
> | Code  | Provides additional information about the message type |
> | Header and first 8 bytes of IP datagram | Helps the sender determine the datagram that caused the error |
> 
> ICMP Message Types and Uses:
> - Destination Unreachable (Type 3): Indicates failure to deliver IP datagram
> - Time Exceeded (Type 11): Generated when TTL field reaches 0 or fragment reassembly time exceeded
> - Echo Request (Type 8) and Echo Reply (Type 0): Used by Ping utility
> - Redirect (Type 5): Informs a host of a better route to a destination
> 
> Ping:
> - Network utility used to test reachability of a host on an IP network
> - Uses ICMP Echo Request (Type 8, Code 0) and Echo Reply (Type 0, Code 0) messages
> - Source sends Echo Request, target responds with Echo Reply
> - Measures round-trip time (RTT) between sending request and receiving reply
> - If target is unreachable or doesn't respond within timeout, no Echo Reply is received

> [!idea] Traceroute
> - Network diagnostic tool used to discover the path between a source and destination host
> - Works by purposely forcing each router along the path to send an ICMP Time Exceeded message
> 
> Traceroute Process:
> 1. Source sends UDP packets to the destination, starting with a TTL of 1 and incrementing by 1 for each subsequent packet
> 2. Each router decrements TTL by 1 before forwarding; when TTL reaches 0, router discards packet and sends ICMP Time Exceeded (Type 11, Code 0) back to source
> 3. Source records IP address and RTT for each router that sends Time Exceeded message
> 4. When packet reaches destination, it responds with ICMP Port Unreachable (Type 3, Code 3) due to unlikely UDP port number
> 5. Source stops sending packets after receiving Port Unreachable message
> 
> By intentionally causing routers to send ICMP Time Exceeded messages, Traceroute maps the path and measures the RTT between the source and each router along the way.

> [!idea] Wireshark
> - Network protocol analyzer for capturing and analyzing network traffic
> - Displays detailed information about captured packets (e.g., source/destination, protocol, length)
> - Filters can be applied to focus on specific protocols, IP addresses, or port numbers
> - Useful for network troubleshooting, security analysis, and learning about network protocols

# Security

> [!idea] Confidentiality, Data Integrity, and Authentication
> - Confidentiality: Ensuring that data is not disclosed to unauthorized parties
>   - Achieved through encryption algorithms (e.g., 3DES, AES)
> - Data Integrity: Verifying that data has not been altered or tampered with
>   - Achieved through hash functions (e.g., SHA, MD5) and digital signatures
> - Authentication: Confirming the identity of a user or system
>   - Achieved through passwords, public key cryptography (e.g., RSA), and digital certificates

> [!idea] Attacks and Nonces
> - Attacks: Attempts to compromise the security of a system or network
>   - Examples: eavesdropping, impersonation, replay attacks, man-in-the-middle attacks
> - Nonces: Random numbers used only once to prevent replay attacks and ensure message freshness
>   - Included in authentication protocols to prove the "liveness" of a message

> [!idea] Hash Functions and Fingerprints
> - Hash Functions: Mathematical algorithms that map data of arbitrary size to a fixed-size output (hash value or digest)
>   - Properties: deterministic, quick to compute, pre-image resistant, small changes result in significantly different hash values
>   - Examples: SHA (Secure Hash Algorithm) family, MD5 (Message Digest 5)
> - Fingerprints: Hash values used to uniquely identify and verify the integrity of data
>   - Applications: password storage, file integrity verification

> [!idea] Encryption Algorithms
> | Algorithm | Type | Key Size | Block Size |
> |-----------|------|----------|------------|
> | 3DES      | Symmetric | 168 bits | 64 bits |
> | AES       | Symmetric | 128, 192, or 256 bits | 128 bits |
> | RSA       | Asymmetric | Varies (e.g., 2048, 4096 bits) | N/A |

> [!idea] Public Key Encryption (RSA) and Certificate Authorities
> - Public Key Encryption: Asymmetric cryptography that uses a public-private key pair
>   - Public key used for encryption, private key used for decryption
>   - Enables secure communication without the need for a pre-shared secret key
> - Certificate Authorities (CAs): Trusted third-party entities that issue digital certificates
>   - Certificates bind public keys to the identities of their owners
>   - CAs verify the identity of the certificate requestor and digitally sign the certificate

> [!idea] Secure Email
> - Secure email communication involves:
>   1. Encrypting the email content to ensure confidentiality
>   2. Digitally signing the email to provide authentication and integrity
>   3. Using public key cryptography for secure key exchange and signature verification
>
> 1. **Key Generation**: Sender and receiver generate their respective public-private key pairs and obtain digital certificates from a trusted certificate authority (CA).
> 2. **Certificate Exchange**: Sender and receiver securely exchange their digital certificates and verify the authenticity of each other's public keys through the CA.
> 3. **Message Encryption**: Sender encrypts the message using a symmetric key and encrypts the symmetric key using the receiver's public key.
> 4. **Digital Signature**: Sender creates a digital signature by signing the encrypted message with their private key.
> 5. **Message Transmission**: Sender transmits the encrypted message, encrypted symmetric key, and digital signature to the receiver.
> 6. **Symmetric Key Decryption**: Receiver decrypts the encrypted symmetric key using their private key to obtain the symmetric key.
> 7. **Message Decryption**: Receiver decrypts the encrypted message using the obtained symmetric key to retrieve the original message.
> 8. **Signature Verification**: Receiver verifies the sender's digital signature using the sender's public key to ensure the message's authenticity and integrity.
>
> This process ensures confidentiality through symmetric encryption, secure key exchange through public-key cryptography, and authentication and integrity through digital signatures.



![[Images/2016 Exam.pdf]]
