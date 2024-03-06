This workshop uses notes on [[1.2 Network Delays]], [[2.1 HTTP]], [[2.2 Caching]], [[2.4 DNS]] and [[2.5 P2P]]. Review those for more details.

Workshop 1 answers by [Samuel Chau.](https://github.com/santiagosayshey) 

> [!exercise]+ Exercise 1 - Latency Through a Network
> Consider a packet flowing through the Internet over 2 hops (source -> router1 -> destination). Assume that it takes the router 1 msec to process a packet and determine the outgoing link. The simplified network is shown below:
> 
> ![[tute1-network.jpg]]
> 
> Given a propagation speed of $2.5 \times 10^8$ m/s (slightly under the speed of light) and a packet data size of 1000 bytes, what is the end-to-end delay for a packet assuming no other traffic at the router?
> 
> What effect would other traffic at the router have?

Since there is no other traffic at the router, we should consider 3 types of delay - Propagation, Transmission and Processing. If there was other traffic at the router, we would have to also consider a queuing delay!

|                 | **Propagation $(t_p = \frac{\text{distance}}{\text{speed}})$**                                                         | **Transmission $(t_T = \frac{L}{R})$**                                                                                                             | **Processing Delay** | **Total** |
| --------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------- |
| **Calculation** | $\frac{1000 \times 1000 \; m}{2.5 \times 10^8 \; m/s} + \frac{5000 \times 1000 \; m}{2.5 \times 10^8 \; m/s} = 0.024s$ | $\frac{1000 \times 8 \; bits}{1 \times 1000 \times 1000 \; bits/s} + \frac{1000 \times 8 \; bits}{20 \times 1000 \times 1000 \; bits/s} = 0.0084s$ | $0.001s$             | $0.034s$  |


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

**1.** A circuit switch with 2 mbps of bandwidth would only be able to support 2/4 family members at a time at 1mbps each. 

**I.** There is enough bandwidth to support 2 users at once. 1 mbps each at 2 mbps total. 
**II.** There is **NOT** enough bandwidth to support 3 users at once. A queuing delay will occur because 3 Mb are trying to be transmitted at once with only 2 mbps total bandwidth. 
**III.** 20%. Each family member hash a probability of 20% to transmit at any one time. 
**IV.** Any three users transmitting at the same time is $\frac{1}{5} \times \frac{1}{5} \times \frac{1}{5} = 0.8\%$ 


> [!exercise]+ Exercise 3 - Peer to Peer (P2P) and Client Server (K&R)
> Consider distributing a file of 10 Gbits ($10 \times 10^9$ bits) to _N_ peers. The server has an upload rate of 20 Mbps, and each peer has a download rate of 1Mbps and an upload rate of _u_. For N=10, 100 and 1,000 and u=200 Kbps, 600 Kbps, and 1Mbps, prepare a chart giving the minimum distribution time for each of the combinations of _N_ and _u_ for both client-server distribution and P2P distribution.
> 
> How close would this approximation be to bit torrent's performance?

Recall: 
$$
D_{cs} \geq \max \left( \frac{NF}{u_s}, \frac{F}{d_{min}} \right)
$$
$$
D_{p2p} \geq \max \left( \frac{F}{u_s}, \frac{F}{d_{min}}, \frac{NF}{\sum_{i=1}^{N} u_i} \right)
$$

Because I'm lazy, here's a python script to calculate the distribution times, along with a table showing the times for each subset of $N$ and $u$ and a graph comparing the two.

```python
# Constants
F = 10e9  # file size in bits
u_s = 20e6  # server upload rate in bits per second
d_min = 1e6  # peer download rate in bits per second

# Scenarios
N_values = [10, 100, 1000]  # number of peers
u_values = [200e3, 600e3, 1e6]  # peer upload rates in bits per second

# Calculate distribution time for Client-Server and P2P for each scenario

for N in N_values:
    for u in u_values:
        u_total = N * u
        D_cs = max(N*F/u_s, F/d_min) / 60
        D_p2p = max(F/u_s, F/d_min, N*F/u_total) / 60
        print(f'For {N} peers at {u} bits per second:')
        print(f'D_cs = {D_cs}')
        print(f'D_p2p = {D_p2p}')
        print() 
		
```

**Client-Server Distribution Time**

| N (Number of Peers) | u=200 Kbps | u=600 Kbps | u=1000 Kbps |
|---------------------|------------|------------|-------------|
| 10                  | 166.67     | 166.67     | 166.67      |
| 100                 | 833.33     | 833.33     | 833.33      |
| 1000                | 8333.33    | 8333.33    | 8333.33     |

**P2P Distribution Time**

| N (Number of Peers) | u=200 Kbps | u=600 Kbps | u=1000 Kbps |
|---------------------|------------|------------|-------------|
| 10                  | 833.33     | 277.78     | 166.67      |
| 100                 | 833.33     | 277.78     | 166.67      |
| 1000                | 833.33     | 277.78     | 166.67      |
![[Figure_1.png]]

**I have a feeling I've screwed something up in the calculations? :/**


> [!exercise]+ Exercise 4 - HTTP
> Why does HTTP specify a blank line between the headers and the entity body for requests and responses? Could HTTP have been designed without this blank line? Explain why or why not.
> 
> Is the content-length header necessary? Explain.

The blank line, specifically `\r\n` delimiters are used to tell the interpreter when the headers stop and the entity body starts.  Could HTTP be designed without this line? Yes, but there would still need to be some standard to determine when the headers end. 

Necessary? No, I don't think so. It is useful, in that it helps with buffering / memory allocation, efficient data transfer, error handling and a million other reasons an endpoint might want the size of a webpage, but it's certainly not necessary. In terms of the HTTP standard, the only 'necessary' information is the request line, i.e. `method | url | version`


> [!exercise]+ Exercise 5 - Caching and DNS
>
> Assume you are using persistent HTTP and request a web page that contains two images. Explain the events that must occur if:
>
> 1. The web page and images are cached in the web proxy cache and the domain is not cached in the local DNS
>
> 2. The web page is not cached; but the domain is cached in the local DNS
>
> 3. Neither the web page nor the domain is cached.
>
> In case 3, how much time is likely to pass between the time the user clicks on the link until the web page is loaded? Assume the user is in Adelaide connected to the Internet through an ADSL modem and they are accessing a website in Sydney (about 1500 Kms away). Be creative in how you could work this out (or at least estimate it).

**1.** The web proxy cache immediately provides the web page and images to the client from its cache. Simultaneously, the local DNS, lacking the domain information, either prompts the client to query higher-level DNS servers or does so itself. This process repeats until a DNS server resolves the domain name, caching the IP address for future use.

**2.** The local DNS cache resolves the domain query. The proxy server does not have the web page and images, so requests them from the origin server to be sent back to the client and caches them for any future requests. 

**3.** A DNS query is initiated because the domain is not in the local DNS cache. With the IP address now known, the client sends a request to the origin server for the web page. The server processes the request and sends back the web page and images to the proxy server where it is cached and sent back to the client.

- **DNS Resolution Time:** Estimated at 150 milliseconds, for the domain name resolution process.
- **Propagation Delay:** With the speed of light at $3×10^8$ meters per second, the calculation for the signal to travel through fibre optic cables from Adelaide to Sydney and back is considered.
- **ADSL Latency:** An estimated additional delay of 10 milliseconds according to [this](https://www.freedomsat.co.uk/articles/what-is-latency)
- **Server Processing Time:** Approximately 100 milliseconds is allocated for the server to process the web page request and begin the response.