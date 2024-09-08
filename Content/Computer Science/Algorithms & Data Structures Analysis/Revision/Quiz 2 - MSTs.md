> [!idea]+ Modified Kruskal
>
> **Parsing Input Arrays:** The three input strings represent the `country`, `build`, and `destroy` arrays. To parse them into 2D lists, we split each string on commas to get rows, and convert characters to integers.  
>
> **Create the edge list:**
>  
> - For every possible edge that connects two cities:
>   - If the edge exists (`country[i][j]=1`), add its negative destroy cost to an array:
>     - `edges.append((i, j, -destroy[i][j]))`
>   - If the edge does NOT exist (`country[i][j]=0`), add its positive build cost to an array:
>     - `edges.append((i, j, build[i][j]))`
> - Sort this list
>
> **Generate an MST using Kruskal and Union-Find**
>
> 1. Initialize a Union-Find data structure with the number of cities. 
> 2. Iterate over the sorted edge list (negative costs for destroying, positive for building).
> 3. For each edge `(u, v)`, perform a `union` on `u` and `v` in Union-Find.
>    - If `union` returns True, add the edge to the MST (no cycle formed).
>    - If `union` returns False, skip the edge (would create a cycle).
>
> **The Key Idea in Constructing the MST**
>
> - Because the "bigger" negative costs come first, we add those to the MST and prioritize destroying smaller costs.
> - Then when you reach the positive numbers, the smaller ones come first to prioritize building them over the larger ones.  
>
> **Determine if the cost should be added**
>
> - Iterate over all edges in the country array
> - If an edge is in the MST, and `country[i][j]=0` (it doesnt exist and needs to be built), add its build cost to the total.
> - If an edge is NOT in the MST, and `country[i][j]=1` (it exists and needs to be destroyed), add its destroy cost to the total.

> [!idea]+ Union-Find Data Structure:
>
> - Represents a collection of disjoint sets.
> - Each set is represented by a representative element called the root.  
> - `find(x)` operation returns the root of the set containing element `x`.
> - `union(x, y)` operation merges the sets containing `x` and `y` into a single set.
>
> **find(x):**
> - If `x` is the root of its set, return `x`.
> - Otherwise, recursively set the parent of `x` to the root of its set (path compression).
> - Return the root of the set containing `x`.
>
> **union(x, y):**
> - Find the roots of the sets containing `x` and `y` using `find(x)` and `find(y)`.
> - If the roots are the same, `x` and `y` are already in the same set, so do nothing.  
> - Otherwise, attach the root of the smaller set (by rank) to the root of the larger set.
> - If the ranks are equal, increment the rank of the new root.


# Full Implementation

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1
            return True
        return False

def char_to_int(char):
    if '0' <= char <= '9':
        return ord(char) - ord('0')
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A')
    elif 'a' <= char <= 'z':
        return ord(char) - ord('a') + 26
    return 0

def parse_input(matrix_str):
    rows = matrix_str.split(',')
    return [[char_to_int(char) for char in row] for row in rows]

def process_input(input_data):
    country = parse_input(input_data[0])
    build_cost = parse_input(input_data[1])
    destroy_cost = parse_input(input_data[2])
    return country, build_cost, destroy_cost

def create_edges(country, build, destroy):
    n = len(country)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == 1:
                edges.append((i, j, -destroy[i][j]))
            else:
                edges.append((i, j, build[i][j]))
    return sorted(edges, key=lambda x: x[2])

def calculate_reconstruction_cost(country, build, destroy):
    edges = create_edges(country, build, destroy)
    uf = UnionFind(len(country))
    mst = []

    for u, v, cost in edges:
        if uf.union(u, v):
            mst.append((u, v, cost))

    build_cost = sum(build[u][v] for u, v, cost in mst if country[u][v] == 0)
    destroy_cost = 0
    for i in range(len(country)):
        for j in range(i + 1, len(country)):
            if country[i][j] == 1 and not any(e[0] == i and e[1] == j or e[0] == j and e[1] == i for e in mst):
                destroy_cost += destroy[i][j]
    
    return build_cost + destroy_cost

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    country, build, destroy = process_input(input_data)
    result = calculate_reconstruction_cost(country, build, destroy)
    print(result)

if __name__ == "__main__":
    main()
```