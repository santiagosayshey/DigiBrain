
> [!idea] The Idea
> The Master Theorem provides a way to determine the asymptotic behaviour of $T(n)$, which is the time complexity of a divide-and-conquer algorithm.
> $$
> T(n) = aT\left(\frac{n}{b}\right) + f(n)
> $$
> $$
T(n) \in
\begin{cases}
O(n^d) & \text{if } a < b^d \\
O(n^d \log n) & \text{if } a = b^d \\
O(n^{\log_b a}) & \text{if } a > b^d
\end{cases}
> $$

| Solution  | Explanation                                                                                                                                                                                                              |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| $a < b^d$ | If $a < b^d$: The work done at the root of the recursion tree is the most significant. The running time is dominated by the work done outside the recursive calls, $O(n^d)$.                                             |
| $a = b^d$ | If $a = b^d$: The work is evenly distributed across the levels of the recursion tree. The running time is a combination of the work done at each level of the recursion and the depth of the recursion, $O(n^d \log n)$. |
| $a > b^d$ | If $a > b^d$: The work done at the leaves of the recursion tree is the most significant. The running time is dominated by the work done at the deepest level of the recursive calls, $O(n^{\log_b a})$.                  |

| Term   | Meaning                                                                                                                                                                                                                                            |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $T(n)$ | This is the function we are trying to solve for. It represents the total running time of the algorithm.                                                                                                                                            |
| $a$    | This is the number of subproblems in the recursion. If an algorithm splits its input data into smaller pieces to solve the problem, $a$ is the count of those pieces.                                                                              |
| $b$    | This is the factor by which the subproblem size is reduced. If an algorithm splits the problem into subproblems that are half the size of the original, then $b=2$.                                                                                |
| $f(n)$ | This function represents the work done at each level of non-recursive part. It's typically the amount of time it takes to split the problem into subproblems and combine the results of the subproblems.                                           |
| $d$    | This represents the exponent in the running time of the non-recursive part (often called the "combine step" or "work done outside the recursive calls") of an algorithm. If the non-recursive work takes $O(n^d)$ time, then $d$ is that exponent. |
