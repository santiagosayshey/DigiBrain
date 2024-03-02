
> [!exercise]+ Exercise 1 - Add a $2n$ digit with an $n$ digit. 
> How many primitive operations does this take? 
> -  $2n$ primitive operations. Even after the $n'th$ digit, we still need to check for carries in a computational context. This means there will always be `max(a,b)` primitive operations
>   
> How many digits does the output have?
> - The same goes for final digits. We take the max of both. At most it can be `max + 1` digits, so in this case it has $2n+1$ digits.
> 


> [!exercise]+ Exercise 2 - Compute `max(A+B, C+D) + E` where A, C have `n` digits, B, D have `3n` digits, and E has `2n` digits.
>
> | Step                       | A + B  | C + D         | max(A+B, C+D)      | max(A+B, C+D) + E     | Explanation                                                                                                                   |
> | -------------------------- | ------ | ------------- | ------------------ | --------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
> | **Primitive Operations**   | 3n     | 3n (6n total) | Minimal (6n total) | 3n + 1 (9n + 1 total) | max(A+B, C+D) + E is 9n+1 primitive operations, because we take 6n + 3n+1 (3n+1 is the # operations taken to sum 3n+1 and 2n) |
> | **Total Digits of Result** | 3n + 1 | 3n + 1        | 3n + 1             | 3n+1                  | The final number of digits in the result can be up to 3n + 2, considering that adding E (2n digits) to the maximum of A+B or C+D (up to 3n + 1 digits) could produce an additional carry, thus potentially increasing the digit count by one. This accounts for the maximum possible digit length resulting from the operations. |



> [!exercise]+ Exercise 3 - Multiply a $2n$ digit number with an `n` digit number
> Contents

