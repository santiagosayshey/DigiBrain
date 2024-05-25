> [!motivation] Minimizing Functions
> In various fields, such as mathematics, engineering, and computer science, there is often a need to find the minimum value of a function. This could be for optimization purposes, such as minimizing the cost of production, reducing error in a model, or finding the most efficient path in a network.

> [!idea] Optimization
> Optimization is the process of finding the best solution to a problem from a set of possible solutions. In the context of minimizing functions, optimization involves finding the input values that result in the smallest output value of the function. This is typically done using various optimization algorithms, such as gradient descent, Newton's method, or the simplex method.

> [!idea] Local vs. Global Minima
> - Local minimum: A point where the function value is smaller than or equal to nearby points, but not necessarily the smallest value in the entire domain.
> - Global minimum: The point with the smallest function value in the entire domain.
> 
> In some cases, a function may have multiple local minima but only one global minimum. Optimization algorithms may get stuck in local minima, preventing them from finding the global minimum.

> [!example] Example: Quadratic Function
> Consider the quadratic function $f(x) = x^2 - 4x + 5$. To find the minimum point, we can use calculus:
> 1. Find the derivative: $f'(x) = 2x - 4$
> 2. Set the derivative equal to zero and solve for x: $2x - 4 = 0 \implies x = 2$
> 3. Evaluate the function at the critical point: $f(2) = 2^2 - 4(2) + 5 = 1$
> 
> Therefore, the minimum point of the function is at $(2, 1)$.
> 
> ```image_goes_here
> A graph of the quadratic function f(x) = x^2 - 4x + 5, showing the minimum point at (2, 1).
> ```

> [!consider] Gradient Descent
> Gradient descent is a popular optimization algorithm used to find the minimum of a function. It works by iteratively taking steps in the direction of the negative gradient of the function at the current point. The size of the steps is determined by the learning rate. Gradient descent can be used for various types of functions, including those with multiple variables.
> 
> The update rule for gradient descent is:
> $$
> x_{n+1} = x_n - \gamma \nabla f(x_n)
> $$
> where $x_n$ is the current point, $\gamma$ is the learning rate, and $\nabla f(x_n)$ is the gradient of the function at $x_n$.

> [!consider] Constrained Optimization
> In some cases, the optimization problem may have constraints on the input values. This is known as constrained optimization. Techniques such as Lagrange multipliers or the Karush-Kuhn-Tucker (KKT) conditions can be used to solve constrained optimization problems.