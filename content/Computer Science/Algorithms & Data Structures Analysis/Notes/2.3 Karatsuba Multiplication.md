
> [!idea] The Idea
> Reduce complexity of recursive multiplication by reducing the number of multiplications! Let $a$ and $b$ be the numbers to be multiplied. 
> 
> Karatsuba's algorithm achieves this by ingeniously reducing the number of recursive multiplications needed to compute the product of two numbers. Instead of the traditional four multiplications required in the recursive method, Karatsuba's algorithm only requires three. This is accomplished by breaking down each number into two parts, $a_1$ and $a_0$ for the first number, and $b_1$ and $b_0$ for the second, where $B$ is the base and $k$ is half the number of digits (or approximately so) in the larger of $a$ and $b$. The key insight of Karatsuba's method is in recognizing that the middle term of the product $(a_1 b_0 + a_0 b_1)B^k$ can be cleverly computed using only three multiplications instead of four by calculating $(a_1 + a_0) \times (b_1 + b_0)$, and then subtracting the products $a_1 \times b_1$ and $a_0 \times b_0$. This reduction in the number of multiplications significantly decreases the overall computational complexity, especially for very large numbers, making it a groundbreaking improvement over the naive recursive method.


$$
\begin{align*}
a \times b &= (a_1 B^{k} + a_0) \times (b_1 B^{k} + b_0) \\
&= (a_1 b_1) B^{2k} + (a_1 b_0 + a_0 b_1) B^{k} + a_0 b_0 && \text{(Recursive Method)} \\
&= (a_1 \times b_1) B^{2k} + \left((a_1 + a_0) \times (b_1 + b_0) - (a_1 \times b_1 + a_0 \times b_0)\right) B^{k} + a_0 \times b_0 && \text{(Karatsuba)}
\end{align*}
$$


| Method    | Multiplication Steps | Addition Steps |
| --------- | -------------------- | -------------- |
| Recursion | 4                    | 3              |
| Karatsuba | 3                    | 6              |
| $O(n)$    | $n^2$                | $n$            |


> [!math] Karatsuba Complexity
> $$
T_K(n) \leq
\begin{cases}
3n^2 + 2n & \text{if } n < 4 \\
3 \cdot T_K\left(\left\lceil \frac{n}{2} \right\rceil + 1\right) + 6 \cdot 2 \cdot n & \text{if } n \geq 4
\end{cases}
> $$
> $$
T_K(n) \leq 207 \cdot n^{\log_3 3}
$$

When $n \lt 4$, use the recursive method. If $n \gt 4$, use Karatsuba's method

