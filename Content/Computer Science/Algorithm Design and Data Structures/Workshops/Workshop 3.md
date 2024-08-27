1. Find the tight bound complexity of the following functions. 

a. 
```
(a) f(n) = 64n 
(b) f(n) = 1000000 
(c) f(n) = 3n^2logn + 6n + 100000 
(d) f(x) = 5x^3 + logx + 66 
(e) f(n) = 10log^2 n + 2n 
(f) f(n,m) = 9n^2 + 99m + c
```

```
(a) O(n)
(b) O(1)
(c) n^2*log(n)
(d) O(x^3)
(e) O(n)
(f) O(n^2+m)
```

b. 
```
-   3/n
-   6
-   n
-   sqrt(n)
-   nloglogn
-   nlogn
-   n^1.5
-   n^2
-   n^3
-   2^n
```

2.

a. 
```cpp
int getHandshakes(int n){
    int handshakes = 0;
    for (int i = 0; i < n; i++){
        for (int j = i+1; j < n; j++){
            handshakes++;
        }
    }
    return handshakes;
}
```

O(n^2)

b. 
```cpp
int getEvenIndexSum (int array[], int size){
    int sum = 0;
    for (int i = 0; i < size; i+=2){
        sum += array[i];
    }
    return sum;
}
```

O(n)

c.
```cpp
void getPowers (int number) {
    for (int i = 1; i < number; i=i*2){
        cout << i << ", ";
    }
}
```

O(log(n))

Challenge:

n and cos(n) or sin(n)

explanation:
Here, f(n) is a linear function and g(n) is a periodic function that oscillates between -1 and 1. As n increases, the value of sin(n) oscillates between -1 and 1, but does not increase or decrease in a monotonic way. Therefore, there is no constant c such that f(n) <= c_g(n) for all sufficiently large values of n, nor is there a constant c such that g(n) <= c_f(n) for all sufficiently large values of n.
