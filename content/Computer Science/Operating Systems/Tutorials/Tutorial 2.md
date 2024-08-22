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
> 

> [!exercise] Question 4: Improving CPU Utilization
> Consider a demand-paging system with the following time-measured utilizations:
> CPU utilization 20%
> Paging disk 97.7%
> Other I/O devices 5%
> 
> Which (if any) of the following will (probably) improve CPU utilization? Explain your answer.
> a. Install a faster CPU.
> b. Install a bigger paging disk.
> c. Increase the degree of multiprogramming.
> d. Decrease the degree of multiprogramming.
> e. Install more main memory.
> f. Install a faster hard disk, or multiple controllers with multiple hard disks.
> g. Add pre-paging to the page fetch algorithms.
> h. Increase the page size.
> 
> Answer:
> 
> 
