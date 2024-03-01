
> [!idea]+ The Idea
> We need to be able to **measure the performance of our ability to communicate**. We do this by understanding the different delays that occur in network communication.

| Delay Type                          | Description                                                                                                                                                                                                                                                                              | Formula                                     |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| <center>Propagation Delay</center>  | The time it takes for a signal to travel from point A to point B over a network medium. It is influenced by the type of medium, the distance between the points, and typically the speed of the signal, which is often close to $c$, the speed of light $(3 \times 10^8$ m/s) in vacuum. | $$t_p=\frac{Distance}{Speed}$$              |
| <center>Transmission Delay</center> | The time required to transmit all the bits of a packet into the network medium. Packet size is denoted by $L$, and the bandwidth (data carrying capacity) is denoted by $R$.                                                                                                             | $$t_T=\frac{L}{R}$$                         |
| <center>Queuing Delay</center>      | The time a packet spends waiting in a queue before it can be transmitted over the network due to congestion or prior packet processing. If there is no space in the queue (i.e. not enough buffer in the router), that packet is dropped!                                                | Depends on queue length and network traffic |
| <center>Processing Delay</center>   | The time taken by a network device (e.g., router, switch) to process a packet.                                                                                                                                                                                                           | Depends on device and packet complexity     |


> [!exercise]+ Exercise 1
> Which mode of data transfer has the higher propagation delay? (Assuming they are transferred over the same distance)
> 1. Pigeon
> 2. Network
> 
> **Answer:** The pigeon does, clearly. Network speeds reach up to the speed of light. Pigeons fly at about $80 \frac{m}{h}$

