
> [!idea] The Idea
> Review [[1.3 School Method Arithmetic]] and [[2.2 Karatsuba Multiplication]] on implementation details. Full implementation [here](https://github.com/santiagosayshey/ADSA-S1-2024/blob/assignment1/main.py): 
> 

# Addition

```python
def add(i1, i2, b):
    bigger = max(i1, i2)
    smaller = min(i1, i2)

    carry = 0
    number = []

    while bigger > 0 :
        digit = bigger % b + smaller % b + carry
        carry = digit // b
        number.append(digit % b)

        bigger = bigger // b
        smaller = smaller // b

    if carry > 0 :
        number.append(carry)

    sum = 0
    i=0

    for digit in number:
        sum += digit*pow(10,i)
        i += 1

    return sum
```

# Karatsuba Multiplication

```python
def split_number(n, k, b):
    high = n // b**k
    low = n % b**k
    return low, high

def multiply(i1, i2, b):

    if i1 < b :
        return i1 * i2 # base case
    
    n = max(len(str(i1)), len(str(i2)))
    k = n // 2
    

    a0, a1 = split_number(i1, k, b) 
    b0, b1 = split_number(i2, k, b)

    x1 = multiply(a0, b0, b)
    x3 = multiply(a1, b1, b)
    x2 = multiply((a0+a1),(b0+b1), b) - x1 - x3

    return x3 * (pow(b, 2*k)) + x2 * (pow(b,k)) + x1

def decimal_to_base(num, base):
    if num == 0:
        return "0"
    
    digits = "0123456789"
    result = ""

    while num > 0:
        result = digits[num % base] + result
        num = num // base

    return result

print(multiply(10,111,2))
```
