# Asymptotic Analysis
  
| Notation              | Meaning                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------- |
| $f(n) = O(g(n))$      | Highest degree term of $f(n)$ is less than or equal to highest degree term of $g(n)$    |
| $f(n) = \Omega(g(n))$ | Highest degree term of $f(n)$ is greater than or equal to highest degree term of $g(n)$ |
| $f(n) = \Theta(g(n))$ | Highest degree terms of $f(n)$ and $g(n)$ are equal                                     |
| $f(n) = o(g(n))$      | Highest degree term of $f(n)$ is strictly less than highest degree term of $g(n)$       |
| $f(n) = \omega(g(n))$ | Highest degree term of $f(n)$ is strictly greater than highest degree term of $g(n)$    |
# Multiplication

> [!idea] School Method Multiplication
> - Multiplies two n-digit integers using $O(n^2)$ primitive operations
> - Results in at most a $2n$-digit integer
>
> | Method | Time Complexity | Max Result Digits |
> |--------|----------------|-------------------|
> | School | $O(n^2)$       | $2n$              |

> [!idea] Recursive Multiplication
> - Splits integers into smaller parts and recursively multiplies them
> - Combines partial products to obtain the final result
> - Recurrence relation:
>   $T(n) \leq \begin{cases} 
>   1 & \text{if } n = 1 \\
>   4 \cdot T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + 3 \cdot 2^n & \text{if } n \geq 2 
>   \end{cases}$
> - Time complexity: $O(n^2)$ (worse than school method)

```
![[Pasted image 20240305013909.png]]
```

> [!idea] Karatsuba Algorithm
> - Divide and conquer approach with only 3 partial products
> - Recurrence relation:
>   $T_K(n) \leq
>   \begin{cases}
>   3n^2 + 2n & \text{if } n < 4 \\
>   3 \cdot T_K\left(\left\lceil \frac{n}{2} \right\rceil + 1\right) + 6 \cdot 2 \cdot n & \text{if } n \geq 4
>   \end{cases}$
> - Time complexity: $O(n^{\log_2 3}) \approx O(n^{1.59})$

> [!consider] Karatsuba vs Recursive Multiplication
> - Karatsuba reaches leaf nodes more quickly than recursive multiplication
> - Shallower tree structure with fewer levels in Karatsuba
>
> ```
> ![[Pasted image 20240311053326.png]]
> ![[Pasted image 20240311060156.png]]
> ```
# AVL Rotations

| Imbalance Type   | Condition                              | Balance Factor of Node | Balance Factor of Node's Child    | Rotations Needed                                          |
| ---------------- | -------------------------------------- | ---------------------- | --------------------------------- | --------------------------------------------------------- |
| LL (Left-Left)   | Left subtree of left child is deeper   | Balance Factor: +2     | Balance Factor of Left Child: +1  | Single Right Rotation at Node                             |
| RR (Right-Right) | Right subtree of right child is deeper | Balance Factor: -2     | Balance Factor of Right Child: -1 | Single Left Rotation at Node                              |
| LR (Left-Right)  | Right subtree of left child is deeper  | Balance Factor: +2     | Balance Factor of Left Child: -1  | Left Rotation at Left Child, then Right Rotation at Node  |
| RL (Right-Left)  | Left subtree of right child is deeper  | Balance Factor: -2     | Balance Factor of Right Child: +1 | Right Rotation at Right Child, then Left Rotation at Node |
**NOTE:** When performing a x rotation, if a child node has two children, then the x child becomes the child of the root, where x can be left or right. 
You're right. The examples provided for the Linked List and Adjacency Array are not specific examples but rather general descriptions of their suitable use cases. Let me provide more concrete examples for those two:

| Data Structure   | Example                                                                         | Criteria                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Adjacency List   | Tracing ancestors in a family tree spanning several generations                 | - Sparse graphs (relatively few edges compared to the total number of possible edges)<br>- Nodes have varying degrees (different numbers of connections)<br>- Space-efficient for sparse graphs<br>- Efficient for traversals and following connections<br>- Suitable when the number of edges is much smaller than the square of the number of nodes                                                                                                                                                                                                                                                                                                                                 |
| Adjacency Matrix | Storing distances between cities in a densely connected transportation network | - Dense graphs (many edges relative to the number of nodes)<br>- Fixed number of nodes known in advance<br>- Efficient for quickly checking the presence or absence of an edge between two nodes<br>- Constant-time lookup for edge weights or properties<br>- Suitable when the number of edges is close to the square of the number of nodes<br>- Efficient for algorithms that require quick access to edge information, such as shortest path algorithms like Floyd-Warshall                                                                                                                                                                                                   |
| Linked List      | Representing a sparse social network with user profiles as nodes                | - Suitable for sparse graphs with a small number of edges<br>- Allows for dynamic allocation of nodes and edges<br>- Efficient insertion and deletion of nodes and edges<br>- Requires extra space for storing pointers or references<br>- Not efficient for accessing nodes or edges directly (requires traversal)<br>- Suitable when the graph structure frequently changes or when memory usage needs to be minimized                                                                                                                                                                                                                                                              |
| Adjacency Array  | Representing a dense computer network with a fixed number of connected devices  | - Suitable for dense graphs with a known number of nodes<br>- Efficient for accessing edge information between two specific nodes<br>- Requires a fixed amount of memory, allocated upfront<br>- Not efficient for graphs with a large number of nodes but few edges (sparse graphs)<br>- Suitable when the number of nodes is fixed and known in advance, and the graph is dense                                                                                                                                                                                                                                                                                                      |
