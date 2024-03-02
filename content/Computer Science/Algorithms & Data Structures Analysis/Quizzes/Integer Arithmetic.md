
> [!exercise]+ Exercise 1 - Add a $2n$ digit with an $n$ digit. 
> How many primitive operations does this take? 
> -  $2n$ primitive operations. Even after the $n'th$ digit, we still need to check for carries in a computational context. This means there will always be `max(a,b)` primitive operations
>   
> How many digits does the output have?
> - The same goes for final digits. We take the max of both. At most it can be `max + 1` digits, so in this case it has $2n+1$ digits.
> 



> [!exercise] Exercise 2 - Analyse Addition and Max Operations
> 
> Compute `max(A+B, C+D) + E` where A, C have `n` digits, B, D have `3n` digits, and E has `2n` digits.
> 
> **Primitive operation:** 
> - Starting with A+B. A has `n` digits, B has `3n` digits. The result will have at most `3n+1` digits.
> - For C+D. C
> 
> **Output digit:** 
> 
> _[Your answer here]_
