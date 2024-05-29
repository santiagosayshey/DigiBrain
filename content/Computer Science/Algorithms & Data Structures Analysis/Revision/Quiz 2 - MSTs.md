**Parsing Input Arrays:** The three input strings represent the `country`, `build`, and `destroy` arrays. To parse them into 2D lists, we split each string on commas to get rows, and convert characters to integers.

**Using Union-Find with Kruskal's:**



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
4. If `union` returns True, add the edge to the MST (no cycle formed).
5. If `union` returns False, skip the edge (would create a cycle).

Generate an MST using Kruskal on this sorted list. 
- Because the "bigger" negative costs come first, we add those to MST and prioritise destroying smaller costs. 
- Then when you reach the positive numbers, the smaller ones come first to prioritise building them over the larger ones

Going through the edges list again.
- If an edge is in the MST, and country[i][j] is 0 (it doesnt exist and needs to be built), add its build cost to the total
- If an edge is NOT in the mst, and country[i][j] is 1 (it exists and needs to be destroyed), add its destroy cost to the total