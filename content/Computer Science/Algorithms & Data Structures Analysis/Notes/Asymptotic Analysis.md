
> [!idea] The Idea
> 1. Complexity of algorithm is a function of it's input size $n$.
> 2. Complexity is machine independent
> 3. Complexity measures basic computer steps
> 4. Complexity encompasses both time & space
> 5. Complexity measures best, average and worst cases

When figuring out the complexity of a given algorithm, we must follow some rules:

| **Rule**                            | **Example**                           | **Explanation**                                          |
| ----------------------------------- | ------------------------------------- | -------------------------------------------------------- |
| Ignore Constants                    | ${5n} \rightarrow O(n)$               | Ignore the 5                                             |
| Only worry about highest order term | $3n^3+5n^2+10n+20 \rightarrow O(n^3)$ | $n^3$ is the highest order, so we ignore everything else |
The following picture describes effectiveness of the most common complexities.

![[1 5ZLci3SuR0zM_QlZOADv8Q 1.jpg]]

> [!activity] Exercise 1 - Determine the complexity of the following code segments:

| Type      | Example                                                                                | Complexity                                             | Explanation                                                     |
| --------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------- |
| Constant  | `x = 5 + (15 * 20)`                                                                    | $O(1)$                                                 | Independent of input size $N$                                   |
|           | `x = 5 + (15 * 20)`<br>`y = 15-2`<br>`print x+y`                                       | $O(1)+O(1)+O(1)$<br><br>$= 3\cdot O(1)$<br><br>$=O(1)$ | Add each of their times, ignore the constants                   |
| Linear    | `for x in range (0, n):`<br>            `print x  // O(1)` <br>                        | $N \cdot O(1)$<br><br>$= O(N)$                         | The print statement is $O(1)$ and we do it $N$ times            |
|           | `y = 5 + (15 * 20)`<br>`for x in range (0, n):`<br>            `print x  // O(1)` <br> | $O(1) + O(n)$<br><br>$= O(N)$                          | The summation of each step and we ignore the lower  order terms |
| Quadratic | `for x in range (0, n):`<br>  `for y in range (0, n):`<br>      `print x*y   \\ O(1)`  | $O(N^2)$                                               | The print statement is executed $N \cdot N$ times               |

> [!activity] Exercise 2 - Determine the complexity of the following code segment:

```python
x = 5 + (15 * 20)                                     # O(1)
for x in range (O,n):
	print x                                           # O(N)
for x in range (O,n):
	for y in range (O,n):
		print x*y                                     #(N^2)
```

| #   | Step                                        | Working Out        |
| --- | ------------------------------------------- | ------------------ |
| 1   | Take the summation of each of the run times | $O(1)+O(N)+O(N^2$) |
| 2   | Find the highest order term                 | $O(N^2)$           |
> [!activity] Exercise 3 - Determine the complexity of the following code segment:

```python
if x > 0:
	# O(1)
else if x < 0:
	# O(logn)
else:
	# O(n^2)
```

| #   | Step                                                 | Working Out |
| --- | ---------------------------------------------------- | ----------- |
| 1   | Take the largest run time (since we want worst case) | $O(N^2)$    |

![[1.4]]
