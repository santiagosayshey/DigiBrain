> [!idea] Tree Traversal
> 
> Tree traversal is a method to recursively visit all the nodes in a tree in a specific order.. Tree traversal is crucial because it enables you to perform various tasks, such as searching for a particular node, printing the contents of the tree, or applying a certain operation to each node.
> 
> There are three commonly used methods for traversing a binary tree:
> 
> 1. **In-Order Traversal:**
>    - In-order traversal visits the nodes of a binary tree in the following order:
>      1. Recursively traverse the left subtree.
>      2. Visit the current node.
>      3. Recursively traverse the right subtree.
>    - In the case of a binary search tree (BST), in-order traversal visits the nodes in ascending order of their keys.
>    - In-order traversal is useful for tasks such as printing the nodes in sorted order or performing range queries efficiently.
> 
> 2. **Pre-Order Traversal:**
>    - Pre-order traversal visits the nodes of a binary tree in the following order:
>      1. Visit the current node.
>      2. Recursively traverse the left subtree.
>      3. Recursively traverse the right subtree.
>    - Pre-order traversal is useful for tasks such as creating a copy of the tree or generating a prefix expression of an arithmetic expression tree.
> 
> 3. **Post-Order Traversal:**
>    - Post-order traversal visits the nodes of a binary tree in the following order:
>      1. Recursively traverse the left subtree.
>      2. Recursively traverse the right subtree.
>      3. Visit the current node.
>    - Post-order traversal is useful for tasks such as deleting nodes from a tree or generating a postfix expression of an arithmetic expression tree.
> 
> Tree traversal is important because it allows you to:
> - **Process nodes in a specific order:** Depending on the traversal method, you can visit the nodes of a tree in a particular order, such as ascending order (in-order traversal) or according to their depth (pre-order or post-order traversal).
> - **Perform operations on each node:** Tree traversal enables you to apply a specific operation or function to each node of the tree, such as updating values, searching for a particular node, or collecting data.
> - **Solve various problems:** Many algorithms and problems in computer science rely on tree traversal as a fundamental step. For example, tree traversal is used in search algorithms, tree serialization, tree balancing, and more.
> 
> The time complexity of tree traversal is typically O(n), where n is the number of nodes in the tree, as each node is visited exactly once. The space complexity depends on the maximum depth of the tree, which is O(h) in the worst case, where h is the height of the tree.


