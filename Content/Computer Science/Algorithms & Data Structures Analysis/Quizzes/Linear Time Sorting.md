
> [!exercise]+ Exercise 1
> What is implied by a sorting algorithm having a complexity of $\Theta(n \cdot \log{n})$?
> - The algorithm performs better than any comparison-based sort.
> - The algorithm's complexity varies significantly with input size.
> - The algorithm is non-comparison based.
> - **The algorithm has both the upper and lower bounds of nlogn.**
> 
> **Answer:**
> $\Theta$ indicates a tight bound where a function represents both the upper and lower bound

> [!exercise]+ Exercise 2
> It is claimed that a newly developed comparison-based sorting algorithm, BetaSort, has a worst-case complexity of $\Theta(n \cdot \log{\log{n}})$. Which statement is true?
> - It is optimized for specific cases but adheres to the worst-case upper bound.
> - **The claim violates the established lower bound and is likely incorrect.**
> - Such complexity is achievable for comparison-based sorts with optimizations.
> - BetaSort utilizes a novel comparison technique that defies traditional bounds.
> 
> **Answer:**
> The absolutely worst case comparison based has been proved to run in $\Theta(n \cdot \log{n})$ time. This algorithm is likely incorrect

> [!exercise]+ Exercise 3
> A new sorting algorithm, DeltaSort, claims a worst-case running time better than Ω(nlogn). What can be inferred about DeltaSort?
> - The claim violates the established lower bound and is likely incorrect.
> - DeltaSort applies to all data types.
> - DeltaSort has achieved a new theoretical breakthrough in comparison sorting.
> - **DeltaSort likely uses a non-comparison-based approach.**
> 
> **Answer:**
> Since it's not stated that DeltaSort is explicity a comparison based sorting algorithm, it certainly is possible for it to be faster than the proven lower bound for a comparison based sorting algorithm. 

> [!exercise]+ Exercise 4
> Which of the following best describes Counting Sort?
> - **It is a non-comparison-based, stable sorting algorithm that is not in-place.**
> - It has a time complexity of O(n^2) in the worst case.
> - It consistently outperforms Radix Sort in efficiency for large data sets.
> - It is a comparison-based sorting algorithm with stability.

> [!exercise]+ Exercise 5
> What is the worst-case time complexity of Counting Sort when the range of input values (k) is much larger than the number of elements (n)?
> - $O(n \cdot \log{n})$
> - $O(n)$
> - $O(k)$
> - **$O(n+k)$**
> 
> **Answer:**
> When $k$ is much bigger than $n$, we can say that it dominates $n$ and therefore should be accounted for in the complexity, When it's smaller, we can say it runs in $O(n)$ time.

> [!exercise]+ Exercise 6
> Which of the following is an inherent disadvantage of Counting Sort?
> - It is not a stable sorting algorithm.
> - **It is impractical for sorting floating-point numbers.**
> - It has a linear time complexity.
> - It requires additional space proportional to the number of elements like Quick Sort.
> 
> **Answer:**
> Is only able to sort countable elements. Floating point numbers cannot be counted without an impractically large array to store the counts. It does also require additional space, but this answer is wrong because it says 'like quicksort', but quicksort is in place.

> [!exercise]+ Exercise 7
> If Radix Sort is used to sort n 32-bit integers, how many passes will it make if the chosen base is 256?
> - 8
> - **4**
> - 32
> - 16
> 
> **Answer:** Given that we are sorting 32-bit integers and the chosen base is 256, we need to determine how many 8-bit (since 256 is $2^8$) chunks fit into a 32-bit number.
> 
A 32-bit integer can be broken down into 4 groups of 8 bits, because $32÷8=4$

> [!exercise]+ Exercise 8
> How does the auxiliary space requirement in Radix Sort compare to other sorting algorithms like Quick Sort or Merge Sort?
> - **It is generally higher due to the need of additional arrays.**
> - It is generally lower.
> - It is about the same.
> - It cannot be determined.
> **Answer:**
> Since we are applying counting sort for each digit, we need additional storage for each sub call. This means it will be at least the size of counting sort, but is likely to be higher.

> [!exercise]+ Exercise 9
> Radix Sort can be implemented using Counting Sort as a subroutine. What aspect of counting sort makes it suitable for this?
> - Its O(n) complexity.
> - Its adaptability to different data types.
> - Its inplace sorting capability.
> - **Its stability.**
> 
> **Answer:** 
> Stability is important in radix sort because we sort by the smallest digits first. We need to be able to keep the order of the previous digit sorts when sorting the current digit.

> [!exercise]+ Exercise 10
> A dataset contains 5 million 32-bit integers. Radix Sort is used for sorting. Calculate the theoretical time complexity.
> 1. Using a radix of $2^4$ (base 16) to represent the numbers: Θ(______)
> 2. Using a radix of $2^8$ (base 256) to represent the numbers: Θ(______)
> 3. Using a radix of $2^16$ (base 65,536) to represent the numbers: Θ(______)
> 4. Using Quicksort: $\Theta$(______)
