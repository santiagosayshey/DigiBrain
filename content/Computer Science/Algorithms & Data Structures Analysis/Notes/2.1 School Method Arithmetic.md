
> [!math] Number Representation
> $$
\text{Any digit \(d\) of any base \(B\), can be represented in decimal by:} \quad d = \sum_{i=0}^{n-1} d_i B^i
> $$

This formula is essentially saying, for every digit in a number, multiply each of them by the base to the power of the position of the digit and sum each result. 

| Base (B)         | Expression                                                  | Decimal Value |     |
| ---------------- | ----------------------------------------------------------- | ------------- | --- |
| 2 (binary)       | $1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0$     | 11            |     |
| 8 (octal)        | $5 \cdot 8^3 + 3 \cdot 8^2 + 4 \cdot 8^1 + 7 \cdot 8^0$     | 2791          |     |
| 10 (decimal)     | $1 \cdot 10^3 + 7 \cdot 10^2 + 0 \cdot 10^1 + 9 \cdot 10^0$ | 1709          |     |
| 16 (hexadecimal) | $A \cdot 16^3 + D \cdot 16^2 + 5 \cdot 16^1 + A \cdot 16^0$ | 44378         |     |


>[!math] Theorem - School Method Addition
> $$
\text{The addition of two n-digit integers requires exactly n primitive operations. The result is at most, an n+1 digit integer.}
$$

$$


\begin{array}{c@{\;}c@{\;}c@{\;}c@{\;}c}
  & 1 & 7 & 0 & 9 \\
+ & 2 & 5 & 3 & 0 \\
\hline
\text{carries} & 1 & 0 & 0 & 0 \\
\hline
\text{sum} & 4 & 2 & 3 & 9 \\
\end{array}

$$
In code, we implement this as follows:

```python
a=number1
b=number2
n=numberofdigits

carry=0
for i=0 to n-1 do
	s[i] = a[i] + b[i]
	carry = s[i] / base
	s[i] = s[i] % base
end for
s[n] = carry
```


>[!math] Theorem - School Method Addition
>$$
\text{The school method multiplication of two n-digit integers requires \:}
3n^2 + 2n = n^2 \:
\text{primitive operations.}
$$


$$
\begin{array}{r}\
\\
\phantom{00}1709 \\
\times \phantom{0}25 \\
\hline
\phantom{0}8545 \text{ (partial product } a \cdot b_0\text{)} \\
34180 \text{ (partial product } a \cdot b_1\text{)} \\
\hline
42725 \text{ (add aligned partial products)}
\end{array}
$$

In pseudo code, this can be represented as follows:

```python
a=number1
b=number2
n=numberofdigits

product=0

for i=0 to n-1 do
	product = product + a * b[i] * base^[i]
end for
```


We already have a pretty fast algorithm to compute addition, but can we make a faster multiplication algorithm than $O(n^2)$?







