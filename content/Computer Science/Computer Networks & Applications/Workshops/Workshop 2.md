
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
> Contents



> [!exercise]+ Question 4 - FSM and RDT
> Draw the FSM for the receiver side of protocol `rdt3.0`
> 
> **Answer:**
> There are no changes from the receiver's side from `rtd2.2` to `rtd3.0`. Any packets retransmitted due to a timeout are still treated as the same data.
> 
> ![[asdasdasdasdasd.png]]

TCP Reno congestion control:

1. TCP Reno uses an Additive Increase/Multiplicative Decrease (AIMD) algorithm to control congestion.
2. It starts with a small congestion window (cwnd) and increases it additively every RTT as long as no packet loss occurs. This is the Additive Increase part.
3. If packet loss is detected via timeout, it assumes congestion has occurred and drastically reduces the cwnd (typically by half). This is the Multiplicative Decrease part.
4. After timeout, it enters a "slow start" phase until reaching a threshold, then switches to additive increase.

Now, here's how an application designer might exploit this to get higher data rates at the expense of other TCP flows:

1. Use many parallel TCP connections. Since each connection has its own cwnd and additive increase phase, the aggregate bandwidth across connections will be higher. This is unfair to applications using fewer connections.
2. Use a larger initial congestion window. Some applications may use larger initial cwnd values than the standard allows. This lets them ramp up faster after loss.
3. Avoid backing off on loss. An aggressive application might avoid halving the cwnd on loss timeout and instead just do a small multiplicative decrease, or simply keep the same cwnd. This maintains a high send rate under congestion.
4. Modify the additive increase factor. Using a larger additive increase factor ramps up the send rate faster after loss, outcompeting other flows with standard increase.