
> [!idea] Recurrence Relations
> 
> Recurrence relations are mathematical equations that describe the running time or space complexity of recursive algorithms by expressing the performance of the algorithm in terms of its input size. They offer a structured way to analyze and predict the efficiency of recursive algorithms as the size of the input data changes.
> 
> Recurrence relations are useful for understanding and analyzing various types of recursive algorithms, including those that break down a problem into smaller subproblems, solve these subproblems recursively, and then combine the solutions to solve the original problem (e.g., divide and conquer algorithms). They are also applicable to other recursive paradigms such as decrease and conquer, dynamic programming, and backtracking.


> [!exercise] Example: Binary Search Algorithm
> Consider the binary search algorithm, which looks for an item in a sorted array by repeatedly dividing the search interval in half. 
> - The time complexity of binary search for an array of \(n\) elements can be represented by the recurrence relation $T(n) = T(n/2) + O(1)$. This equation indicates that the time to search $n$ elements is equal to the time to search $n/2$ elements plus a constant time for the division and comparison operations.



> [!idea]+ Solving Recurrence Relations
> There are many ways, but the main way is to use the [[2.3 Master Theorem|Master Theorem]]

When we combine subproblems, we have to consider the work taken to combine the results of the subproblems. This is usually a constant in the non base case. 