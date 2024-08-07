> [!example] Question 1
> **(a)** What is the difference between kernel mode and user mode? Why is the difference important to an OS?
>
> **Answer:**
> 
> OSes have two distinct modes that define the usage of privileged actions. Kernel mode is reserved for the OS's kernel, and essentially allows complete control over everything. Everything else runs in user mode, and must defer to the kernel in order to complete a privileged action. This is done primarily through system calls. It is almost analogous to a child asking for their parent's hand when crossing the road. 
> 
> The separation of these two modes is important, because user programs must be limited in their ability to affect critical system controls or control hardware. They have the opportunity to monopolise resources, lock other programs out or control hardware. 
>
> **(b)** Which of the following instructions should be allowed only in kernel mode
> 
> 1- disable all interrupts
> 2- read the time-of-day clock
> 3- set the time-of-day clock
> 4- change the memory map
>
> **Answer:**
> Disable all interrupts - Kernel mode. If a user program could disable all interrupts, they can essentially monopolise the OS.
> Read the time of day - User mode. Read operations should be available to all user programs for basic things like time of day. If we wanted to read more sensitive data like user passwords, then we would want to defer to kernel mode.
> Set the time of day - Kernel mode. Obvious really. The OS should have control over a resource that affects all programs.
> Change the memory map - Kernel mode. Another obvious one. Being able to change the layout of memory should be reserved for the kernel. It has the ability to cause catastrophic issues for the computer if a user could control it. Overwriting, losing important data, leaking it, etc.

> [!example] Question 2
> (a) What is the main difference between a process and a thread?
>
> **Answer:**
> 
> Programs are a consecutive sequence of instructions that tell a computer to do something. A process is a program in execution. Each process has it's own unique subset of unique memory space, meaning instructions belonging to the same process share the same memory.
> 
  A thread is a subset of a process, where each thread executes its own unique set of instructions, but uses the same subset of memory that every other thread in a process uses.
> 
> 
>
> (b) In a system with threads, is there normally one stack per thread or one stack per process? Explain
>
> **Answer:**

> [!example] Question 3
> Draw a diagram that illustrate the transitions of a process state for
> a) a non pre-emptive scheduler
> b) a pre-emptive scheduler
>
> **Answer:**
>
> Give two reasons to support pre-emption.
>
> **Answer:**

> [!example] Question 4
> The table below describes the CPU-I/O Burst cycles for processes P1, P2 and P3. Assume 0 is the highest priority.
>
> [Table from the image]
>
> (a) Draw the Gantt chart timeline, illustrating the interleaving of processes, and calculate the average waiting time for each process under
> 1. a non pre-emptive priority scheduling algorithm
> 2. a round robin scheduling algorithm with quantum = 6.
>
> **Answer:**
