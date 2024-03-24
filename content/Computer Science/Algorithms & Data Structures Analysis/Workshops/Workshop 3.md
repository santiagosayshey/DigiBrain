
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
> - $c=1$
> - $d=\frac{1}{2}$
> - **$d<b$**
> 
> This means:
> $$T(n) = \Theta(n^{\log _ba}) = \Theta(n^{\log_2 1})$$

