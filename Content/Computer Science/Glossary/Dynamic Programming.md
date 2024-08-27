
> [!idea] Dynamic Programming
>
> Dynamic Programming (DP) is an algorithmic technique that **solves complex problems by breaking them down into simpler subproblems** and **storing the solutions** to these subproblems to avoid redundant calculations.
>
> The key characteristics of problems that can be solved using Dynamic Programming are:
> 1. **Optimal Substructure:** The optimal solution to the overall problem can be constructed from the optimal solutions to its subproblems.
> 2. **Overlapping Subproblems:** The problem can be broken down into subproblems that are reused multiple times during the computation.
>
> Dynamic Programming is commonly used in optimization problems, where the goal is to find the best solution among all possible solutions. It is particularly useful when the problem exhibits optimal substructure and overlapping subproblems, as it can significantly reduce the time complexity compared to brute-force or recursive approaches.

> [!consider] Real-Life Example: Navigation Apps
> 
> Consider a navigation app like Google Maps that helps you find the shortest route from your current location to a destination. The app could **calculate all possible routes and compare them to find the shortest one, but that would be inefficient**, especially for long distances with many possible paths.
>
> Instead, navigation apps use techniques similar to Dynamic Programming. They break down the problem into smaller subproblems, like **finding the shortest path to intermediate landmarks or junctions. By storing and reusing** these subproblem solutions, the app can efficiently construct the overall shortest path without redundantly calculating the same subpaths multiple times.
