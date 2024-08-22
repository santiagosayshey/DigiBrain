> [!exercise] Question 1: Paging Fragmentation
> How much fragmentation occurs with paging? Which type?
> 
> **Answer:**
> 
> Paging experiences only **internal fragmentation**. The amount is typically small:
> 
> - Each page may have some unused space at the end
> - Maximum wasted space per page is (page size - 1) bytes
> - On average, half a page is wasted per process
> 
> Definitions:
> - **Internal fragmentation**: Unused space within an allocated memory block
> - **External fragmentation**: Unused space between allocated memory blocks
> 
> Paging eliminates external fragmentation by design, as it uses fixed-size pages and frames. This allows for efficient memory allocation without creating gaps between allocated memory regions.

> [!exercise] Question 2: Virtual to Physical Address Translation
> A certain computer provides its user with $2^{32}$ bytes of virtual memory and $2^{22}$ bytes of physical memory. The page size is 4,096 bytes. A process requests a read of address 11123456. Explain how the system establishes the corresponding physical location, distinguishing between software and hardware operations.
> 
> **Answer:**
> 
> 1. **Address Breakdown**:
>    - Virtual memory size: $2^{32}$ = 4,294,967,296 bytes
>    - Physical memory size: $2^{22}$ = 4,194,304 bytes
>    - Page size: 4,096 bytes
>    - Virtual address: 11,123,456
> 
> 2. **Page Number and Offset Calculation**:
>    - Page number = Virtual address / Page size = 11,123,456 / 4,096 = 2,715 (integer division)
>    - Offset = Virtual address % Page size = 11,123,456 % 4,096 = 2,720
> 
> 3. **Software Operations**:
>    - The OS maintains the page table
>    - It checks if page 2,715 is in memory (valid bit)
>    - If not in memory, it handles the page fault
> 
> 4. **Hardware Operations**:
>    - The MMU uses page number 2,715 to index the page table
>    - It retrieves the corresponding frame number (let's assume it's 1,234)
>    - Combines frame number with offset to form physical address
> 
> 5. **Physical Address Formation**:
>    - Frame number: 1,234
>    - Physical address = (Frame number * Page size) + Offset
>    - Physical address = (1,234 * 4,096) + 2,720 = 5,057,024
> 
> The process involves both software (OS managing page tables and handling page faults) and hardware (MMU performing the actual translation) components working together to translate the virtual address 11,123,456 to the physical address 5,057,024.

> [!exercise] Question 3: Page Replacement Algorithms
> Consider the following page reference string:
> 1, 2, 3, 4, 2, 1, 5, 6, 2, 1, 2, 3, 7, 6, 3, 2, 1, 2, 3, 6.
> 
> How many page faults would occur for the following replacement algorithms, assuming we have only three memory frames? How many if we increase the memory to 5 frames?
> • LRU replacement
> • FIFO replacement
> • Optimal replacement
> 
> Remember all frames are initially empty so your first unique pages will all cost one fault each.
> 
> Answer:
> 
> 1. LRU (Least Recently Used):
>    Process: Keep track of when each page was last used. When a page fault occurs and all frames are full, replace the page that hasn't been used for the longest time.
> 
>    - 3 frames: 15 faults
>      - Pages 1, 2, 3 fill empty frames.
>      - Page 4 replaces 1 (least recently used).
>      - Continue replacing least recently used page when a fault occurs.
> 
>    - 5 frames: 10 faults
>      - Pages 1, 2, 3, 4, 5 fill empty frames.
>      - Page 6 replaces 1, then 7 replaces 2.
>      - Fewer replacements due to more available frames.
> 
> 2. FIFO (First-In-First-Out):
>    Process: Maintain a queue of pages. When a page fault occurs and all frames are full, replace the page that has been in memory the longest (front of the queue).
> 
>    - 3 frames: 15 faults
>      - Pages 1, 2, 3 fill empty frames.
>      - Page 4 replaces 1 (first in).
>      - Continue replacing oldest page in memory.
> 
>    - 5 frames: 10 faults
>      - Pages 1, 2, 3, 4, 5 fill empty frames.
>      - Page 6 replaces 1, then 7 replaces 2.
>      - Performs identically to LRU for this sequence.
> 
> 3. Optimal:
>    Process: When a page fault occurs and all frames are full, look ahead in the reference string and replace the page that won't be used for the longest time in the future.
> 
>    - 3 frames: 11 faults
>      - Pages 1, 2, 3 fill empty frames.
>      - For page 4, replace 3 as it won't be used for the longest time.
>      - Continue replacing page not used for longest future time.
> 
>    - 5 frames: 8 faults
>      - Pages 1, 2, 3, 4, 5 fill empty frames.
>      - 6 and 7 cause faults, filling all frames.
>      - Only page 3 causes another fault after this.
> 
> The Optimal algorithm performs best due to its future knowledge, but it's not implementable in real systems. LRU and FIFO are more practical but may perform differently depending on the specific page reference pattern.

> [!exercise] Question 4: Improving CPU Utilization
> Consider a demand-paging system with the following time-measured utilizations:
> CPU utilization 20%
> Paging disk 97.7%
> Other I/O devices 5%
> 
> Which (if any) of the following will (probably) improve CPU utilization? Explain your answer.
> 
> Answer:
> 
> a. Install a faster CPU:
>    - Unlikely to improve CPU utilization
>    - The current CPU is idle 80% of the time, so increasing its speed won't help
>    - The bottleneck appears to be in the paging system, not CPU speed
> 
> b. Install a bigger paging disk:
>    - Unlikely to improve CPU utilization
>    - The issue is the speed of paging, not the capacity of the paging disk
>    - A larger disk doesn't necessarily mean faster paging operations
> 
> c. Increase the degree of multiprogramming:
>    - Unlikely to improve CPU utilization
>    - With the paging disk already at 97.7% utilization, increasing multiprogramming would likely worsen the paging bottleneck
>    - This could lead to thrashing, further reducing CPU utilization
> 
> d. Decrease the degree of multiprogramming:
>    - Might improve CPU utilization
>    - Reducing the number of concurrent programs could decrease paging disk load
>    - This might allow the CPU to spend more time processing and less time waiting for pages
> 
> e. Install more main memory:
>    - Likely to improve CPU utilization
>    - More memory means fewer page faults and less paging disk activity
>    - This directly addresses the high paging disk utilization
> 
> f. Install a faster hard disk, or multiple controllers with multiple hard disks:
>    - Likely to improve CPU utilization
>    - This would speed up paging operations, reducing the time the CPU spends waiting for pages
>    - Directly addresses the bottleneck in the paging system
> 
> g. Add pre-paging to the page fetch algorithms:
>    - Might improve CPU utilization
>    - Could reduce the number of page faults by predicting and loading pages before they're needed
>    - However, effectiveness depends on the accuracy of prediction and could potentially increase unnecessary disk activity
> 
> h. Increase the page size:
>    - Might improve CPU utilization, but effects are complex
>    - Larger pages could reduce the number of page faults for programs with high spatial locality
>    - However, it could increase the time for each individual page fault and potentially waste memory for programs with poor locality
> 
> In conclusion, the most effective solutions are likely to be those that directly address the paging bottleneck: installing more main memory (e) or a faster/multiple paging disks (f). These solutions target the root cause of the low CPU utilization, which is the excessive time spent waiting for paging operations.
