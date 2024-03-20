
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

| **Question**                                                    | **Answer**                                                                                                                                   |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| dunstan.org.au resolves to:                                     | Using `dig dunstan.org.au` we find that the domain name resolves to the IP address: **151.101.194.159**                                      |
| Other domain names that resolve to the same address             | Using `dig -x 151.101.194.159` we find that the domain name resolves to the following addresses: **pri.authdns.ripe.net. and dns.ripe.net.** |
| Owner of the IP address                                         | Using `whois 151.101.194.159`, we find that the owner of the IP address is **Fastly, Inc.**                                                  |
| The IP address range which the IP address belongs               | The previous command `whois 151.101.194.159 ` also shows the range of IP addresses: **151.101.0.0 - 151.101.255.255**                        |
| The Autonomous System Number (ASN) that contains the IP address | Searching for `151.101.194.159` on `shodan.io` reveals that the ASN is: **AS54113**<br><br>![[Pasted image 20240320235132.png]]              |
| Other netblocks registered under the same ASN                   | (List of netblocks/ip address ranges)                                                                                                        |


![[Pasted image 20240317160148.png]]