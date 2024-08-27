
Recall [[2.4 Master Theorem]]

> [!exercise]+ Exercise 1 - Find the complexity of the following recurrence relation:
> $$
T(n) =
\begin{cases}
1 & \text{if } n=1 \\
n+\frac{T(\frac{n}{2})}{2} & \text{if } n>1 \\
\end{cases}
> $$
> We can see that:
> - $a=1/2$
> - $b=2$
> - $d=1$
> - $a<b^d = \frac{1}{2}<2$
> 
> This means:
> $$T(n) \in O(n^d) = O(n)$$

