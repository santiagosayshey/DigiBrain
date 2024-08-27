> [!Idea] **Pipelining**
> Pipelining is a technique used to improve the efficiency of HTTP communication by allowing multiple HTTP requests to be sent out before any responses are received, without waiting for each one to complete in turn.
> 
> **Without Pipelining**
>
> | Time (ms) | Client Actions                | Server Actions       |
> |-----------|------------------------------|----------------------|
> | 0         | Send Request A               | -                    |
> | 100       | -                            | Receive Request A    |
> | 200       | -                            | Process Request A    |
> | 400       | -                            | Send Response A      |
> | 500       | Receive Response A           | -                    |
> | 500       | Send Request B               | -                    |
> | 600       | -                            | Receive Request B    |
> | 700       | -                            | Process Request B    |
> | 900       | -                            | Send Response B      |
> | 1000      | Receive Response B           | -                    |
> | 1000      | Send Request C               | -                    |
> | 1100      | -                            | Receive Request C    |
> | 1200      | -                            | Process Request C    |
> | 1400      | -                            | Send Response C      |
> | 1500      | Receive Response C           | -                    |
> 
> **With Pipelining**
> 
> | Time (ms) | Client Actions                | Server Actions       |
> |-----------|------------------------------|----------------------|
> | 0         | Send Request A               | -                    |
> | 100       | Send Request B               | Receive Request A    |
> | 200       | Send Request C               | Receive Request B    |
> | 300       | -                            | Receive Request C    |
> | 400       | -                            | Process Request A    |
> | 600       | -                            | Send Response A      |
> | 700       | -                            | Process Request B    |
> | 800       | Receive Response A           | -                    |
> | 900       | -                            | Send Response B      |
> | 1000      | -                            | Process Request C    |
> | 1100      | Receive Response B           | -                    |
> | 1200      | -                            | Send Response C      |
> | 1300      | Receive Response C           | -                    |
