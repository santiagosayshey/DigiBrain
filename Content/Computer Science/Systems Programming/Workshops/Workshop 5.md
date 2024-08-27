```console
gcc -o prod_cons prod_cons.c buffer.c assert.c -lpthread

prod_cons

P: Starting
C: Starting
P: |one|
P: |two|
P: |three|
P: |four|
P: |five|
P: |six|
P: |seven|
P: |eight|
C: |one|
C: |two|
C: |three|
C: |four|
C: |five|
C: |six|
C: |seven|
C: |eight|
P: |nine|
P: |ten|
P: ||
P: Ending
C: |nine|
C: |ten|
C: ||
C: Ending
```

Explanation: Producer - Consumer Problem

1.  The producer thread produces items (in this case, lines of text from a file) and places them into the buffer.
    
2.  The consumer thread removes items from the buffer and processes them (in this case, by printing the lines).
    
3.  To ensure proper synchronization and avoid potential race conditions, the code uses a mutex and two condition variables, `notFull` and `notEmpty`.
    
    -   The `notFull` condition variable is used to block the producer from adding items when the buffer is full.
        
    -   The `notEmpty` condition variable is used to block the consumer from removing items when the buffer is empty.
        

This way, both the producer and consumer can operate concurrently without interfering with each other, ensuring the correct operation of the program.

