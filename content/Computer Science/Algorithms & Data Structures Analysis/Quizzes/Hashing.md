> [!exercise]+ Exercise 1
> 
> What is the primary advantage of using linear probing in hash tables?
>
> A. It eliminates the need for a hash function.
> B. It ensures that no collisions ever occur.
> **C. It provides a systematic method for resolving hash collisions.**
> D. It decreases the storage requirement for the hash table.
> 
> **Explanation:**
> Linear probing is used to find the next available 'spot' in the array to place the key value pair. 

> [!exercise]+ Exercise 2
>
> Which of the following best describes linear probing in a hash table?
>
> A. A method to link all entries with the same hash value into a list.
> B. A technique that places all entries in a binary search tree.
> C. **A strategy to find the next available slot by looking sequentially from the original hash position.**
> D. A method to double the hash table size upon reaching a certain load factor.

> [!exercise]+ Exercise 3
>
> In the context of hash tables, what does a "tombstone" signify when using deletion strategies like linear probing?
>
> A. An entry that has been permanently deleted and cannot be reused.
> B. **A marker that an entry has been deleted, but the slot can be reused.**
> C. A special value indicating the end of the table.
> D. A placeholder for future insertions to maintain hash table integrity.

> [!exercise]+ Exercise 4
>
> Which characteristic is essential for a good hash function in the context of hash tables utilizing linear probing?
>
> A. Determinism
> B. Efficiency in computing the hash value
> C. Uniform distribution of hash values
> **D. All of the above**
> 
> **Explanation:**
> Determinism is necessary to be able to reapply the hash function when searching through the hash table.
> Uniform distribution is necessary to limit collisions. 
> Efficient hash function is necessary to keep constant operations. 

> [!exercise]+ Exercise 5
>
> How does linear probing handle hash collisions?
>
> A. By rehashing the key with a secondary hash function.
> B. By storing all colliding elements in a linked list at the index.
> **C. By sequentially probing the next slots until an empty one is found.**
> D. By immediately resizing the hash table to accommodate more elements.

> [!exercise]+ Exercise 6
>
> What is the primary disadvantage of linear probing?
>
> A. It does not allow for the deletion of keys once they have been inserted.
> B. It requires additional memory overhead to store metadata about the hash table's state.
> **C. It can lead to primary clustering, where contiguous blocks of slots get filled, leading to increased search times.**
> D. It significantly increases the computational overhead of the hash function.
> 
> **Explanation:**
> In a poor hash function, many collisions may occur causing values to be stored in probed slots. This increases search times to the tune of $O(n)

> [!exercise]+ Exercise 7
>
> What is the main issue that linear probing can encounter, affecting the performance of hash tables?
>
> A. Load factor imbalance
> B. Unilateral table size
> C. Primary clustering
> D. High space complexity

> [!exercise]+ Exercise 8
>
> What characteristic a good hash function for hash tables?
>
> A. It should always return the same hash for a given key to ensure consistency.
> B. It should distribute keys uniformly across the hash table to minimize collisions.
> C. It should result in a high number of collisions to fully utilize the hash table's capacity.
> D. It should prioritize certain keys over others to improve search efficiency.

