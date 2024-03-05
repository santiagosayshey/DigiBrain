> [!exercise]+ Question 1 - Latency Through a Network
> Consider a packet flowing through the Internet over 2 hops (source -> router1 -> destination). Assume that it takes the router 1 msec to process a packet and determine the outgoing link. The simplified network is shown below:
> 
> ![[tute1-network.jpg]]
> 
> Given a propagation speed of $2.5 \times 10^8$ m/s (slightly under the speed of light) and a packet data size of 1000 bytes, what is the end-to-end delay for a packet assuming no other traffic at the router?
> 
> What effect would other traffic at the router have?
> <hr>
> 
> **Answer**: 
> Since there is no other traffic at the router, we should consider 3 types of delay - Propagation, Transmission and Processing. If there was other traffic at the router, we would have to also consider a queuing delay!
> 
> 
> |             | **Propagation $(t_p = \frac{\text{distance}}{\text{speed}})$**                                                         | **Transmission $(t_T = \frac{L}{R})$**                                                                                                             | **Processing Delay** | **Total** |
> | ----------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------- |
> | **Calculation** | $\frac{1000 \times 1000 \; m}{2.5 \times 10^8 \; m/s} + \frac{5000 \times 1000 \; m}{2.5 \times 10^8 \; m/s} = 0.024s$ | $\frac{1000 \times 8 \; bits}{1 \times 1000 \times 1000 \; bits/s} + \frac{1000 \times 8 \; bits}{20 \times 1000 \times 1000 \; bits/s} = 0.0084s$ | $0.001s$             | $0.034s$  |
> 
> 
