
> [!exercise]+ Exercise 1
> Search on the University of Adelaide domain for a PDF document containing the word "crucifixion" **in the title** of the document. (a) What is the Google search syntax and (b) who is the author of the PDF file?
> 
> **Answer:**
> - Search Query Used: `site:adelaide.edu.au intitle:crucifixion filetype:pdf`
> - Author: Felicity Harley
>   
> ![[Pasted image 20240313083552.png]]

> [!exercise]+ Exercise 2
> Google dorks are good at finding vulnerabilities in websites. Do a quick research for the cross-site scripting (XSS) vulnerability in a product called Calcium by Brown Bear Software (you will learn about XSS in subsequent modules). What google search would you perform to find websites running Calcium? Perform the search, and paste a screenshot of the results.
> 
> **Answer:**
> A Google search for `site:www.exploit-db.com calcium xss` returns this page on [exploit-db](https://www.exploit-db.com/exploits/31858) as the first result. The page reveals that Calcium is prone to cross script scripting because the `CalenderName` inside the URL is not properly sanitised. 
> 
> i.e. `http://www.example.com/cgi-bin/Calcium40.pl?Op=ShowIt&CalendarName=[xss]`
> 
> ![[Pasted image 20240313085227.png]]
> 
> We can search for sites that use calcium by including `inurl:Calcium40.pl` in the search.
> 
> ![[Pasted image 20240321000359.png]]

> [!exercise]+ Exercise 3
> Use the `whois_pocs` module in recon-ng to list some contacts for x.com. Who is located in Carson, CA?}
> 
> **Answer:**
>
> ```shell
> [recon-ng][assignment2][whois_pocs] > options set SOURCE x.com
> SOURCE => x.com
> [recon-ng][assignment2][whois_pocs] > run
>
> ...
> [*] --------------------------------------------------
> [*] URL: http://whois.arin.net/rest/poc/RNO51-ARIN
> [*] Country: United States
> [*] Email: x@x.com
> [*] First_Name: Robert
> [*] Last_Name: Nordland
> [*] Middle_Name: None
> [*] Notes: None
> [*] Phone: None
> [*] Region: Carson, CA
> [*] Title: Whois contact
> ```
>
> **Explanation:** Using the `whois_pocs` module in Recon-ng I was able to find points of contact associated with the domain `x.com`. By setting the source to x.com and running the module, it retrieves contact information from WHOIS records, finding information related to the domain. The process identifies **Robert Nordland**, located in Carson, CA, as a contact.

> [!exercise]+ Exercise 4
> Use the techniques introduced in the workshop to complete the following table.
> 
> | **Question**                                                    | **Answer**                                                                                                                                   |
> | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
> | dunstan.org.au resolves to:                                     | Using `dig dunstan.org.au` we find that the domain name resolves to the IP address: **151.101.194.159**                                      |
> | Other domain names that resolve to the same address             | Using `dig -x 151.101.194.159` we find that the domain name resolves to the following addresses: **pri.authdns.ripe.net. and dns.ripe.net.** |
> | Owner of the IP address                                         | Using `whois 151.101.194.159`, we find that the owner of the IP address is **Fastly, Inc.**                                                  |
> | The IP address range which the IP address belongs               | The previous command `whois 151.101.194.159 ` also shows the range of IP addresses: **151.101.0.0 - 151.101.255.255**                        |
> | The Autonomous System Number (ASN) that contains the IP address | Searching for `151.101.194.159` on `shodan.io` reveals that the ASN is: **AS54113**<br><br>![[Pasted image 20240320235132.png]]              |
> | Other netblocks registered under the same ASN                   | Searching for `AS54113` on `https://ipinfo.io/AS54113`, we find the following netblocks:<br><br>![[Pasted image 20240321000552.png]]         |

