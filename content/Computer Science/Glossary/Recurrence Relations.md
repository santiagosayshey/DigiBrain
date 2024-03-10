
> [!idea] Recurrence Relations
> 
> Recurrence relations are mathematical equations that describe the running time or space complexity of recursive algorithms by expressing the performance of the algorithm in terms of its input size. They offer a structured way to analyze and predict the efficiency of recursive algorithms as the size of the input data changes.
> 
> Recurrence relations are useful for understanding and analyzing various types of recursive algorithms, including those that break down a problem into smaller subproblems, solve these subproblems recursively, and then combine the solutions to solve the original problem (e.g., divide and conquer algorithms). They are also applicable to other recursive paradigms such as decrease and conquer, dynamic programming, and backtracking.


> [!exercise]+ Example - Fibonacci Sequence
> 
> Let's find the recurrence relation for the Fibonacci sequence using the code provided:
> 
> ```c
> int fibonacci(int n) 
> {
>     if (n == 0)
>     {
>         return 0;
>     }
>     else if (n == 1)
>     {
>         return 1;
>     }
>     else
>     {
>         return fibonacci(n - 1) + fibonacci(n - 2);
>     }
> }
> ```
> 
> The recurrence relation for the Fibonacci sequence can be written as:
> 
> ```
> F(n) = 0, if n = 0
>      = 1, if n = 1
>      = F(n-1) + F(n-2), if n > 1
> ```
> 
> This recurrence relation states that the nth Fibonacci number is equal to the sum of the (n-1)th and (n-2)th Fibonacci numbers, with the base cases of F(0) = 0 and F(1) = 1.

> [!exercise]+ Example - Factorial
> 
> Now, let's find the recurrence relation for the factorial function using the following code:
> 
> ```c
> int factorial(int n) 
> {
>     if (n == 0)
>     {
>         return 1;
>     }
>     else
>     {
>         return n * factorial(n - 1);
>     }
> }
> ```
> 
> The recurrence relation for the factorial function can be written as:
> 
> ```
> F(n) = 1, if n = 0
>      = n * F(n-1), if n > 0
> ```
> 
> This recurrence relation states that the factorial of n (denoted as n!) is equal to n multiplied by the factorial of (n-1), with the base case of F(0) = 1.

In both examples, the recurrence relations capture the recursive nature of the functions and provide a mathematical representation of how the functions compute their results based on smaller subproblems.



> [!idea]+ Solving Recurrence Relations
> There are many ways, but the main way is to use the [[2.3 Master Theorem|Master Theorem]]

When we combine subproblems, we have to consider the work taken to combine the results of the subproblems. This is usually a constant in the non base case. 