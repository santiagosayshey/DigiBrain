

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

> [!idea]+ How much better?
> School method multiplication runs in $O(n^2)$ time where as Karatsuba's Method runs in $O(n^{1.58})$

