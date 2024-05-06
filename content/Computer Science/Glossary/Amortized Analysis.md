> [!idea] Amortized Analysis
>
> Amortized analysis is a method used to **analyse the time complexity of algorithms involving a sequence of operations**.
>
> Key points to remember:
> - Amortized analysis provides the average cost per operation over a worst-case sequence of operations.
> - It "spreads out" the cost of expensive operations over the entire sequence.
> - The total cost of a sequence is analyzed, and the average cost per operation is calculated.
> - Techniques used in amortized analysis include:
>   - Aggregate method
>   - Accounting method
>   - Potential method
> - Amortized analysis is useful for data structures with operations that have varying costs.
> - It provides a more accurate and practical analysis of time complexity compared to worst-case analysis of individual operations.

> [!example] Dynamic Array (Vector) Resizing
>
> Consider a dynamic array data structure, such as a vector in C++, which allows elements to be inserted and removed efficiently. When the array reaches its capacity, it needs to be resized to accommodate more elements.
>
> Let's say we start with an empty vector and perform a sequence of insertions:
>
> - Insert 1: [1] (capacity: 1)
> - Insert 2: [1, 2] (capacity: 2)
> - Insert 3: [1, 2, 3] (capacity: 4)
> - Insert 4: [1, 2, 3, 4] (capacity: 4)
> - Insert 5: [1, 2, 3, 4, 5] (capacity: 8)
>
> In this example, the vector doubles its capacity whenever it becomes full. Resizing the vector is an expensive operation because it involves allocating a new larger array and copying all the elements from the old array to the new one.
>
> If we analyze the worst-case time complexity of each individual insertion, it would be O(n) for the resizing operation, where n is the current size of the vector.
>
> However, using amortized analysis, we can show that the average cost per insertion is actually O(1) over a sequence of insertions.
>
> The key observation is that the resizing operation, which takes O(n) time, happens only after a sequence of insertions that double the vector's size. All the other insertions in between take O(1) time.
>
> Using the aggregate method of amortized analysis, we can sum up the total cost of a sequence of n insertions:
> - Cost of resizing: O(1) + O(2) + O(4) + ... + O(n) = O(n)
> - Cost of individual insertions: n * O(1) = O(n)
>
> The total cost of n insertions is O(n), and when divided by the number of insertions (n), we get an amortized cost of O(1) per insertion.
>
> Amortized analysis reveals that, although individual insertions can be expensive when resizing occurs, the average cost per insertion over a sequence of insertions is actually constant, making dynamic arrays an efficient data structure for many scenarios.

