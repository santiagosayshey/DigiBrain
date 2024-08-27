
> [!idea] Number Representation
> $$
\text{Any digit \(d\) of any base \(B\), can be represented in decimal by:} \quad d = \sum_{i=0}^{n-1} d_i B^i
> $$
> | Base (B)         | Expression                                                  | Decimal Value |
| ---------------- | ----------------------------------------------------------- | ------------- |
| 2 (binary)       | $1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0$     | 11            |
| 8 (octal)        | $5 \cdot 8^3 + 3 \cdot 8^2 + 4 \cdot 8^1 + 7 \cdot 8^0$     | 2791          |
| 10 (decimal)     | $1 \cdot 10^3 + 7 \cdot 10^2 + 0 \cdot 10^1 + 9 \cdot 10^0$ | 1709          |
| 16 (hexadecimal) | $A \cdot 16^3 + D \cdot 16^2 + 5 \cdot 16^1 + A \cdot 16^0$ | 44378         |

This formula is essentially saying, for every digit in a number, multiply each of them by the base to the power of the position of the digit and sum each result. 
