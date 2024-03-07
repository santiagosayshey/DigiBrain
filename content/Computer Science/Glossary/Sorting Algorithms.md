> [!idea]+ Idea
> Sorting algorithms take raw data and order it following specific rules, enhancing searchability and analysis. This is extremely useful for optimizing tasks such as database querying and algorithm performance. We rank them based on complexity—using Big O notation—to help us select the appropriate algorithm for the task's time and space constraints.

| Method                 | Algorithm                              | Worst-case Time Complexity | Average-case Time Complexity | Best-case Time Complexity | Space Complexity | Stableness                         |
| ---------------------- | -------------------------------------- | -------------------------- | ---------------------------- | ------------------------- | ---------------- | ---------------------------------- |
| Comparison + Iterative | [[6.2 Bubble Sort\|Bubble Sort]]       | $O(n^2)$                   | $O(n^2)$                     | $O(n)$                    | $O(1)$           | Stable                             |
|                        | [[6.3 Selection Sort\|Selection Sort]] | $O(n^2)$                   | $O(n^2)$                     | $O(n^2)$                  | $O(1)$           | Not stable, but can be made stable |
|                        | [[6.1 Insertion Sort\|Insertion Sort]] | $O(n \log n)$              | $O(n \log n)$                | $O(n \log n)$             | $O(n)$           | Stable                             |
|                        | [[6.5 Quick Sort\|Quick Sort]]         | $O(n^2)$                   | $O(n \log n)$                | $O(n \log n)$             | $O(\log n)$      | Not stable                         |
|                        | [[6.4 Merge Sort\|Merge Sort]]         | $O(n^2)$                   | $O(n^2)$                     | $O(n)$                    | $O(1)$           | Stable                             |
|                        | [[3.3 Radix Sort\|Radix Sort]]         | $O(n+k)$                   | $O(n+k)$                     | $O(n+k)$                  | $O(k)$           | Stable                             |
|                        | [[3.2 Counting Sort\|Counting Sort]]   | $O(nk)$                    | $O(nk)$                      | $O(nk)$                   | $O(n+k)$         | Stable                             |
