
| Notation              | Meaning                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------- |
| $f(n) = O(g(n))$      | Highest degree term of $f(n)$ is less than or equal to highest degree term of $g(n)$    |
| $f(n) = \Omega(g(n))$ | Highest degree term of $f(n)$ is greater than or equal to highest degree term of $g(n)$ |
| $f(n) = \Theta(g(n))$ | Highest degree terms of $f(n)$ and $g(n)$ are equal                                     |
| $f(n) = o(g(n))$      | Highest degree term of $f(n)$ is strictly less than highest degree term of $g(n)$       |
| $f(n) = \omega(g(n))$ | Highest degree term of $f(n)$ is strictly greater than highest degree term of $g(n)$    |

| Imbalance Type   | Condition                              | Balance Factor of Node | Balance Factor of Node's Child    | Rotations Needed                                          |
| ---------------- | -------------------------------------- | ---------------------- | --------------------------------- | --------------------------------------------------------- |
| LL (Left-Left)   | Left subtree of left child is deeper   | Balance Factor: +2     | Balance Factor of Left Child: +1  | Single Right Rotation at Node                             |
| RR (Right-Right) | Right subtree of right child is deeper | Balance Factor: -2     | Balance Factor of Right Child: -1 | Single Left Rotation at Node                              |
| LR (Left-Right)  | Right subtree of left child is deeper  | Balance Factor: +2     | Balance Factor of Left Child: -1  | Left Rotation at Left Child, then Right Rotation at Node  |
| RL (Right-Left)  | Left subtree of right child is deeper  | Balance Factor: -2     | Balance Factor of Right Child: +1 | Right Rotation at Right Child, then Left Rotation at Node |
**NOTE:** When performing a x rotation, if a child node has two children, then the x child becomes the child of the root, where x can be left or right. 
