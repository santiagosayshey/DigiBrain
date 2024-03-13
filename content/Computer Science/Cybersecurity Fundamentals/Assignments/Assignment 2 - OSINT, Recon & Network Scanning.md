
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
>
> | **Question**                                          | **Answer**                                       |
> | ------------------------------------------------- | -------------------------------------------- |
> | dunstan.org.au resolves to:                       | (IP address)                                 |
> | Other domain names that resolve to the same       | (List a subset of other domain names that    |
> | address                                           | resolve to the same IP address as above)     |
> | Owner of the IP address                           | (Organisation name according to whois)       |
> | The IP address range which the IP address belongs | (Netblock IP range according to whois)       |
> | The Autonomous System Number (ASN) that contain   | (ASN that contains the IP address range.     |
> | the IP address                                    | e.g., AS1234)                                |
> | Other netblocks registered under the same ASN     | (List of netblocks/ip address ranges)        |
