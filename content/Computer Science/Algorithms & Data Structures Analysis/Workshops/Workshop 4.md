
> [!exercise]+ Exercise 1
> Argue that since sorting n elements takes $O(n \cdot \log n)$ time in the worst case in the comparison model, any comparison based algorithm for constructing a binary search tree from an arbitrary list of n elements take  $O(n \cdot \log n)$ time in the worst case.
> 
> **Answer:**
> Sure! Here's a more succinct and direct response, directly addressing the core question:

- **Assumption**: Suppose we can construct a binary search tree (BST) from a list of \( n \) elements in less than \( n \log n \) time (little-o \( n \log n \)).
  
- **BST to Sorting**: After building the BST, we perform an in-order traversal, which outputs the elements in sorted order. The traversal takes \( O(n) \) time.

- **Total Time**: The total time for both constructing the BST and sorting the elements via traversal is thus less than \( n \log n \).

- **Contradiction**: Since sorting any list of \( n \) elements requires at least \( n \log n \) time in the comparison model, our assumption leads to a contradiction.

- **Conclusion**: Therefore, constructing a BST from an arbitrary list of \( n \) elements using any comparison-based method must take at least \( n \log n \) time in the worst case.


> [!exercise]+ Exercise 2
> Professor Bunyan believes he has uncovered a remarkable property of binary search trees. Consider searching for key k in a binary search tree that ends at a leaf. Let:
> - A be the set of keys strictly to the left of the search path. 
> - B be the set of keys on the search path itself. 
> - C be the set of keys strictly to the right of the search path.  
>   
> Professor Bunyan claims that for any a ∈ A, b ∈ B, and c ∈ C, it holds that a ≤ b ≤ c. Provide the smallest possible counterexample to disprove this claim.


Inserting a single element into a tree takes $O(\log n)$ time in the worst case. Since we have n elements to insert, the total time to construct the binary search tree is $O(n \log n)$.

We can argue that this O(n log n) time is a lower bound for any comparison-based algorithm because constructing a binary search tree allows us to sort the list of elements. We know that sorting a list of n elements using comparisons requires at least O(n log n) time in the worst case. Therefore, constructing a binary search tree must also take at least O(n log n) time when using comparisons. If there were a faster comparison-based algorithm to construct a binary search tree, it would contradict the lower bound for comparison-based sorting.