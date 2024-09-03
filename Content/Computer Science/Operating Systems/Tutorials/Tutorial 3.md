> [!exercise] Question 1: Concurrent Threads and Shared Variables
> The following program consists of two concurrent threads that shared the variable x.
> ```
> int x = 1;
> Thread T1: Do_something; x = x*2; print x
> Thread T2: Read 4 values; x = x+4;
> ```
> Give all possible final values of the variable x after the two threads run.
> 
> **Answer:**
> There are several possible scenarios due to the concurrent nature of the threads:
> 
> 1. T1 runs completely before T2:
>    - x = 1 * 2 = 2 (T1)
>    - x = 2 + 4 = 6 (T2)
>    - Final value: 6
> 
> 2. T2 runs completely before T1:
>    - x = 1 + 4 = 5 (T2)
>    - x = 5 * 2 = 10 (T1)
>    - Final value: 10
> 
> 3. T1 and T2 interleave, T1 reads x before T2 modifies it:
>    - T1 reads x (1), T2 modifies x (1 + 4 = 5), T1 completes (1 * 2 = 2)
>    - Final value: 2
> 
> 4. T1 and T2 interleave, T2 modifies x before T1 reads it:
>    - T2 modifies x (1 + 4 = 5), T1 reads and modifies x (5 * 2 = 10)
>    - Final value: 10
> 
> 5. T1 and T2 read the initial value simultaneously:
>    - Both threads read x as 1
>    - T1 sets x to 2, T2 sets x to 5
>    - Final value depends on which thread writes last: either 2 or 5
> 
> Therefore, the possible final values of x are: 2, 5, 6, and 10.

> [!exercise] Question 2: Extended Concurrent Threads with Locks
> The program was extended to three concurrent threads and two locks were added.
> ```
> int x = 1;
> lock_t lc1, lc2;
> Thread T1: Do_something; lock(lc1);lock(lc2); x = x*2;
> unlock(lc2); unlock(lc1);
> Thread T2: lock(lc2); x = x+4; unlock(lc2);
> Thread T3: lock(lc1); x = x*x; unlock(lc1);
> ```
> Remember that any thread may attempt to run in any order.
> 
> a) Describe one order that works well and another possible order that will result in a race condition.
> 
> b) Will the use of a multicore processor increase or decrease the chance to get the race condition
> 
> c) Can you fix the use of the locks to achieve the desired outcome.
> 
> **Answer:**
> 
> a) An order that works well:
>    T1 -> T2 -> T3
>    This order ensures that each thread completes its operation before the next one starts, avoiding any race conditions.
>    
>    An order that results in a race condition:
>    T2 acquires lc2, T3 acquires lc1, T1 attempts to acquire both locks
>    This can lead to a deadlock as T1 waits for lc2 (held by T2) and T2 waits for lc1 (held by T3).
> 
> b) The use of a multicore processor would **increase** the chance of encountering a race condition. With multiple cores, threads can truly run in parallel, increasing the likelihood of interleaved executions and potential race conditions.
> 
> c) To fix the use of locks and achieve the desired outcome:
>    - Implement a consistent order of lock acquisition across all threads to prevent deadlocks.
>    - Use a single lock for all critical sections to ensure mutual exclusion.
>    
>    Modified code:
>    ```
>    int x = 1;
>    lock_t lock;
>    
>    Thread T1: Do_something; lock(lock); x = x*2; unlock(lock);
>    Thread T2: lock(lock); x = x+4; unlock(lock);
>    Thread T3: lock(lock); x = x*x; unlock(lock);
>    ```
>    
>    This ensures that only one thread can modify x at a time, preventing race conditions and maintaining data consistency.

> [!exercise] Question 3: Producer-Consumer Problem with Condition Variables
> Below you can read a solution of the Producer-Consumer Problem that uses a lock M in combination with two condition variables to make the producer sleep when the buffer is full, and to make the consumer sleep when the buffer is empty.
> 
> Note the shared buffer b is a circular buffer of capacity for n items. The variable in points to the next gap, and the variable out points to the item to be consumed. When both point to the same item, it means the buffer if empty. When in points to the item before out, it means the buffer is full.
> 
> ```
> Producer
> while (true) {
> /*produce item v */
> pt_lock (&M);
> while ((in + 1) % n == out)
>     pt_cond_wait(&Out_CV, &M);
> b [in] = v;
> in = (in + 1) % n;
> pt_cond_signal (&In_CV);
> pt_unlock (&M);
> }
> 
> Consumer
> while (true) {
> pt_lock (&M);
> while (in == out)
>     pt_cond_wait(&In_CV, &M);
> w = b [out];
> out = (out + 1) % n;
> pt_unlock (&M);
> pt_cond_signal (&Out_CV);
> /*consume item w */
> }
> ```
> 
> The semantics for the condition variables operations are explained below:
> 
> pt_cond_wait (&CV, &Mutex);
> 1. unlock the mutex
> 2. sleep for a while (may wake up at any time)
> 3. relock the mutex
> 
> pt_cond_signal (&CV);
> wake up at least one of the threads (if any) that is sleeping on the CV
> 
> The analogy to a person sleeping in a side room fits the pthread_cond_signal operation. A thread that is waiting on a call to pthread_cond_wait may wake up at any time, just as a person who goes to bed may wake up before the alarm clock goes off.
> 
> When some other thread calls pthread_cond_signal for the given CV, the effect is similar to someone ringing a loud alarm bell in the side "room" that corresponds to the CV. If there is a thread waiting on a CV, it is guaranteed to wake up when that CV is signaled. If there are several threads waiting on the same CV, at least one is guaranteed to wake up. (Whether more than one wakes up depends on the implementation.) If there is no thread waiting on the CV, the pthread_cond_signal call has no effect.
> 
> Explain what happens when:
> 
> a) The buffer is full, and the producer wants to put one item.
> 
> b) The buffer contains 3 items, and the consumer reads one item.
> 
> c) The buffer contains 1 item, and the consumer reads that item.
> 
> **Answer:**
> 
> a) When the buffer is full and the producer wants to put one item:
>    - The producer acquires the lock M.
>    - It checks the condition `(in + 1) % n == out`, which is true (buffer is full).
>    - The producer calls `pt_cond_wait(&Out_CV, &M)`, which:
>      1. Releases the lock M
>      2. Puts the producer thread to sleep, waiting on Out_CV
>      3. When awakened, it will reacquire the lock M
>    - The producer remains asleep until a consumer signals Out_CV after consuming an item.
> 
> b) When the buffer contains 3 items and the consumer reads one item:
>    - The consumer acquires the lock M.
>    - It checks the condition `in == out`, which is false (buffer is not empty).
>    - The consumer reads the item from `b[out]`.
>    - It updates `out = (out + 1) % n`.
>    - The consumer releases the lock M.
>    - It signals Out_CV, potentially waking up a waiting producer.
>    - The consumer then processes the read item.
> 
> c) When the buffer contains 1 item and the consumer reads that item:
>    - The consumer acquires the lock M.
>    - It checks the condition `in == out`, which is false (buffer is not empty).
>    - The consumer reads the item from `b[out]`.
>    - It updates `out = (out + 1) % n`.
>    - After this update, `in == out` becomes true, indicating an empty buffer.
>    - The consumer releases the lock M.
>    - It signals Out_CV, potentially waking up a waiting producer.
>    - The consumer then processes the read item.
>    - The next time a consumer tries to read, it will wait on In_CV until a producer adds an item.

![[Pasted image 20240903215802.png]]