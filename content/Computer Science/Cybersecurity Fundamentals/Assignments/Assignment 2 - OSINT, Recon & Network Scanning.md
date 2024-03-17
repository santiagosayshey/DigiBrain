
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
> A Google search for `calcium xss` returns this page on [exploit-db](https://www.exploit-db.com/exploits/31858) as the first result. The page reveals that Calcium is prone to cross script scripting because the `CalenderName` inside the URL is not properly sanitised. 
> 
> i.e. `http://www.example.com/cgi-bin/Calcium40.pl?Op=ShowIt&CalendarName=[xss]`
> 
> ![[Pasted image 20240313085227.png]]
> 
> We can search for sites that use calcium by including `inurl: Calcium40.pl` in the search.
> 
> ![[Pasted image 20240313085633.png]]


> [!exercise]+ Exercise 3
> Use the `whois_pocs` module in recon-ng to list some contacts for x.com. Who is located in Carson, CA?}
> 
> **Answer:**
>
> ```
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
> **Explanation:** This exercise demonstrates using the `whois_pocs` module in Recon-ng to find points of contact associated with the domain `x.com`. By setting the source to x.com and running the module, it retrieves contact information from WHOIS records, pinpointing finding related to the domain. The process identifies Robert Nordland, located in Carson, CA, as a contact.

> [!exercise]+ Exercise 4
> Use the techniques introduced in the workshop to complete the following table.
> 

| **Question**                                      | **Answer**                                |
| ------------------------------------------------- | ----------------------------------------- |
| dunstan.org.au resolves to:                       | 151.101.194.159                           |
| Other domain names that resolve to the same       | (List a subset of other domain names that |
| address                                           | resolve to the same IP address as above)  |
| Owner of the IP address                           | (Organisation name according to whois)    |
| The IP address range which the IP address belongs | (Netblock IP range according to whois)    |
| The Autonomous System Number (ASN) that contain   | (ASN that contains the IP address range.  |
| the IP address                                    | e.g., AS1234)                             |
| Other netblocks registered under the same ASN     | (List of netblocks/ip address ranges)     |

```shell
└─$ dig dunstan.org.au

; <<>> DiG 9.19.19-1-Debian <<>> dunstan.org.au
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 39852
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;dunstan.org.au.                        IN      A

;; ANSWER SECTION:
dunstan.org.au.         900     IN      A       151.101.194.159

;; Query time: 407 msec
;; SERVER: 10.2.0.1#53(10.2.0.1) (UDP)
;; WHEN: Wed Mar 13 00:51:38 EDT 2024
;; MSG SIZE  rcvd: 59
```

```shell
└─$ dig -x 151.101.194.159 

; <<>> DiG 9.19.19-1-Debian <<>> -x 151.101.194.159
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 33930
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;159.194.101.151.in-addr.arpa.  IN      PTR

;; AUTHORITY SECTION:
151.in-addr.arpa.       3600    IN      SOA     pri.authdns.ripe.net. dns.ripe.net. 1710244132 3600 600 864000 3600

;; Query time: 819 msec
;; SERVER: 10.2.0.1#53(10.2.0.1) (UDP)
;; WHEN: Wed Mar 13 00:55:42 EDT 2024
;; MSG SIZE  rcvd: 117
```