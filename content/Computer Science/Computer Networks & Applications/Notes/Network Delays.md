
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


> [!exercise]+ Exercise 2
> Which mode of data transfer has the higher transmission delay?
> 1. Pigeon
> 2. Network
> 
> **Answer: ** The network does. Pigeons are capable of carrying much more information at once than a network is capable of. (At least mostly) They could carry some physical disk with hundreds of GB in a single communication. We should also consider how fast we can copy data onto the USB, which is often much quicker than it is to load it into a network. 


> [!exercise]+ Exercise 3
> The NBN has potential speeds of 100 $\frac{Mb}{s}$ download and 40 $\frac{Mb}{s}$ upload. Is it faster to send a $4 GB$ file on a USB using a pigeon?
> 
> **Answer:** Yes. The calculations in the table below clearly show that the network transmission speed is considerably slower. 
> 
| Mode of Communication | <center>Method</center>                                                                                                                  | Calculation: $$t_T=\frac{L}{R}$$                                                   | Total Time  |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------- |
| Pigeon                | Copying data to the USB Drive, then attaching that USB Drive to the pigeons legs. Let's say the USB Drive has a write speed of 100 MB/s. | $$ = \frac{4\times1024\times1024\times1024\; Bytes}{100\times10^6 \;Bytes/s}$$     | 43 Seconds  |
| Network               | Transmitting all the packets inside a bit to the network medium. i.e. Transmitting at 4GB at 40 $mbps$                                   | $$ = \frac{4\times1024\times1024\times1024\times8\; bits}{40\times10^6 \;bits/s}$$ | 859 seconds |
>




