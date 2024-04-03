

> [!idea]+ School Method
>
> 1. Split the numbers in half $(k = n/2)$
> 2. **Recursively** find **4** partial products
> 	$P_1 = a_1 \times b_1$
> 	$P_2 = a_1 \times b_0$
> 	$P_3 = a_0 \times b_1$
> 	$P_4 = a_0 \times b_0$
> 3. Add partial products $(P_1 \times 10^k)+(P_2 + P_3)10^{k/2} + P_4$

> [!consider] How do we make this better?
> Reduce the computational complexity of the partial products? Reduce the number of partial products?

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
>
> (where $B$ is the base)

Why is this better?

> [!consider]
> More computationally expensive:
> - School: 4 multiplications + 3 additions
> - Karatsuba: 3 multiplications + 6 additions

The callouts have been formatted correctly with lines starting with ">", and the partial products in Karatsuba's method are now inline without math blocks. A new "consider" callout has been added at the end for the text comparing the computational complexity of the school method and Karatsuba's method.