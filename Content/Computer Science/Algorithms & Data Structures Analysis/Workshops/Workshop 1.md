

> [!exercise]+ Exercise 1 - Determine if the following are right or wrong

| Statement<br>                   | True / False | Explanation                                                                            |
| ------------------------------- | ------------ | -------------------------------------------------------------------------------------- |
| $n^2 + 10^6n \in O(n^2)$<br>    | True         | A constant c exists whereby $c \cdot n^2$  > $n^2$. For example, $2 \cdot n^2 \gt n^2$ |
| $n \cdot \log{n} \in O(n)$      | False        | A constant c *does not* exist whereby $c \cdot n$  > $n \cdot \log{n}$.                |
| $n \cdot \log{n} \in \Omega(n)$ | True         | A constant c exist whereby $c \cdot n$  < $n \cdot \log{n}$.                           |
| $\log{n} \in o(n)$              | True         | $\lim_{n \to \infty} \frac{\log{n}}{n} = 0$                                            |
> [!exercise]+ Exercise 2 - Prove the following

| Statement                                                   | Answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $c \cdot f(n) = \Theta(f(n))$ for any positive constant $c$ | An algorithm $T(n)$ is tightly bounded by a function $f(n)$ if and only if there exist constants $c_1$ and $c_2$ whereby $T(n)$ is sandwiched between $c_1 \cdot f(n)$ and $c_2 \cdot f(n)$ for every $n$ larger than some initial. <br><br>Since $c$ can be any positive constant, we can say that $f(n)$ multiplied by two constants - $c_0$ and $c_1$ where $c_0 \lt c$ and $c_1 \gt c$ acts as a tight bound for $c \cdot f(n)$<br>                                                                                                |
| $f(n) + g(n) = \Omega(f(n))$                                | An algorithm $T(n)$ is lower bounded by a function $f(n)$ if and only if there exists a constant $c$ whereby $T(n)$ is greater than or equal to $c \cdot f(n)$ for every $n$ larger than some initial <br><br><br>The sum of two functions always grows at least as fast as 1 of the functions. This means that we can treat each singular function as a lower bound for the sum of the two functions. I.e. there exists no constant $c$ such that $c \cdot f(n) > f(n) + g(n)$                                                        |
| $f(n) + g(n) = O(f(n))$ if $g(n) = O(f(n))$                 | If $g(n)$ is upper bounded by $f(n)$, meaning there exists some constant $c \geq 1$ such that $g(n) \leq c \cdot f(n)$ for all $n \geq n_0$, then the sum $f(n) + g(n)$ is also upper bounded by a constant multiple of $f(n)$. Specifically, we can find a constant $c'$ such that $f(n) + g(n) \leq c' \cdot f(n)$ for all $n \geq n_1$, where $n_1$ is suitably chosen. This conclusion follows because the growth of $f(n)$ dominates or is at least equivalent to the growth of $g(n)$, making $f(n)$ an upper bound for the sum. |
| $O(f(n)) \cdot O(g(n)) = O(f(n) \cdot g(n))$                | Let $f(n) \in O(g(n))$ and $h(n) \in O(p(n))$. By definition, there exist positive constants $c_1$, $c_2$, $n_0$, and $n_1$ such that for all $n \geq n_0$, $f(n) \leq c_1g(n)$, and for all $n \geq n_1$, $h(n) \leq c_2p(n)$. Taking the product of these two inequalities gives: for all $n \geq \max(n_0, n_1)$, $f(n)h(n) \leq c_1c_2g(n)p(n)$. Thus, we have $f(n)h(n) \in O(g(n)p(n))$, demonstrating that the product of two $O$-notations results in an $O$-notation of the product of their functions.                       |

> [!exercise]+ Exercise 3
$\text{Is it true that if } f(n) =\Theta(g(n)) \text{ and } g(n) = \Theta(h(n)), \text{ then } h(n) = \Theta(f(n))?$

This is true. Asymptotically similar functions are transitively tightly bounded in either direction. 

```functionplot
---
title:
xLabel: x
yLabel: y
bounds: [0,3,0,3]
disableZoom: true
grid: true
---
T(x)=x
f(x)=2*x
g(x)=3*x
```
In the graph, we see 3 asymptotically tight functions - x, 2x and 3x. They’re all tight bounds for each other. 
> [!exercise]+ Exercise 4
$\text{Is it true that if } f(n) = O(g(n)) \text{ and } g(n) = O(h(n)), \text{ then } h(n) = \Omega(f(n))?$

This is true. Essentially we are saying that $h(n)$ grows faster than $g(n)$ and $g(n)$ grows faster than $f(n)$. This means that $h(n)$ also grows faster than $f(n)$ and therefore $f(n)$ is a lower bound for $h(n)$ as it is for $g(n)$

> [!exercise]+ Exercise 5
$\text{Is it true that a } \Theta(n^2) \text{ algorithm always takes longer to run than a } O(\log n) \text{ algorithm?}$

This is not true. We must consider constant terms. It is true to say that $O(\log{n})$ is asymptotically faster than $\Theta(n^2)$, but it is not true, say when we have a small n.

Example: $f(n) = 10000 \cdot \log{n}$ and $g(n) = 0.5n^2$ for $n=16$

$g(n)$ _will_ behave faster in this example, but the it’s growth rate is still faster.


> [!exercise]+ Exercise 6
$\text{For each pair of functions given below, point out the asymptotic relationships that apply: } f = O(g), f = \Theta(g), f = \Omega(g).$
$1.\ f(n) = \sqrt{n} \text{ and } g(n) = \log(n)$
$2.\ f(n) = 1 \text{ and } g(n) = 2$
$3.\ f(n) = 1000 \cdot 2^n \text{ and } g(n) = 3^n$
$4.\ f(n) = 4^{n+4} \text{ and } g(n) = 2^{2n+2}$
$5.\ f(n) = 5n\log(n) \text{ and } g(n) = n\log(5n)$
$6.\ f(n) = n! \text{ and } g(n) = (n + 1)!$

| Problem | $f(n)$           | $g(n)$      | $f = O(g)$ | $f = \Theta(g)$ | $f = \Omega(g)$ |
| ------- | ---------------- | ----------- | ---------- | --------------- | --------------- |
| 1       | $\sqrt{n}$       | $\log(n)$   | No         | No              | Yes             |
| 2       | 1                | 2           | Yes        | Yes             | Yes             |
| 3       | $1000 \cdot 2^n$ | $3^n$       | Yes        | No              | No              |
| 4       | $4^{n+4}$        | $2^{2n+2}$  | Yes        | Yes             | Yes             |
| 5       | $5n\log(n)$      | $n\log(5n)$ | No         | No              | Yes             |
| 6       | $n!$             | $(n + 1)!$  | Yes        | No              | No              |


> [!exercise]+ Exercise 7
$\text{Prove that } n^k = o(c^n) \text{ for any integer } k \text{ and any } c > 1.$

Prove that $n^k$ is strictly upper bounded by $c^n$

Must prove that $\lim_{n \to \infty} \frac{T(n)}{f(n)} = 0$

$\frac{c^n}{n^k}$ - we 