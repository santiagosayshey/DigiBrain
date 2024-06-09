# The Postal Analogy

- Data encapsulation in networks is like putting a letter inside multiple envelopes
- Each OSI layer adds its own "envelope" (header) to the data
- Application layer data = the letter itself
- Headers are added from top to bottom layers
- Headers are removed from bottom to top layers at the receiving end
# Delays

| Delay Type                          | Description                                                                                                                                                                                                                                                                              | Formula                                     |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| <center>Propagation Delay</center>  | The time it takes for a signal to travel from point A to point B over a network medium. It is influenced by the type of medium, the distance between the points, and typically the speed of the signal, which is often close to $c$, the speed of light $(3 \times 10^8$ m/s) in vacuum. | $$t_p=\frac{Distance}{Speed}$$              |
| <center>Transmission Delay</center> | The time required to transmit all the bits of a packet into the network medium. Packet size is denoted by $L$, and the bandwidth (data carrying capacity) is denoted by $R$.                                                                                                             | $$t_T=\frac{L}{R}$$                         |
| <center>Queuing Delay</center>      | The time a packet spends waiting in a queue before it can be transmitted over the network due to congestion or prior packet processing. If there is no space in the queue (i.e. not enough buffer in the router), that packet is dropped!                                                | Depends on queue length and network traffic |
| <center>Processing Delay</center>   | The time taken by a network device (e.g., router, switch) to process a packet.                                                                                                                                                                                                           | Depends on device and packet complexity     |
# Application Layer Protocols

Application layer protocols define the rules for communication between applications running on different devices. They specify the types of messages exchanged, their format (syntax), meaning (semantics), and how and when they should be exchanged.

| Protocol | Key Features                                                                                                                                                                                                                                                                                                                                  |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TCP      | - Connection-oriented protocol<br>- Provides reliable, ordered, and error-checked delivery of data<br>- Establishes a virtual connection between sender and receiver<br>- Uses a three-way handshake for connection establishment<br>- Employs flow control and congestion control mechanisms                                                 |
| UDP      | - Connectionless protocol<br>- Provides unreliable, unordered, and error-prone delivery of data<br>- No virtual connection establishment<br>- Faster than TCP due to less overhead<br>- Suitable for applications that prioritize speed over reliability, such as streaming media or online gaming                                            |
| DNS      | - Translates domain names to IP addresses<br>- Hierarchical, distributed database<br>  - Root name servers<br>  - Top-Level Domain (TLD) servers<br>  - Authoritative DNS servers<br>  - Local name servers                                                                                                                                   |
|          | - Supports iterative and recursive queries<br>  - Iterative: Server responds with the best answer it has or refers the client to another server<br>  - Recursive: Server takes responsibility for resolving the query, querying other servers if needed                                                                                       |
|          | - Resource records:<br>  - A: IPv4 address<br>  - AAAA: IPv6 address<br>  - NS: Name server<br>  - CNAME: Canonical name<br>  - MX: Mail exchange<br>- Uses UDP on port 53 for queries and responses                                                                                                                                          |
| HTTP     | - Protocol for communication between web browsers and servers<br>- HTTP/1.0 (non-persistent):<br>  - Each connection is used for only a single request and response<br>  - Requires two RTTs: one for TCP handshake and another for HTTP request/response<br>  - Higher overhead due to establishing and closing connections for each request |
|          | - HTTP/1.1 (persistent):<br>  - Connections can be reused for multiple requests and responses<br>  - Reduces the number of RTTs and overhead<br>  - Introduces more complex connection management (timeout and closure mechanisms)                                                                                                            |
|          | - Caching and proxies:<br>  - Temporary storage of frequently requested data to reduce server load and improve response time<br>  - Proxies act as intermediaries between clients and servers, forwarding requests and responses                                                                                                              |
|          | - Pipelining (HTTP/1.1):<br>  - Sending multiple requests without waiting for each response, improving performance                                                                                                                                                                                                                            |

