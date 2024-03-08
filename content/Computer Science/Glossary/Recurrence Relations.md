> [!idea] Recurrence Relations
> Recurrence relations are mathematical formulas that describe the complexity of divide and conquer algorithms by expressing how the algorithm performs on smaller subsets of the problem. They offer a structured way to analyse and predict the performance of algorithms as the size of input data changes. 
> 
> This is particularly useful for understanding algorithms that break down a problem into smaller parts, solve these parts, and then combine the solutions to solve the original problem.

> [!exercise] Example: Binary Search Algorithm
> Consider the binary search algorithm, which looks for an item in a sorted array by repeatedly dividing the search interval in half. 
> - The time complexity of binary search for an array of \(n\) elements can be represented by the recurrence relation $T(n) = T(n/2) + O(1)$. This equation indicates that the time to search $n$ elements is equal to the time to search $n/2$ elements plus a constant time for the division and comparison operations.



> [!idea]+ Solving Recurrence Relations
> There are many ways, but the main way is to use the [[2.3 Master Theorem|Master Theorem]]

When we combine subproblems, we have to consider the work taken to combine the results of the subproblems. This is usually a constant in the non base case. 