> [!exercise] Question 1
> What is the primary goal of a Minimum Spanning Tree (MST) in a graph?
>
> 1. To find the shortest path between two specific vertices.
> **2. To create a subset of the graph that connects all vertices with the minimum total edge weight.**
> 3. To detect cycles within the graph.
> 4. To maximise the distance between any two vertices in the graph.
>
> **Explanation:**
> A minimum spanning tree minimises the edges in a graph such that all nodes are still connected.

> [!exercise] Question 2  
> What is the main difference between Prim's and Kruskal's algorithms?
>
> 1. Prim's algorithm works on directed graphs, while Kruskal's works on undirected graphs.
> **2. Prim's algorithm builds the MST by adding edges, while Kruskal's algorithm starts with vertices**.
> 3. Prim's algorithm is a greedy algorithm, while Kruskal's is not.
> 4. Prim's algorithm grows a single MST, while Kruskal's algorithm may grow multiple trees before connecting them.
>
> **Explanation:** The key difference between Prim's and Kruskal's algorithms lies in their approach to constructing the Minimum Spanning Tree (MST). Prim's algorithm starts with an arbitrary vertex and incrementally adds the smallest weighted edge connecting a vertex in the growing MST to a vertex outside the MST. In contrast, Kruskal's algorithm starts by sorting all edges in ascending order of their weights and then iteratively adds the smallest edge that doesn't form a cycle with the edges already included in the MST.**

> [!exercise] Question 3
> Which algorithm is typically used for finding a Minimum Spanning Tree in a graph with weighted edges?
>
> 1. Breadth-First Search (BFS)
> 2. Depth-First Search (DFS)  
> **3. Kruskal's Algorithm**
> 4. Bellman-Ford Algorithm
>
> **Explanation:** The rest of the algorithms either visit all nodes, or find the shortest paths. 

> [!exercise] Question 4
> What is the main characteristic of edges in a Minimum Spanning Tree of a graph?
>
> 1. All edges have the same weight.
> 2. The sum of the weights of the edges is maximised.
> **3. The sum of the weights of the edges is minimised.**
> 4. Each edge connects vertices of the same degree.
>
> **Explanation:** If you add up all the edges in an MST, it will be the sma

> [!exercise] Question 5
> Which of the following statements about the Minimum Spanning Tree (MST) is TRUE?
>
> 1. An MST of a graph can include cycles to ensure minimal edge weights.
> 2. An MST is only possible if the graph is fully connected without any isolated vertices.
> 3. The MST of a graph guarantees the shortest path between any two vertices in the graph.
> 4. A graph can have more than one MST if multiple edges have the same weight.
>
> **Explanation:**