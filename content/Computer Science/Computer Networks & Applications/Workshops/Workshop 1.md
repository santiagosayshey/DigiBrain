
> [!exercise]+ Question 1 - Latency Through a Network
> Consider a packet flowing through the Internet over 2 hops (source -> router1 -> destination). Assume that it takes the router 1 msec to process a packet and determine the outgoing link. The simplified network is shown below:
> 
> ![[tute1-network.jpg]]
> 
> Given a propagation speed of $2.5 \times 10^8$ m/s (slightly under the speed of light) and a packet data size of 1000 bytes, what is the end-to-end delay for a packet assuming no other traffic at the router?
> 
> What effect would other traffic at the router have?
> 
> 
> 

Since there is no other traffic at the router, we should consider 3 types of delay - Propagation, Transmission and Processing.


Propagation


Transmi


|                 | **<center>Propagation</center>**                                                                           | **Transmission**                                                                                                                              | **Processing Delay** | **Total** |
| --------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------- |
| **Formula**     | <center>$t_p = \frac{distance}{speed}$</center>                                                            | <center>$t_T = \frac{L}{R}$</center>                                                                                                          | -                    |           |
| **Calculation** | $$\frac{1000 \times 1000 \; m}{2.5 \times 10^8} + \frac{5000 \times 1000 \; m}{2.5 \times 10^8} = 0.024s$$ | $$\frac{1000}{1 \times 1000 \times 1000 \times 8 \; bytes} + \frac{1000}{20 \times 1000 \times 1000 \times 8 \; bytes} = \frac{21}{160000}s$$ | $0.001s$             |           |

