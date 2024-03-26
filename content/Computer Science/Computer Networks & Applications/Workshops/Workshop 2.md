
> [!exercise]+ Question 1 (Multiplexing/Demultiplexing)
> - The UDP header does not contain any information that is not present in the TCP header (verify this for yourself). That being the case, why do you, as a programmer, have to specify the header information (ports and IP addresses) whenever you send a UDP packet; but you don't when you send a TCP packet?
> - How is a UPD socket fully identified? How is a TCP socket fully identified?
> - Assume a web application in Host A has a UDP socket bound to port number 8080. Now Host B and C each sends UDP segment to Host A with destination port number 8080. Will both segments be directed to the same socket at Host A? If so, how will the process at Host A know that these that these two segments originated from two different hosts?



