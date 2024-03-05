> [!exercise]+ Exercise 1 - Latency Through a Network
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

> [!exercise]+ Exercise 2 - Packet switching and Circuit switching (K&R)
> Assume that you are sharing a link with a bandwidth of 2 Mbps at home. Assume that each member of your family, when using the link, transmits continuously at 1 Mbps but each member transmits only 20 percent of the time.
> 
> 1. If you set-up your network to circuit switching, how many family members can be supported simultaneously (remember, in circuit switching, resources are reserved for each user)?
> 2. Now, let’s assume that you’ve re-designed the network to support packet switching and re-consider how many active (simultaneous users can be supported).
> 
> **I.** Why will there not be a queuing delay at the devices waiting to use the link if two or fewer users transmit at the same time?
> **II.** Why will there be a queuing delay at the devices attempting to use the link, if three users transmit at the same time?
> **III.** What is the probability that a given user is transmitting at any given time?
> **IV.** Now re-consider the situation of three users transmitting at the same time. First, find the probability that at any given time, all three users are transmitting simultaneously. Now find the fraction of time during which the queue grows.
> 
> **Answer:**
> 
> **1.** A circuit switch with 2 mbps of bandwidth would only be able to support 2/4 family members at a time at 1mbps each. 
> 
> **I.** There is enough bandwidth to support 2 users at once. 1 mbps each at 2 mbps total. 
> **II.** There is **NOT** enough bandwidth to support 3 users at once. A queuing delay will occur because 3 Mb are trying to be transmitted at once with only 2 mbps total bandwidth. 
> **III.** 20%. Each family member hash a probability of 20% to transmit at any one time. 
> **IV.** Any three users transmitting at the same time is $\frac{1}{5} \times \frac{1}{5} \times \frac{1}{5} = 0.8\%$ 
