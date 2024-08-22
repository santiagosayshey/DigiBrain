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
> 3. Next?
>   - Find frame that corresponds to page 2715. 
>   - Find physical memory location 

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

# LRU 

For 3 frames:

| Page Reference | Frames | Page Fault? | Frame Replaced (if any) |
|----------------|--------|-------------|-------------------------|
| 1 | [1] | Yes | - |
| 2 | [1,2] | Yes | - |
| 3 | [1,2,3] | Yes | - |
| 4 | [2,3,4] | Yes | 1 |
| 2 | [3,4,2] | No | - |
| 1 | [4,2,1] | Yes | 3 |
| 5 | [2,1,5] | Yes | 4 |
| 6 | [1,5,6] | Yes | 2 |
| 2 | [5,6,2] | Yes | 1 |
| 1 | [6,2,1] | Yes | 5 |
| 2 | [6,2,1] | No | - |
| 3 | [2,1,3] | Yes | 6 |
| 7 | [1,3,7] | Yes | 2 |
| 6 | [3,7,6] | Yes | 1 |
| 3 | [7,6,3] | No | - |
| 2 | [6,3,2] | Yes | 7 |
| 1 | [3,2,1] | Yes | 6 |
| 2 | [3,2,1] | No | - |
| 3 | [3,2,1] | No | - |
| 6 | [2,1,6] | Yes | 3 |

In the 3-frame scenario, there are 15 page faults.

| Page Reference | Frames | Page Fault? | Frame Replaced (if any) |
|----------------|--------|-------------|-------------------------|
| 1 | [1] | Yes | - |
| 2 | [1,2] | Yes | - |
| 3 | [1,2,3] | Yes | - |
| 4 | [1,2,3,4] | Yes | - |
| 2 | [1,2,3,4] | No | - |
| 1 | [1,2,3,4] | No | - |
| 5 | [1,2,3,4,5] | Yes | - |
| 6 | [2,3,4,5,6] | Yes | 1 |
| 2 | [2,3,4,5,6] | No | - |
| 1 | [3,4,5,6,1] | Yes | 2 |
| 2 | [4,5,6,1,2] | Yes | 3 |
| 3 | [5,6,1,2,3] | Yes | 4 |
| 7 | [6,1,2,3,7] | Yes | 5 |
| 6 | [6,1,2,3,7] | No | - |
| 3 | [6,1,2,3,7] | No | - |
| 2 | [6,1,2,3,7] | No | - |
| 1 | [6,1,2,3,7] | No | - |
| 2 | [6,1,2,3,7] | No | - |
| 3 | [6,1,2,3,7] | No | - |
| 6 | [6,1,2,3,7] | No | - |

In the 5-frame scenario, there are 10 page faults.

# FIFO

For 3 frames:

| Page Reference | Frames | Page Fault? | Frame Replaced (if any) |
|----------------|--------|-------------|-------------------------|
| 1 | [1] | Yes | - |
| 2 | [1,2] | Yes | - |
| 3 | [1,2,3] | Yes | - |
| 4 | [4,2,3] | Yes | 1 |
| 2 | [4,2,3] | No | - |
| 1 | [1,2,3] | Yes | 4 |
| 5 | [1,5,3] | Yes | 2 |
| 6 | [1,5,6] | Yes | 3 |
| 2 | [2,5,6] | Yes | 1 |
| 1 | [2,1,6] | Yes | 5 |
| 2 | [2,1,6] | No | - |
| 3 | [3,1,6] | Yes | 2 |
| 7 | [3,7,6] | Yes | 1 |
| 6 | [3,7,6] | No | - |
| 3 | [3,7,6] | No | - |
| 2 | [2,7,6] | Yes | 3 |
| 1 | [2,1,6] | Yes | 7 |
| 2 | [2,1,6] | No | - |
| 3 | [3,1,6] | Yes | 2 |
| 6 | [3,1,6] | No | - |

In the 3-frame scenario, there are 15 page faults.

For 5 frames:

