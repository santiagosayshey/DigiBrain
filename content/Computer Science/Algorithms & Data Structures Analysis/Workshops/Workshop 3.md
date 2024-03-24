
> [!idea]+ Master Theorem (Simple Form)
> For positive constants $a$, $b$, $c$ and $d$, and $n=b^k$ for some integer $k$, consider the recurrence:
> $$
r(n) =
\begin{cases}
a & \text{if } n=1 \\
cn +dr(\frac{n}{b}) & \text{if } n>1 \\
\end{cases}
> $$
> Then:
> $$
r(n) = \Theta
\begin{cases}
n^{\log _ba} & \text{if } d<b \\
n^{\log _ba}\log n & \text{if } d=b \\
n^{\log _dc} & \text{if } d>b \\
\end{cases}
> $$


> [!exercise]+ Exercise 1 - Find the complexity of the following recurrence relation:
> $$
T(n) =
\begin{cases}
1 & \text{if } n=1 \\
n+T(\frac{n}{2}) & \text{if } n>1 \\
\end{cases}
> $$
> We can see that:
> - $a=1$
> - $b=2$
> - $c=1$
> - $d=1$
> - **$d<b$**
> 
> This means:
> $$T(n) = \Theta(n^{\log _ba}) = \Theta(n^{\log_2 1})$$

wha