
> [!exercise]+ Question 1 (Multiplexing/Demultiplexing)
> 1. The UDP header does not contain any information that is not present in the TCP header (verify this for yourself). That being the case, why do you, as a programmer, have to specify the header information (ports and IP addresses) whenever you send a UDP packet; but you don't when you send a TCP packet?
> 2. How is a UPD socket fully identified? How is a TCP socket fully identified?
> 3. Assume a web application in Host A has a UDP socket bound to port number 8080. Now Host B and C each sends UDP segment to Host A with destination port number 8080. Will both segments be directed to the same socket at Host A? If so, how will the process at Host A know that these that these two segments originated from two different hosts?
>    
> **Answers:**
> 1. This is because of the difference in connection philosophy between UDP and TCP. UDP is said to be **"connectionless"**, so the application must provide the header information for every packet sent. TCP, on the other hand, is **connection-oriented**. This means that once a connection is established between the client and server, the TCP layer maintains the connection state and automatically includes the necessary header information for each packet sent within that connection.
> 2. **UDP** sockets are identified by the **destination IP address and port** number. **TCP** sockets requires BOTH **source AND destination IP address and port** number.
> 3. **UDP segments still include source port and IP**, they're just not needed to identify the socket to be demultiplexed to. The source port and IP allows the destination to know where the data came from. 


> [!exercise]+ Question 2 - TCP and Protocol Design
>Protocol design decisions often have unexpected performance consequences. HTTP 1.0 is an example of a protocol design where lower layer protocol behaviour impacted directly on the performance of the higher layer protocol.
>
>1. What is the difference between HTTP 1.1 and HTTP 1.0 in terms of transport layer connections?
>2. What two transport layer issues do the changes to HTTP address?
>3. How does the change improve HTTP performance?
>
>**Answers:**
>1. In HTTP 1.0, a **new TCP connection is established for each request/response pair**, leading to high overhead. HTTP 1.1 allows **persistent connections**, enabling multiple requests/responses over a single connection.
>2. The changes address **congestion control** by reducing the number of times congestion control mechanisms are triggered due to fewer connections. They also tackle **low link utilization** by enabling pipelining, allowing multiple requests to be sent consecutively without waiting for each response, thereby making efficient use of the available bandwidth.
>3. These changes **improve HTTP performance** by significantly **reducing latency** (less time spent on TCP handshakes), **enhancing bandwidth utilization** (through pipelining), and **decreasing server load** (fewer connections to manage), leading to faster web page loading times and more efficient network use.


> [!exercise]+ Question 3 - Congestion Management / Control
> Consider congestion control in TCP Reno (most common algorithm).
>- How might application designers exploit the Internet's use of TCP to get higher data rates at the expense of other data flows that are using TCP?
>
>**Answer:**
> TCP Reno congestion control works by:
>
> - Adjusting the amount of data a sender can transmit before receiving confirmation, known as the **congestion window**.
>
> - When the network is not congested, TCP Reno gradually increases the congestion window, allowing more data to be sent. If the sender detects **data loss**, indicating congestion, it **dramatically reduces** the window to alleviate the load on the network.
>
> - After reducing the window, TCP Reno cautiously increases it again, transitioning to a more aggressive increase if congestion is not encountered. This cycle of increasing the send rate when possible and rapidly decreasing it when necessary allows TCP Reno to **adapt to changing network conditions** and **share network capacity fairly** among competing traffic.
>
> Application designers can exploit TCP Reno's congestion control mechanism to **gain an unfair advantage** over other applications. They may do this by:
>
> 1. Using **multiple TCP connections in parallel**, allowing their application to achieve higher total bandwidth than others using fewer connections.
>
> 2. Starting with a **larger congestion window**, enabling faster ramp-up after packet loss compared to applications adhering to standard initial window sizes.
>
> 3. **Not reducing the congestion window** as much as they should when packet loss is detected, maintaining a higher send rate during congestion.
>
> 4. **Increasing the congestion window more aggressively** than standard TCP Reno, allowing faster recovery of send rates after packet loss.
>


> [!exercise]+ Question 4 - FSM and RDT
> Draw the FSM for the receiver side of protocol `rdt3.0`
> 
> **Answer:**
> There are no changes from the receiver's side from `rtd2.2` to `rtd3.0`. Any packets retransmitted due to a timeout are still treated as the same data.
> 
> ![[asdasdasdasdasd.png]]


> [!exercise]+ Question 5 - Selective Repeat
>
> Consider the problem of implementing timers. Selective Repeat does not resend all packets on timeout, so it must timeout packets individually. However, in an implementation we are likely to only have access to one hardware timer.
>
> How might you solve this problem?
>
> To solve the problem of implementing timers for Selective Repeat using a single hardware timer, you can consider the following approaches:
>
> 1. Using a single timer for the oldest unacknowledged packet:
>    - **Start the timer when the oldest unacknowledged packet is sent.**
>    - **If an ACK is received for the oldest packet, stop the timer and start it again for the next oldest unacknowledged packet.**
>    - **If the timer expires, retransmit the oldest unacknowledged packet and start the timer again.**
>    - Overhead: This approach requires maintaining a data structure to keep track of the oldest unacknowledged packet and its associated timer.
>
> 2. Using a single timer and a timeout queue:
>    - When a packet is sent, calculate its timeout timestamp and add it to a timeout queue.
>    - Set the timer to expire at the earliest timeout timestamp in the queue.
>    - When an ACK is received, remove the corresponding packet from the timeout queue and update the timer if necessary.
>    - If the timer expires, retransmit the packet associated with the expired timestamp and update the timer based on the next earliest timestamp in the queue.
>    - Overhead: This approach requires maintaining a timeout queue and updating it whenever packets are sent or acknowledged.
>
> **A simpler solution is to use the first approach, where only the oldest unacknowledged packet in the sender's window needs a timer.** This is because:
> - **If the oldest packet is acknowledged, the window slides forward, and the timer can be started for the next oldest unacknowledged packet.**
> - **If the oldest packet times out, it is retransmitted, and the timer is restarted for the same packet.**
>
> Restarting the timer every time a packet is sent would be inefficient because:
> - It would require resetting the timer for every packet sent, even if an earlier packet is still unacknowledged.
> - If an ACK is received for an earlier packet, the timer would need to be adjusted, adding complexity to the implementation.
>
> **Restarting the timer when the oldest packet is ACKed is a better approach because:**
> - **It ensures that the timer is always associated with the oldest unacknowledged packet.**
> - **It simplifies the timer management process, as the timer only needs to be restarted when the window slides forward.**
>
