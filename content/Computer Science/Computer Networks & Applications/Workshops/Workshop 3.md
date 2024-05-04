
> [!exercise]+ Exercise 1 - IP Subnets
> 
> Are the two IP addresses 129.127.8.8 and 129.127.104.8 in the same subnet? Explain your answer.
> 
> Are the two IP addresses 129.127.8.8/24 and 129.127.104.8/24 in the same subnet? Explain your answer.
> 
> **Answers:**
> 1. They could be, but its impossible to definitively say without knowing what class type the two networks are. If they're both of class A or B, then yes, they are part of the same subnet. On the other hand, if they're type C, then they are NOT part of the same subnet.
> 2. To determine if these networks are part of the same subnet, we should convert the address into binary and determine if the first 24 bits (the network bits) are the same. We can quickly notice that the first 24 bits make up the first 3 octets, so we need to only compare the decimal octets to see if they're the same. The third octet is different, so we have a different set of network bits and therefore, the addresses belong to two different subnets

