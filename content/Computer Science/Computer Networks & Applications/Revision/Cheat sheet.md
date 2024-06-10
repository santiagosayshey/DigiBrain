# Envelopes

   - The OSI model layers can be likened to Russian nesting dolls, where each layer adds its own "envelope" of header information.
   - As data passes from upper to lower layers, it's encapsulated with protocol-specific information at each stage.
   - The process is reversed at the receiving end, with each layer removing its corresponding header information.

# Delays

| Delay Type         | Description                                                                                                            | Formula                                            |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Propagation Delay  | The time it takes for a signal to travel from point A to point B over a network medium.                                | $$t_p = Distance / Speed$$                         |
| Transmission Delay | The time required to transmit all the bits of a packet into the network medium.                                        | $$t_T = L / R$$L is packet size and R is bandwidth |
| Queuing Delay      | The time a packet spends waiting in a queue before it can be transmitted due to congestion or prior packet processing. | Depends on queue length and network traffic        |
| Processing Delay   | The time taken by a network device (e.g., router, switch) to process a packet.                                         | Depends on device and packet complexity            |
# Client/Server, P2P


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

| HTTP Version | Characteristics |
|--------------|-----------------|
| HTTP/1.0 | Non-persistent, each connection used for a single request-response. |
| HTTP/1.1 | Persistent, allows connection reuse for multiple requests, reducing overhead. |

   - Caching/Proxies: Stores frequently accessed data closer to clients, reducing server load and response times.
   - Pipelining: Allows multiple requests to be sent without waiting for each response, improving efficiency.