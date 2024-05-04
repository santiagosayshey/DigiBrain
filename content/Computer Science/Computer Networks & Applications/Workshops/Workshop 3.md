
> [!exercise]+ Exercise 1 - IP Subnets
> 
> Are the two IP addresses 129.127.8.8 and 129.127.104.8 in the same subnet? Explain your answer.
> 
> Are the two IP addresses 129.127.8.8/24 and 129.127.104.8/24 in the same subnet? Explain your answer.
> 
> **Answers:**
> 1. In classful networking, the first octet in a Class B address ranges from 128 to 191. They also use the first two octets `xxx.xxx` to define the network portion. Since the first octet in both addresses fall between 128 and 191, and they both have the same first two octets, we can confidently say they are both are class B addresses and therefore belong to the same subnet. 
> 2. To determine if these networks are part of the same subnet, we should convert the address into binary and determine if the first 24 bits (the network bits) are the same. We can quickly notice that the first 24 bits make up the first 3 octets, so we need to only compare the decimal octets to see if they're the same. The third octet is different, so we have a different set of network bits and therefore, the addresses belong to two different subnets.
