
> [!exercise]+ Question 1 (Multiplexing/Demultiplexing)
> 1. The UDP header does not contain any information that is not present in the TCP header (verify this for yourself). That being the case, why do you, as a programmer, have to specify the header information (ports and IP addresses) whenever you send a UDP packet; but you don't when you send a TCP packet?
> 2. How is a UPD socket fully identified? How is a TCP socket fully identified?
> 3. Assume a web application in Host A has a UDP socket bound to port number 8080. Now Host B and C each sends UDP segment to Host A with destination port number 8080. Will both segments be directed to the same socket at Host A? If so, how will the process at Host A know that these that these two segments originated from two different hosts?
>    
> **Answers:**
> 1. This is because of the difference in connection philosophy between UDP and TCP. UDP is said to be **"connectionless"**, so the application must provide the header information for every packet sent. TCP, on the other hand, is **connection-oriented**. This means that once a connection is established between the client and server, the TCP layer maintains the connection state and automatically includes the necessary header information for each packet sent within that connection.
> 2. **UDP** sockets are identified by the **destination IP address and port** number. **TCP** sockets requires BOTH **source AND destination IP address and port** number.
> 3. **UDP segments still include source port and IP**, they're just not needed to identify the socket to be demultiplexed to. The source port and IP allows the destination to know where the data came from. 



