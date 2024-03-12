
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

