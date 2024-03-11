Recall [[Proof by Induction]]:

> [!exercise]+ Exercise 1 - Prove $n^3 +2n$ is divisible by 3 using mathematical induction.
> ![[Pasted image 20240311154300.png]]

> [!exercise]+ Exercise 2 - Prove the sum of the first $n$ positive integers is equal to $\frac{n(n+1)}{2}$ using mathematical induction.
> 
> ![[Pasted image 20240311160232.png]]

> [!exercise]+ Exercise 3- Let $F(n)$ be the $n'th$ Fibonacci number. We have that $F(1) = F(2) = 1$ and $F(n)=F(n-1)+F(n-2)$. Find a value $a$ so that $F(n) \in O(a^n)$. We want $a$ to be as small as possible.

Recall [[Randomised Algorithms]]:


> [!exercise]+ Exercise 4 
> Suppose your task is to implement a boolean function called `badSign` that takes an integer input and returns true if the input is positive and false otherwise. However, you are required to write `badSign` so that it, randomly, 25% of the time returns the incorrect boolean value. How would you implement such a function?

```c
function badSign(int i) {
	sign = false
	
	if i > 0
		sign = true
	
	if rand(25%)
		return !sign
		
	return sign
}
```

> [!exercise] Exercise 5
> Suppose your second task is to implement a boolean function called `betterSign` that takes an integer input and returns true if the input is positive and false otherwise. However, this time, you are not allowed to directly inspect the input integer x. You are only allowed to inspect `badSign(x)`. How would you write the `betterSign` function, in order to obtain a function that is more accurate than `badSign` itself?
> 

Call `badSign` over and over, store the results. The result with the higher percentage is true.

```c
function betterSign(int i) {

	for i=1 to x
		sign = badSign(i)
		if sign
			pos++
		else
			neg++
	
	if pos > neg
		return true
	return false
}
```

> [!exercise] Exercise 6
> What happens when `badSign` is incorrect 49% of the time? What happens when `badSign` is incorrect 51% of the time?


