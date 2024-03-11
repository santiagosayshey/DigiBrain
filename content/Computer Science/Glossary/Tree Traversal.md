> [!idea] Tree Traversal
> 
> Tree traversal is a recursive method to visit all the nodes in a tree in a specific order. There are three commonly used methods for traversing a binary tree:
> 
> 1. In-Order Traversal:
> 2. Pre-Order Traversal:
> 3. Post-Order Traversal:
>    
> In each pseudocode, the `visit(node)` function represents the operation or action you want to perform on the current node during the traversal. This could be printing the node's value, updating its data, or any other desired operation.

> [!idea] In-Order Traversal
> 
> In-order traversal visits the nodes of a binary tree in the following order:
> 1. Recursively traverse the left subtree.
> 2. Visit the current node.
> 3. Recursively traverse the right subtree.
> 
> In the case of a binary search tree (BST), in-order traversal visits the nodes in ascending order of their keys.
> 
> ```
> function inOrderTraversal(node):
>     if node is not None:
>         inOrderTraversal(node.left)
>         visit(node)
>         inOrderTraversal(node.right)
> ```

> [!idea] Pre-Order Traversal
> 
> Pre-order traversal visits the nodes of a binary tree in the following order:
> 1. Visit the current node.
> 2. Recursively traverse the left subtree.
> 3. Recursively traverse the right subtree.
> 
> Pre-order traversal is useful for tasks such as creating a copy of the tree or generating a prefix expression of an arithmetic expression tree.
> 
> ```
> function preOrderTraversal(node):
>     if node is not None:
>         visit(node)
>         preOrderTraversal(node.left)
>         preOrderTraversal(node.right)
> ```

> [!idea] Post-Order Traversal
> 
> Post-order traversal visits the nodes of a binary tree in the following order:
> 1. Recursively traverse the left subtree.
> 2. Recursively traverse the right subtree.
> 3. Visit the current node.
> 
> Post-order traversal is useful for tasks such as deleting nodes from a tree or generating a postfix expression of an arithmetic expression tree.
> 
> ```
> function postOrderTraversal(node):
>     if node is not None:
>         postOrderTraversal(node.left)
>         postOrderTraversal(node.right)
>         visit(node)
> ```