# TCC vs UDP

| Feature               | TCP                                                    | UDP                                                    |
|-----------------------|--------------------------------------------------------|--------------------------------------------------------|
| Reliability           | Reliable, ordered, and error-checked delivery          | Unreliable, unordered, and error-prone delivery        |
| Connection Type       | Connection-oriented                                    | Connectionless                                         |
| Speed                 | Slower due to overhead and reliability checks          | Faster due to less overhead                            |
| Flow Control          | Yes, prevents sender from overwhelming receiver         | No flow control                                        |
| Congestion Control    | Yes, adjusts sending rate based on network congestion   | No congestion control                                  |
| Usage                 | Web browsing, email, file transfers                    | Streaming media, online gaming, VoIP                   |

# Multiplexing and Demultiplexing

## TCP

| Multiplexing                                                                                                                | Demultiplexing                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| - Combines data from multiple application processes into a single TCP segment                                               | - Distributes received TCP segments to the appropriate application processes based on the destination IP address and port number                                  |
| - Adds source and destination IP addresses and port numbers to the TCP header for identification                            | - Uses the unique combination of source IP, source port, destination IP, and destination port to determine the specific process to deliver the data                |
| - Allows multiple processes to use the same port simultaneously by maintaining a separate connection for each unique combination | - Ensures that data from each connection is delivered to the correct process                                                                                      |
## UDP

| Multiplexing                                                                                                      | Demultiplexing                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| - Combines data from multiple application processes into a single UDP datagram                                    | - Distributes received UDP datagrams to the appropriate application processes based on the destination IP address and port number                             |
| - Adds destination IP address and port number to the UDP header for identification                                | - Uses the destination IP address and port number to determine the specific process to deliver the data                                                       |
| - Source IP address and port number are optional                                                                  | - Multiple processes can use the same port, but data from different sources may be interleaved as there is no unique connection identifier like in TCP        |
## Reliable Data Transfer (RDT) Protocols

| Protocol         | Key Features                                                                                                           |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Go-Back-N (GBN)  | - Sender maintains a window of size N<br>- Receiver sends cumulative ACKs<br>- Retransmits all packets from the lost one |
| Selective Repeat (SR) | - Sender maintains a window of size N<br>- Receiver sends individual ACKs<br>- Retransmits only the lost or corrupted packet |

## Key Components of Reliable Transport

| Component           | Description                                                                                                                   |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Window Size         | Number of packets that can be sent without waiting for an acknowledgment                                                      |
| Sequence Number     | Identifier for each packet to ensure ordered delivery and detect duplicates                                                   |
| ACKs                | Acknowledgments sent by the receiver to confirm successful receipt of packets                                                 |
| NAKs                | Negative acknowledgments sent by the receiver to indicate lost or corrupted packets                                           |
| Checksums           | Error-detection mechanism to ensure data integrity                                                                            |
| Timeouts            | Timer used by the sender to detect lost packets and initiate retransmission                                                   |
| RTT Calculation     | Round-Trip Time estimation for setting appropriate timeout values                                                             |

## TCP Congestion Control

| Phase               | Description                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------|
| Slow Start          | Exponential increase in congestion window size until a threshold is reached or packet loss occurs          |
| Congestion Avoidance| Additive increase in congestion window size to slowly probe for additional bandwidth                       |
| Fast Retransmit     | Retransmitting a lost packet before the timeout when multiple duplicate ACKs are received                  |
| Fast Recovery       | Adjusting the congestion window size after a fast retransmit to avoid entering slow start again            |

## TCP Connection Establishment and Termination

| Phase                 | Description                                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------|
| Three-Way Handshake   | 1. SYN (client to server)<br>2. SYN-ACK (server to client)<br>3. ACK (client to server)                     |
| Four-Way Handshake    | 1. FIN (client to server)<br>2. ACK (server to client)<br>3. FIN (server to client)<br>4. ACK (client to server) |