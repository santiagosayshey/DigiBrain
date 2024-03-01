
> [!idea] The Idea
> Reduce complexity of school method multiplication through recursion! Let $a$ and $b$ be the numbers to be multiplied:

$$
a \times b = (a_1 \cdot B^k + a_0) \times (b_1 \cdot B^k + b_0) \\
= a_1b_1 \cdot B^{2k} + (a_1b_0 + a_0b_1) \cdot B^k + a_0b_0
$$


>[!math] Theorem - Recursive Multiplication
> Let $T(n)$ be the maximal number of primitive operations to multiply two n-digit numbers recursively.
>$$
T(n) \leq \begin{cases} 
1 & \text{if } n = 1 \\
4 \cdot T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + 3 \cdot 2^n & \text{if } n \geq 2 
\end{cases}
> $$
> $$
\text{For } n \text{ power of } 2 : T(n) \leq 7n^2 - 6n
> $$
> $$
\text{For general } n : T(n) \leq 28n^2
> $$

We can prove this using traditional induction method, or we can use the [[Master Theorem]]