> [!exercise]+ Exercise 5
> Create a free account on shodan.io ([https://shodan.io](https://shodan.io)). You will be entitled to an academic upgrade if you register using your @student.adelaide.edu.au or @adelaide.edu.au account. Learn a bit about the Shodan search modifiers, similar to the Google ones (e.g., see [here](https://thor-sec.com/cheatsheet/shodan/shodan_cheat_sheet/) ) . Search for information on hosts under the company "Pfizer" and answer the following questions. Start with the "org:" modifier.
>
> | **Question**                                                                                                                  | **Answer**                                                                                                                                                                                                                                                                                                                                                                        |
> | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | What web server(s) are used by this company?                                                                                  | We can use the `org` modifier to narrow down results to Pfizer. Since web servers use ports `80 and 443` for HTTP and HTTPS respectively, we can add this to our search as well:<br><br>`org:"Pfizer" port:80,443` <br><br>This shows that the majority of web servers used by Pfizer are **nginx, Apache and Microsoft IIS**<br><br>![[Pasted image 20240321002555.png]]<br><br> |
> | What versions of OpenSSH are used by this company?                                                                            | By adding `product: "OpenSSH"` to our search, we can narrow down results that include OpenSSH as a product. This shows that versions **7.4 and 5.9** of OpenSSH are used:<br><br>`org:"Pfizer" product:"OpenSSH"`<br><br>![[Pasted image 20240321003023.png]]                                                                                                                     |
> | According to Shodan, what are some of the vulnerabilities in one of the versions of the OpenSSH servers?                      | Clicking on version 7.4 and the first result: https://www.shodan.io/host/168.224.206.40 shows the following vulnerabilities (not all shown):<br><br>![[Pasted image 20240321010242.png]]                                                                                                                                                                                          |
> | Choose the **most recent** vulnerability from above, and find the **CVSS2.0 string** for it by looking it up on nvd.nist.gov. | Searching for the vulnerability on nvd.gist.gov shows that no information exists v2, but does for v3.<br><br>![[Pasted image 20240321011624.png]]<br><br>![[Pasted image 20240321011632.png]]<br>                                                                                                                                                                                 |

> [!exercise]+ Exercise 6
> Write a simple DNS brute-force script in your language of choice to enumerate hostnames under a given domain and an input dictionary. Run the code against **adelaide.edu.au** using [this dictionary file](https://myuni.adelaide.edu.au/courses/95262/files/14689596?wrap=1 "dnsmap-2.zip") (this file contains the entire 3-character permutations - please unzip before use). _**Running the whole list will take a long time, so you can stop after a few minutes.**_ Paste some preliminary results.
> 
> Here is a sample code for Python3:  
> ```python
> #!/usr/bin/env python3  
> import sys, socket  
> socket.setdefaulttimeout(0.1) # set timeout to 100ms  
> host = "www.adelaide.edu.au"  
> try:  
>    ip = socket.gethostbyname(host)  
>     print(f"{host} resolves to {ip}")  
> except:  
>     pass # ignore error
> ```
> 
> **Answer:**
> 
> I adjusted the existing script by specifying a dictionary file, `dnsmap.txt`, and targeting the `adelaide.edu.au` domain for DNS brute-forcing. The script reads through each line of the dictionary, attempting to resolve each subdomain against the specified domain. If a resolution is successful, it prints out the fully qualified domain name along with its IP address.
> 
> ```python
> #!/usr/bin/env python3
> import sys
> import socket
> 
> socket.setdefaulttimeout(0.1)
> 
> base_domain = "adelaide.edu.au"
> dictionary_path = "dnsmap.txt"
> 
> def dns_brute_force(domain, dict_path):
>     with open(dict_path, 'r') as file:
>         for line in file:
>             subdomain = line.strip()
>             fqdn = f"{subdomain}.{domain}"  # Fully Qualified Domain Name
>             try:
>                 ip = socket.gethostbyname(fqdn)
>                 print(f"{fqdn} resolves to {ip}")
>             except socket.gaierror:
>                 pass  # Ignore error, subdomain doesn't resolve
> 
> # Run the brute force
> dns_brute_force(base_domain, dictionary_path)
> ```
> 
> **Results: (after a few minutes)**
> 
> ```shell
> samchau@SamPC:~/assignment2$ python3 dns.py
> m.adelaide.edu.au resolves to 129.127.149.1
> av.adelaide.edu.au resolves to 129.127.95.145
> cp.adelaide.edu.au resolves to 129.127.149.31
> cs.adelaide.edu.au resolves to 129.127.149.1
> gg.adelaide.edu.au resolves to 129.127.144.5
> gp.adelaide.edu.au resolves to 192.43.227.193
> id.adelaide.edu.au resolves to 35.71.156.117
> ks.adelaide.edu.au resolves to 129.127.43.66
> mw.adelaide.edu.au resolves to 129.127.144.69
> ns.adelaide.edu.au resolves to 129.127.40.3
> ...
> ```

> [!exercise]+ Exercise 7
> Use the Wayback Machine to find out how Access Adelaide (access.adelaide.edu.au) looked like in 2009. How does it look compared to the current Access Adelaide web page?
> 
>**Answer:**
>
>On the Wayback Machine site, I searched for `access.adelaide.edu.au` and clicked on a date from 2009. The site looks identical to how looks today (perhaps its time for a refresh?)
>
>![[Pasted image 20240321020056.png]]

> [!exercise]+ Exercise 8
> There is a network service running on the Hacklab VM behind a port somewhere between 20000 and 60000.
> 1. Identify the port number and connect to it using `netcat` (“`nc`” or “`netcat`” command) to retrieve the secret.
> 2. Paste a screenshot showing the secret answer.
> 3. Explain how you identified and retrieved the secret answer.
> 
> **Answer:**
> 
> Using `sudo nmap -p 20000-60000 -sS 192.168.56.113 -T5`, we can identify the open port (`-T5` because I can't be bothered waiting). We find that the desired port is **21245**.
> ```shell
> └─$ sudo nmap -p 20000-60000 -sS 192.168.56.113 -T5
> Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-20 12:01 EDT
> 
> Nmap scan report for 192.168.56.113
> Host is up (0.0020s latency).
> Not shown: 39999 filtered tcp ports (no-response)
> 
> PORT      STATE  SERVICE
> 20245/tcp closed unknown
> 21245/tcp open   unknown
> 
> MAC Address: 08:00:27:67:09:48 (Oracle VirtualBox virtual NIC)
> Nmap done: 1 IP address (1 host up) scanned in 170.97 seconds
> 
> └─$ nc 192.168.56.113 21245
>  _________________________________________
> / csf2024s1_{adaptably-wesleyan-didelphia \
> \ }                                       /
>  -----------------------------------------
>         \   ^__^
>          \  (oo)\_______
>             (__)\       )\/\
>                 ||----w |
>                 ||     ||
> ```



> [!exercise]+ Exercise 9
The Hacklab VM is running what’s known as a “port knocking” that opens a previously closed port 12345 for a limited time if you send a series of SYN packets to these 3 ports: 2201, 2211, 2234 (be careful, there is a timeout of 15 seconds, so you may have to write a simple script).    
>1. Connect to port 12345 using netcat to get the secret. 
>2. Paste a screenshot showing the secret answer.      
>3. Explain how you identified and retrieved the secret answer.

