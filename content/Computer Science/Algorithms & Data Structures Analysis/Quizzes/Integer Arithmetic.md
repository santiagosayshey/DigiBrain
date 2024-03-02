
> [!exercise]+ Exercise 1 - Add a $2n$ digit with an $n$ digit. 
> How many primitive operations does this take? 
> -  $2n$ primitive operations. Even after the $n'th$ digit, we still need to check for carries in a computational context. This means there will always be `max(a,b)` primitive operations
>   
> How many digits does the output have?
> - The same goes for final digits. We take the max of both. At most it can be `max + 1` digits, so in this case it has $2n+1$ digits.
> 

