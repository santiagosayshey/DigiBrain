1. Postal Analogy
   - The OSI model layers can be likened to Russian nesting dolls, where each layer adds its own "envelope" of header information.
   - As data passes from upper to lower layers, it's encapsulated with protocol-specific information at each stage.
   - The process is reversed at the receiving end, with each layer removing its corresponding header information.

2. Delay Types
   - Transmission Delay: Time required to transmit all bits of a packet into the network medium. Formula: t_T = L/R, where L is packet size and R is bandwidth.
   - Propagation Delay: Time taken for a signal to travel from point A to point B over a network medium. Formula: t_p = Distance/Speed.
   - Be able to calculate and understand the difference between transmission and propagation delays.

3. Client-Server vs. Peer-to-Peer (P2P)
   - Client-Server: Centralized model where a server serves multiple clients. Performance depends on server capacity and client-server communication.
   - P2P: Decentralized model where each peer acts as both client and server. Performance depends on peer upload/download rates and file distribution among peers.
   - Socket programming: Enables communication between processes on different machines. (No need to write code, just understand the concept)

4. DNS (Domain Name System)
   - Translates domain names to IP addresses, enabling user-friendly website access.
   - Hierarchical, distributed database with Root, TLD, and Authoritative servers.
   - Iterative Queries: Contacted server replies with the name of the next server to contact.
   - Recursive Queries: DNS servers handle the complete resolution process on behalf of the client.
   - DNS Records: A (IP address), NS (name server), CNAME (canonical name), MX (mail exchange).

5. HTTP (Hypertext Transfer Protocol)
   - Request-response protocol for client-server communication.
   - HTTP/1.0: Non-persistent, each connection used for a single request-response.
   - HTTP/1.1: Persistent, allows connection reuse for multiple requests, reducing overhead.
   - Caching/Proxies: Stores frequently accessed data closer to clients, reducing server load and response times.
   - Pipelining: Allows multiple requests to be sent without waiting for each response, improving efficiency.