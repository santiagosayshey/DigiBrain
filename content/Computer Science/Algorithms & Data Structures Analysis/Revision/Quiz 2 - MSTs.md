**Parsing Input Arrays:** The three input strings represent the `country`, `build`, and `destroy` arrays. To parse them into 2D lists, we split each string on commas to get rows, and convert characters to integers.

**Create the edge list:**
- For every possible edge that connects two cities:
	- If the edge exists (`country[i][h]=1`), add its negative destroy cost to an array: 
		- `edges.append((i, j, -destroy[i][j]))`
	- If the edge does NOT exist (`country[i][h]=0`) add its positive build cost to an array
		- `edges.append((i, j, build[i][j]))`
- Sort this list

**Generate an MST using Kruskal and Union-Find**
1. Initialize a Union-Find data structure with the number of cities.
2. Iterate over the sorted edge list (negative costs for destroying, positive for building).
3. For each edge `(u, v)`, perform a `union` on `u` and `v` in Union-Find.
	- If `union` returns True, add the edge to the MST (no cycle formed).
	- If `union` returns False, skip the edge (would create a cycle).

**The Key Idea in Constructing the MST**
- Because the "bigger" negative costs come first, we add those to MST and prioritise destroying smaller costs. 
- Then when you reach the positive numbers, the smaller ones come first to prioritise building them over the larger ones

**Determine if the cost should be added**
- Iterate over all edges in the country array
	- If an edge is in the MST, and `country[i][j] = 0` (it doesnt exist and needs to be built), add its build cost to the total
	- If an edge is NOT in the mst, and `country[i][j] = 1` (it exists and needs to be destroyed), add its destroy cost to the total




**Union-Find Data Structure:**

- Represents a collection of disjoint sets.
- Each set is represented by a representative element called the root.
- `find(x)` operation returns the root of the set containing element `x`.
- `union(x, y)` operation merges the sets containing `x` and `y` into a single set.

**find(x):**
- If `x` is the root of its set, return `x`.
- Otherwise, recursively set the parent of `x` to the root of its set (path compression).
- Return the root of the set containing `x`.

**union(x, y):**
- Find the roots of the sets containing `x` and `y` using `find(x)` and `find(y)`.
- If the roots are the same, `x` and `y` are already in the same set, so do nothing.
- Otherwise, attach the root of the smaller set (by rank) to the root of the larger set.
- If the ranks are equal, increment the rank of the new root.

By using path compression in `find` and union by rank in `union`, the amortized time complexity of both operations is O(α(n)), where α(n) is the inverse Ackermann function, which is practically a small constant for most practical values of n.

This efficient implementation of the Union-Find data structure allows Kruskal's algorithm to detect and avoid cycles in the MST construction efficiently.