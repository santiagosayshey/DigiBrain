# The Postal Analogy

- Data encapsulation in networks is like putting a letter inside multiple envelopes
- Each OSI layer adds its own "envelope" (header) to the data
- Application layer data = the letter itself
- Headers are added from top to bottom layers
- Headers are removed from bottom to top layers at the receiving end


# Delays

| Delay Type | Description | Formula |
|------------|-------------|---------|
| Propagation Delay | Time for signal to travel from source to destination<br>- Depends on distance and signal speed (close to speed of light) | `Propagation delay = Distance / Speed` |
| Transmission Delay | Time to transmit all bits of a packet into the network<br>- Depends on packet size (L) and bandwidth (R) | `Transmission delay = L / R` |
| Queuing Delay | Time a packet waits in a queue before transmission<br>- Depends on queue length and network traffic<br>- If queue is full, packets are dropped | - |
| Processing Delay | Time taken by a network device to process a packet<br>- Depends on device and packet complexity | - |
