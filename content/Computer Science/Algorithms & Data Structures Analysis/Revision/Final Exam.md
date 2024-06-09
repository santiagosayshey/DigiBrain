# Asymptotic Analysis
  
| Notation              | Meaning                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------- |
| $f(n) = O(g(n))$      | Highest degree term of $f(n)$ is less than or equal to highest degree term of $g(n)$    |
| $f(n) = \Omega(g(n))$ | Highest degree term of $f(n)$ is greater than or equal to highest degree term of $g(n)$ |
| $f(n) = \Theta(g(n))$ | Highest degree terms of $f(n)$ and $g(n)$ are equal                                     |
| $f(n) = o(g(n))$      | Highest degree term of $f(n)$ is strictly less than highest degree term of $g(n)$       |
| $f(n) = \omega(g(n))$ | Highest degree term of $f(n)$ is strictly greater than highest degree term of $g(n)$    |

# AVL Rotations

| Imbalance Type   | Condition                              | Balance Factor of Node | Balance Factor of Node's Child    | Rotations Needed                                          |
| ---------------- | -------------------------------------- | ---------------------- | --------------------------------- | --------------------------------------------------------- |
| LL (Left-Left)   | Left subtree of left child is deeper   | Balance Factor: +2     | Balance Factor of Left Child: +1  | Single Right Rotation at Node                             |
| RR (Right-Right) | Right subtree of right child is deeper | Balance Factor: -2     | Balance Factor of Right Child: -1 | Single Left Rotation at Node                              |
| LR (Left-Right)  | Right subtree of left child is deeper  | Balance Factor: +2     | Balance Factor of Left Child: -1  | Left Rotation at Left Child, then Right Rotation at Node  |
| RL (Right-Left)  | Left subtree of right child is deeper  | Balance Factor: -2     | Balance Factor of Right Child: +1 | Right Rotation at Right Child, then Left Rotation at Node |
**NOTE:** When performing a x rotation, if a child node has two children, then the x child becomes the child of the root, where x can be left or right. 

# Graph Structures

| Data Structure   | Example                                                                         | Criteria                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Adjacency List   | Tracing ancestors in a family tree spanning several generations                 | - Sparse graphs (relatively few edges compared to the total number of possible edges)<br>- Nodes have varying degrees (different numbers of connections)<br>- Space-efficient for sparse graphs<br>- Efficient for traversals and following connections<br>- Suitable when the number of edges is much smaller than the square of the number of nodes                                                                                                                                                                                                                                                                                                                                 |
| Adjacency Matrix | Storing distances between cities in a densely connected transportation network | - Dense graphs (many edges relative to the number of nodes)<br>- Fixed number of nodes known in advance<br>- Efficient for quickly checking the presence or absence of an edge between two nodes<br>- Constant-time lookup for edge weights or properties<br>- Suitable when the number of edges is close to the square of the number of nodes<br>- Efficient for algorithms that require quick access to edge information, such as shortest path algorithms like Floyd-Warshall                                                                                                                                                                                                   |
| Linked List      | Representing a sparse social network with user profiles as nodes                | - Suitable for sparse graphs with a small number of edges<br>- Allows for dynamic allocation of nodes and edges<br>- Efficient insertion and deletion of nodes and edges<br>- Requires extra space for storing pointers or references<br>- Not efficient for accessing nodes or edges directly (requires traversal)<br>- Suitable when the graph structure frequently changes or when memory usage needs to be minimized                                                                                                                                                                                                                                                              |
| Adjacency Array  | Representing a dense computer network with a fixed number of connected devices  | - Suitable for dense graphs with a known number of nodes<br>- Efficient for accessing edge information between two specific nodes<br>- Requires a fixed amount of memory, allocated upfront<br>- Not efficient for graphs with a large number of nodes but few edges (sparse graphs)<br>- Suitable when the number of nodes is fixed and known in advance, and the graph is dense                                                                                                                                                                                                                                                                                                      |
# Complexity

