
> [!idea]+ Idea
> Order statistics tell us the position of an element in a set relative to other elements. The $i'th$ order statistic in a set of $n$ elements is the $i'th$ smallest element.
> - The minimum element is the $1st$ order statistic
> - The maximum element is the $n'th$ order statistic
> - The median is the $n/2'th$ order statistic. If n is even, there are 2 medians

> [!consider] Min / Max
> 
> - How many comparisons are needed to find the minimum element in a set? The maximum? We need $n-1$ comparisons at $O(n)$ in the worst case
> - Can we simultaneously find the minimum and maximum with less than twice the cost?
> - Yes:
>   - Walk through elements by pairs
>     - Compare each element in pair to the other
>     - Compare the largest to maximum, smallest to minimum
>   - Total cost: 3 comparisons per 2 elements = $O(\frac{3n}{2})$
> 
> **Example:**
> Let's find the minimum and maximum in the set: [5, 2, 9, 1, 7, 4]
> 
> Normal Approach:
> - Find minimum: Compare 5 to 2, 2 to 9, 2 to 1, 1 to 7, 1 to 4. Minimum is 1. (5 comparisons)
> - Find maximum: Compare 5 to 2, 5 to 9, 9 to 1, 9 to 7, 9 to 4. Maximum is 9. (5 comparisons)
> - Total comparisons: 5 + 5 = 10
> 
> Simultaneous Min/Max Approach:
> - Compare pairs: (5, 2), (9, 1), (7, 4)
>   - 5 > 2, 9 > 1, 7 > 4
> - Compare larger elements to current max: 5 < 9, 9 > 7. Maximum is 9.
> - Compare smaller elements to current min: 2 > 1, 1 < 4. Minimum is 1.
> - Total comparisons: 3 (pairs) + 2 (max) + 2 (min) = 7


