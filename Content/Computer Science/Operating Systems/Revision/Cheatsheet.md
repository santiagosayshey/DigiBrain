# Concurrency Cheatsheet

**Concurrency**: Sequential execution underutilizes resources and limits performance, so we introduce concurrency to interleave execution of multiple threads or processes, improving resource utilization and responsiveness.

**Race Conditions**: Arise when concurrent threads or processes access shared resources simultaneously, leading to unpredictable results due to interleaved operations.

**Critical Sections**: Segments of code accessing shared resources that must be protected from concurrent access to prevent race conditions.

**Locks**: Used to ensure mutual exclusion, allowing only one thread to access a critical section at a time.

**Lock Implementation**:

- **Correctness Goals**: Ensure mutual exclusion, deadlock-free (progress), and starvation-free (bounded waiting).
- **Fairness**: Provide equal opportunity for threads to acquire the lock.
- **Performance**: Minimize overhead and maximize efficiency.

**Lock Implementation Techniques**:

- **Disabling Interrupts**: Temporarily disable interrupts during critical sections to prevent context switches (works only on uniprocessor systems; monopolizes CPU).
- **Simple Flag with Load/Store**: Non-atomic operations can lead to race conditions.
- **Atomic Instructions**: Use hardware-supported atomic operations like Test-and-Set and Compare-and-Swap (CAS) to implement locks.

**Spin Locks**: Threads repeatedly check (spin) until the lock becomes available.

- **Use When**: Critical sections are short; low contention; overhead of context switching is higher than spinning.
- **Problems**: Consumes CPU cycles while waiting; not energy-efficient.

**Blocking Locks**: Threads block (sleep) if the lock is unavailable, freeing up CPU resources.

- **Use When**: Critical sections are long; high contention; CPU efficiency and power saving are priorities.

**Condition Variables**: Allow threads to wait for certain conditions to be met and to signal other threads.

- **wait(mutex)**: Thread releases the mutex and waits; upon waking, it re-acquires the mutex.
- **signal()**: Wakes up one waiting thread.
- **broadcast()**: Wakes up all waiting threads.
- **Usage Rule**: Always recheck the condition after waking to handle spurious wakeups.

**Semaphores**: Synchronization primitive with a non-negative integer value.

- **wait()**: Decrements the semaphore if positive; blocks if zero.
- **post()**: Increments the semaphore; wakes up waiting threads.
- **Usage**: Control access to resources and synchronize threads.

**Equivalence of Semaphores, Locks, and Condition Variables**: They can be implemented using each other; choice depends on the specific problem and preference.

**Deadlock**: Occurs when threads are blocked, each waiting for resources held by others.

**Four Necessary Conditions**:

1. **Mutual Exclusion**: Only one thread can use a resource at a time.
2. **Hold and Wait**: Threads hold resources while waiting for others.
3. **No Preemption**: Resources cannot be forcibly taken away.
4. **Circular Wait**: Circular chain of threads each waiting for resources held by the next.

**Breaking Deadlock**: Prevent any of the four conditions.

**Deadlock Prevention Strategies**:

- **Wait-Free Algorithms**: Ensure every operation completes in a finite number of steps, removing the need to wait.
- **Atomic Lock Acquisition**: Require threads to acquire all needed resources atomically.
- **Preemption**: Allow resources to be forcibly taken away.
- **Resource Ordering**: Impose an order on resource acquisition to prevent circular wait.

**Deadlock Avoidance**:

**Banker's Algorithm**: Simulate resource allocation to ensure the system remains in a safe state before actually granting resources.

- **Steps**:
  1. Check if the request is less than or equal to the need.
  2. Check if the request is less than or equal to the available resources.
  3. Temporarily allocate resources and check for a safe state.
  4. If safe, grant the request; otherwise, the thread waits.

**Summary**:

- **Race Conditions**: Solved by protecting critical sections with locks.
- **Locks**: Ensure mutual exclusion; implemented using atomic instructions.
- **Condition Variables**: Coordinate execution order among threads; used with locks.
- **Semaphores**: Control access to resources and synchronize threads.
- **Deadlock**: Prevented by eliminating one of the four necessary conditions or using algorithms like the Banker's Algorithm.

# Short Examples

**Dispatching**: Transfer control of the CPU to a process selected by the scheduler via context switches—save the current process state, load the next process state in kernel mode, then switch to user mode to execute the process.

**Allow Processes to Yield Control**: Can lead to malicious programs monopolizing resources and never yielding.

**Allow OS to Interrupt Running Processes**: Lets other processes take control.

**Process States**: Manage underutilization of the CPU due to slow I/O (blocked) and give control to other processes waiting on the CPU (ready) so they can begin execution (running).

**Scheduling Strategies**:

- **First-In-First-Out (FIFO)**: Executes processes to completion in the order they arrive.

  - **Advantages**: Simple to implement; low overhead; predictable.
  - **Issue**: Short jobs wait for long jobs to finish (convoy problem).

- **Shortest Job First**: Executes the shortest available job next to minimize average waiting time.

  - **Advantages**: Reduces average waiting time.
  - **Issues**:
    - **Timing**: Long jobs may wait indefinitely if short jobs keep arriving.
    - **Knowledge**: Hard to know execution time in advance.

---

By structuring the content in concise paragraphs and single-level bullet points, this cheatsheet aligns with your preferred style and provides a clear, compact overview of concurrency concepts.