| Page Reference | Frames | Page Fault? | Frame Replaced (if any) |
|----------------|--------|-------------|-------------------------|
| 1 | [1] | Yes | - |
| 2 | [1,2] | Yes | - |
| 3 | [1,2,3] | Yes | - |
| 4 | [1,2,3,4] | Yes | - |
| 2 | [1,2,3,4] | No | - |
| 1 | [1,2,3,4] | No | - |
| 5 | [1,2,3,4,5] | Yes | - |
| 6 | [6,2,3,4,5] | Yes | 1 |
| 2 | [6,2,3,4,5] | No | - |
| 1 | [6,1,3,4,5] | Yes | 2 |
| 2 | [6,1,2,4,5] | Yes | 3 |
| 3 | [6,1,2,3,5] | Yes | 4 |
| 7 | [7,1,2,3,5] | Yes | 6 |
| 6 | [7,6,2,3,5] | Yes | 1 |
| 3 | [7,6,2,3,5] | No | - |
| 2 | [7,6,2,3,5] | No | - |
| 1 | [7,6,1,3,5] | Yes | 2 |
| 2 | [7,6,1,2,5] | Yes | 3 |
| 3 | [3,6,1,2,5] | Yes | 7 |
| 6 | [3,6,1,2,5] | No | - |
In the 5-frame scenario, there are 13 page faults.

# Optimal ( Like a Stack)

For 3 frames:

| Page Reference | Frames | Page Fault? | Frame Replaced (if any) |
|----------------|--------|-------------|-------------------------|
| 1 | [1] | Yes | - |
| 2 | [1,2] | Yes | - |
| 3 | [1,2,3] | Yes | - |
| 4 | [1,2,4] | Yes | 3 |
| 2 | [1,2,4] | No | - |
| 1 | [1,2,4] | No | - |
| 5 | [1,2,5] | Yes | 4 |
| 6 | [1,2,6] | Yes | 5 |
| 2 | [1,2,6] | No | - |
| 1 | [1,2,6] | No | - |
| 2 | [1,2,6] | No | - |
| 3 | [1,2,3] | Yes | 6 |
| 7 | [1,2,7] | Yes | 3 |
| 6 | [1,2,6] | Yes | 7 |
| 3 | [1,2,3] | Yes | 6 |
| 2 | [1,2,3] | No | - |
| 1 | [1,2,3] | No | - |
| 2 | [1,2,3] | No | - |
| 3 | [1,2,3] | No | - |
| 6 | [1,2,6] | Yes | 3 |
In the 3-frame scenario, there are 11 page faults.

For 5 frames:

| Page Reference | Frames | Page Fault? | Frame Replaced (if any) |
|----------------|--------|-------------|-------------------------|
| 1 | [1] | Yes | - |
| 2 | [1,2] | Yes | - |
| 3 | [1,2,3] | Yes | - |
| 4 | [1,2,3,4] | Yes | - |
| 2 | [1,2,3,4] | No | - |
| 1 | [1,2,3,4] | No | - |
| 5 | [1,2,3,4,5] | Yes | - |
| 6 | [1,2,3,5,6] | Yes | 4 |
| 2 | [1,2,3,5,6] | No | - |
| 1 | [1,2,3,5,6] | No | - |
| 2 | [1,2,3,5,6] | No | - |
| 3 | [1,2,3,5,6] | No | - |
| 7 | [1,2,3,6,7] | Yes | 5 |
| 6 | [1,2,3,6,7] | No | - |
| 3 | [1,2,3,6,7] | No | - |
| 2 | [1,2,3,6,7] | No | - |
| 1 | [1,2,3,6,7] | No | - |
| 2 | [1,2,3,6,7] | No | - |
| 3 | [1,2,3,6,7] | No | - |
| 6 | [1,2,3,6,7] | No | - |
In the 5-frame scenario, there are 8 page faults.

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
>    - CPU utilisation is only at 20%, so installing a faster CPU will only drop this number even further. The issue is that the CPU is already processing things faster than the paging disk can give tasks to the CPU. 
> 
> b. Install a bigger paging disk:
> - This will only increase the number of pages in the disk, not its processing speed. Processing page speed is increases, then CPU utilisation increases. 
> 
> c. Increase the degree of multiprogramming:
>    - Does this mean concurrent processing? This still probably won’t increase CPU utilisation because we are still bottlenecked by the speed at which the paging disk can process. 
> 
> d. Decrease the degree of multiprogramming:
>    - Might improve cpu utilisation. If you decrease the number of concurrent threads, then the CPU is only able to process x amount of things at once. 
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