| Algorithm                         | Description                                                                               | Complexity         | Key                                                                        | Special Considerations               |
| --------------------------------- | ----------------------------------------------------------------------------------------- | ------------------ | -------------------------------------------------------------------------- | ------------------------------------ |
| Standard Multiplication Algorithm | Multiplication algorithm commonly taught in schools                                       | $O(n^2)$           | $n$: number of digits                                                      | -                                    |
| Karatsuba's Algorithm             | Efficient algorithm for multiplying two n-digit numbers                                   | $O(n^{\log_2(3)})$ | $n$: number of digits                                                      | Uses 3 partial products instead of 4 |
| Counting Sort                     | Sorting algorithm that counts the number of objects having distinct key values            | $O(n+k)$           | $n$: number of elements, $k$: range of input values                        | Only works for integer keys          |
| Radix Sort                        | Sorting algorithm that sorts data with integer keys by grouping keys by individual digits | $O(d(n+k))$        | $n$: number of elements, $k$: range of input values, $d$: number of digits | Only works for integer keys          |
| Randomised Selection Algorithm    | Selects the k-th smallest element from an unsorted list                                   | $O(n)$             | $n$: number of elements                                                    | -                                    |
| Deterministic Selection Algorithm | Selects the k-th smallest element from an unsorted list                                   | $O(n)$             | $n$: number of elements                                                    | -                                    |
| Kosaraju's Algorithm              | Finds strongly connected components in a directed graph                                   | $O(V+E)$           | $V$: number of vertices, $E$: number of edges                              | -                                    |
| Dijkstra's Algorithm              | Finds the shortest path from a single source to all other nodes                           | $O((V+E)\log V)$   | $V$: number of vertices, $E$: number of edges                              | Cannot handle negative edge weights  |
| Bellman-Ford Algorithm            | Finds the shortest path from a single source to all other nodes (handles negative edges)  | $O(VE)$            | $V$: number of vertices, $E$: number of edges                              | Can detect negative cycles           |
| Floyd-Warshall Algorithm          | Finds the shortest path between all pairs of nodes                                        | $O(V^3)$           | $V$: number of vertices                                                    | -                                    |
| Kruskal's Algorithm               | Finds a minimum spanning tree in a weighted, connected graph                              | $O(E \log E)$      | $E$: number of edges                                                       | -                                    |
| Prim's Algorithm                  | Finds a minimum spanning tree in a weighted, connected graph                              | $O(E \log V)$      | $V$: number of vertices, $E$: number of edges                              | -                                    |


| Data Structure | Operation | Average Case | Worst Case | Key | Special Considerations |
|----------------|-----------|--------------|------------|-----|------------------------|
| Binary Search Trees | Search | $O(\log n)$ | $O(n)$ | $n$: number of elements | Worst case occurs when tree is unbalanced |
|  | Insertion | $O(\log n)$ | $O(n)$ | $n$: number of elements | Worst case occurs when tree is unbalanced |
|  | Deletion | $O(\log n)$ | $O(n)$ | $n$: number of elements | Worst case occurs when tree is unbalanced |
| AVL Trees | Search | $O(\log n)$ | $O(\log n)$ | $n$: number of elements | Self-balancing property maintains $O(\log n)$ height |
|  | Insertion | $O(\log n)$ | $O(\log n)$ | $n$: number of elements | Self-balancing property maintains $O(\log n)$ height |
|  | Deletion | $O(\log n)$ | $O(\log n)$ | $n$: number of elements | Self-balancing property maintains $O(\log n)$ height |
| Linked Lists | Search | $O(n)$ | $O(n)$ | $n$: number of elements | - |
|  | Insertion | $O(1)$ | $O(1)$ | - | - |
|  | Deletion | $O(1)$ | $O(1)$ | - | - |
| Skip Lists | Search | $O(\log n)$ | $O(n)$ | $n$: number of elements | Probabilistic data structure |
|  | Insertion | $O(\log n)$ | $O(n)$ | $n$: number of elements | Probabilistic data structure |
|  | Deletion | $O(\log n)$ | $O(n)$ | $n$: number of elements | Probabilistic data structure |
| Hash Tables | Search | $O(1)$ | $O(n)$ | $n$: number of elements | Worst case occurs with poor hash function or many collisions |
|  | Insertion | $O(1)$ | $O(n)$ | $n$: number of elements | Worst case occurs with poor hash function or many collisions |
|  | Deletion | $O(1)$ | $O(n)$ | $n$: number of elements | Worst case occurs with poor hash function or many collisions |