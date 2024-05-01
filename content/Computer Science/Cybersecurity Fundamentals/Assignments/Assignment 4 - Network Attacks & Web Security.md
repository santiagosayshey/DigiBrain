
> [!exercise]+ Exercise 1 - DHCP Attack
> Another type of attack that was not included in the workshop is DHCP (dynamic host configuration protocol) based attacks. Do a bit of research into how DHCP works and about some DHCP attacks and answer the following questions.
> 1. What are the 4 packets (messages) that are communicated between the client seeking and IP address and the DHCP server?
> 2. Are the 4 messages Layer 2 unicast or broadcast (be careful not to confuse between Layer 3 broadcast, which is sending to an IP broadcast address like 10.0.2.255, as opposed to Layer 2 broadcast which is sent to MAC address FF:FF:FF:FF:FF:FF).
> 3. Therefore, in a switched network, which of the 4 messages in the DHCP negotiation would the attacker be able to observe?
> 4. Briefly explain what DHCP spoofing and DHCP starvation attacks are executed, and how the two can be used in combination. 
> 5. For an adversary looking to perform MITM, which DHCP configuration option(s) would you try to manipulate? 
> 6. Briefly explain how "DHCP **snooping**" configuration in a switch work to prevent DHCP **spoofing**?


> [!exercise]+ Exercise 2 - MITM Prevention
> 1. Briefly explain (1 or 2 sentences max) how HTTPS can defeat MITM via ARP cache poisoning.
> 2. In the same context, why did Chrome developers decided to display "Not Secure" on HTTP websites?
> 3. In the same context, what's the danger of ignoring a browser error message like this one and clicking on "Continue to this website"?
> 4. Briefly write an explanation that you might provide to your grandparent (or anyone who may not be IT savvy) why they should be careful when connecting to open WiFi hotspots like the ones at airports.



> [!exercise]+ Exercise 3 
> Go to `http://<Your Hacklab VM IP addr>:8081/method.php` to get the secret!
> 
> **Answer:**
> Initially, I tried visiting the site in my browser but only received a hint: `"Hm... you don't seem to be using the correct METHOD. Explore your available OPTIONS."` This made it clear that I should attempt an `OPTIONS` request via `curl`.
> 
> ```bash
> curl -X OPTIONS http://192.168.56.113:8081/method.php
> ```
> 
> This returned the flag:
> ```
> csf2021_{helper-evaluate-mammogram}
>```


> [!exercise]+ Exercise 4
> Access `http://192.168.56.113:8081/admin.php` to get the secret!
> 
> **Answer:**
> I visited the page and clicked on the request button, which revealed the hint: `"Sorry, only superadmins are allowed to see the secret."` This led me to inspect the cookies via the browser’s developer tools.
> 
> I adjusted the `superuser` cookie to `true` and clicked on the request button again:
> 
> ```
> Welcome Super User! Here is the secret: csf2021_{client-postbox-amid}
> ```
> 
> ![[Pasted image 20240502052455.png]]

