
> [!idea] The Idea
> When we discuss an algorithm's time complexity, we often represent it as a function $T(n)$, where $n$ is the size of the input. As $N$ increases, the execution time of the algorithm typically increases as well. *The goal of asymptotic notation is to provide ways to describe the behaviour of $T(n)$ as $n$ approaches infinity.* This helps in comparing algorithms by providing a high-level understanding of their efficiency in terms of time and space.

====

| Bound                | Symbol                      | Mathematical Description                                                                             | Logical Description                                                                                                                                                                                                                    |
| -------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Upper Bound          | $O$ <br>(big oh)            | $T(n)\;is\;O(f(n)) \iff T(n) \leq c \cdot f(n)\;\forall \; n > n_0$                                  | An algorithm $T(n)$ is upper bounded by a function $f(n)$ if and only if there exists a constant $c$ whereby $T(n)$ is smaller than $c \cdot f(n)$ for every single $n$ bigger than the initial $n$                                    |
| Lower Bound          | $(\Omega)$ <br>(big omega)  | $T(n) \; is \; \Omega(f(n)) \iff c \cdot f(n) \leq T(n) \; \forall \; n > n_0$                       | An algorithm $T(n)$ is lower bounded by a function $f(n)$ if and only if there exists a constant $c$ whereby $T(n)$ is greater than or equal to $c \cdot f(n)$ for every $n$ larger than some initial $n$                              |
| Tight Bound          | $(\Theta)$ <br>(theta)      | $T(n) \; is \; \Theta(f(n)) \iff c_1 \cdot f(n) \leq T(n) \leq c_2 \cdot f(n) \; \forall \; n > n_0$ | An algorithm $T(n)$ is tightly bounded by a function $f(n)$ if and only if there exist constants $c_1$ and $c_2$ whereby $T(n)$ is sandwiched between $c_1 \cdot f(n)$ and $c_2 \cdot f(n)$ for every $n$ larger than some initial $n$ |
| Stricter Upper Bound | $o$ <br>(little oh)         | $T(n) \; is \; o(f(n)) \iff \lim_{n \to \infty} \frac{T(n)}{f(n)} = 0$                               | An algorithm $T(n)$ grows strictly slower than $f(n)$ if and only if the ratio of $T(n)$ to $f(n)$ approaches 0 as $n$ becomes infinitely large.                                                                                       |
| Stricter Lower Bound | $\omega$ <br>(little omega) | $T(n) \; is \; \omega(f(n)) \iff \lim_{n \to \infty} \frac{T(n)}{f(n)} = \infty$                     | An algorithm $T(n)$ grows strictly faster than $f(n)$ if and only if the ratio of $T(n)$ to $f(n)$ becomes infinitely large as $n$ grows without bound.                                                                                |

 >[!visual] Graphically
> **Upper Bound** - If we have two functions $T(n) = n$ and $f(n)=n^2$, we can say that $T(n)$ is upper bounded by $f(n)$.
> 
> **Lower Bound** - What happens when we can't find a constant $c$ such that $c \cdot f(n)$ is greater than $f(n)$? If we have two functions $T(n) = n$ and $f(n)=log(n)$, we can say that $T(n)$ is lower bounded by $f(n)$.



```functionplot
---
title: 
xLabel: x
yLabel: y
bounds: [0,5,0,5]
disableZoom: true
grid: true
---
T(x)=x
f(x)=x^2
g(x)=log(x)
```

>[!idea] Consider:
>When evaluating the efficiency of an algorithm, it's crucial to consider how **tight** our bound is. Although multiple functions can serve as upper and lower bounds for $T(n)$, not all of them provide an accurate representation of the algorithm's efficiency. A _tighter_ bound, which closely matches the actual growth rate of $T(n)$, offers a more precise understanding of the algorithm's performance. It is *both* an upper AND lower bound at the same time. 

 >[!visual] Graphically
> **Tight Bound** - If we have two functions $T(n) = n$ and $f(n)=n$, we can say that $T(n)$ has a tight bound $f(n)$, because there exists two constants $c_1$ and $c_2$ that sandwich $T(n$)
> 
> There also exists two other bounds, which describe upper and lower bounds that are **NOT** tight. 


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
g(x)=0.5*x
```


> [!activity] Exercise 1 - Determine the correctness of the following statements:

| Statement                         | In English                                                       | Answer | Explanation                                                                                        |
| --------------------------------- | ---------------------------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------- |
| $5n \log n \in O(n \log n)$       | $n \cdot \log(n)$ is an upper bound for $5n \cdot \log(n)$       | True   | Dropping constants, it's the same function. Therefore, it's a tight bound and also an upper bound. |
| $5n \log n \in O(n^2)$            | $n^2$ is an upper bound for $5n \cdot \log(n)$                   | True   | As $n$ grows, $n^2$ increases faster than $n \log n$, making $n^2$ an upper bound.                 |
| $5n \log n \in \Omega(n^2)$       | $n^2$ is a lower bound for $5n \cdot \log(n)$                    | False  | $n \log n$ grows slower than $n^2$, so $n^2$ cannot be a lower bound for $5n \log n$.              |
| $5n \log n \in o(n^2)$            | $5n \cdot \log(n)$ grows strictly slower than $n^2$              | True   | For very large $n$, $n^2$ grows much faster than $n \log n$, so $5n \log n$ is in $o(n^2)$.        |
| $5n \log n + n^2 \in O(n \log n)$ | $n \cdot \log(n)$ is an upper bound for $5n \cdot \log(n) + n^2$ | False  | $n^2$ term dominates as $n$ grows, so $n \log n$ cannot be an upper bound for the sum.             |
| $5n \log n + n^2 \in O(n^2)$      | $n^2$ is an upper bound for $5n \cdot \log(n) + n^2$             | True   | $n^2$ is the highest order term, making it the tight bound and thus also an upper bound.           |
> [!activity] Exercise 2 - Find the bound for each function

| Function         | Upper Bound | Lower Bound        | Tight Bound   | Strict Upper Bound | Strict Lower Bound |
| ---------------- | ----------- | ------------------ | ------------- | ------------------ | ------------------ |
| $5n$             | $O(n)$      | $\Omega(n)$        | $\Theta(n)$   | $o(n \log n)$      | $\omega(\sqrt{n})$ |
| $n^2 - n \log n$ | $O(n^2)$    | $\Omega(n^2)$      | $\Theta(n^2)$ | $o(n^3)$           | $\omega(n \log n)$ |
| $100n$           | $O(n^2)$    | $\Omega(\sqrt{n})$ | $\Theta(n)$   | $o(n \log n)$      | $\omega(\sqrt{n})$ |

