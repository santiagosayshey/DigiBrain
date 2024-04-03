

> [!idea]+ School Method
>
> 1. Split the numbers in half $(k = n/2)$
> 2. **Recursively** find **4** partial products
> 	$P_1 = a_1 \times b_1$
> 	$P_2 = a_1 \times b_0$
> 	$P_3 = a_0 \times b_1$
> 	$P_4 = a_0 \times b_0$
> 3. Add partial products $(P_1 \times 10^k)+(P_2 + P_3)10^{k/2} + P_4$


> [!consider]+ How do we make this better?
>
> The school method has a high computational complexity due to the number of partial products and the size of the numbers involved in the multiplications. To improve this, we can:
>
> 1. Reduce the number of partial products
> 	- Fewer partial products mean fewer multiplications and additions, thus reducing the overall computational complexity.
> 2. Reduce the complexity of the partial product calculations
> 	- If we can find a way to calculate the partial products more efficiently, it will improve the overall performance of the multiplication algorithm.
> 3. Optimize the addition of partial products
> 	- After calculating the partial products, we need to add them together efficiently to get the final result. Optimizing this step can also contribute to better performance.


> [!idea]+ Karatsuba's Method
>
> At each step:
> 1. Split numbers in half
> 2. **Recursively** find **3** partial products
> 	$P_1 = a_1 \times b_1$
> 	$P_2 = (a_1 + a_0) \times (b_1 + b_0)$
> 	$P_3 = a_1 \times b_1$
> 3. Add partial products
> 	$P_1 \times B^{2k} + (P_2 - P_1 - P_3)(B^k) + P_3$

> [!consider] Why is this better?
> It's less computationally expensive at each recursive step
> - School: 4 multiplications + 3 additions
> - Karatsuba: 3 multiplications + 6 additions

> [!consider]+ How much better?
> School method multiplication runs in $O(n^2)$ time where as Karatsuba's Method runs in $O(n^{1.58})$

> [!consider] But *not always* better!
> Generally, we still want to use the school method for $n \le 2$.  
> 
> ![[Pasted image 20240404000635.png]]



> [!exercise]+ Exercise - School Method
> ![[Pasted image 20240404021720.png]]
> 
> ![[Pasted image 20240404021744.png]]
> 
> ![[Pasted image 20240404021800.png]]


> [!exercise]+ Exercise - Karatsuba Method
> ![[Pasted image 20240404021853.png]]
> 
> ![[Pasted image 20240404021905.png]]

# Mock Quiz

> [!exercise] Question 1
> Calculate 42 × 57 using the school method of multiplication.
> 
> ![[Pasted image 20240404022830.png]]



> [!exercise] Question 2
> Calculate 123 × 456 using Karatsuba multiplication. Show the splitting of numbers, the partial products, and the final combination of partial products.

> [!exercise] Question 3
> Which of the following correctly represents the splitting of numbers in the Karatsuba method for the multiplication of 4321 × 5678?
>
> A) a1 = 43, a0 = 21; b1 = 56, b0 = 78
> B) a1 = 432, a0 = 1; b1 = 567, b0 = 8
> C) a1 = 4, a0 = 321; b1 = 5, b0 = 678
> D) a1 = 4321, a0 = 0; b1 = 5678, b0 = 0

> [!exercise] Question 4
> In the Karatsuba multiplication method, which of the following represents the correct formula for combining the partial products?
>
> A) P1 × B^(k1 + k2) + (P2 - P1 - P3)(B^k1) + P3
> B) P1 × B^(k1 + k2) + (P2 - P1 - P3)(B^k2) + P3
> C) P1 × B^(k1 + k2) + (P2 + P1 + P3)(B^k2) + P3
> D) P1 × B^(k1 + k2) + (P2 - P1 - P3)(B^(k1 + k2)) + P3

> [!exercise] Question 5
> Why is Karatsuba multiplication considered more efficient than the school method for large numbers?
>
> A) Karatsuba multiplication requires fewer additions.
> B) Karatsuba multiplication requires fewer multiplications.
> C) Karatsuba multiplication is easier to understand and implement.
> D) Karatsuba multiplication is more efficient for small numbers.




