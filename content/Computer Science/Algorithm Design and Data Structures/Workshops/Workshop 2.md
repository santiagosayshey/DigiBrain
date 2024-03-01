### General Instructions

In this workshop you will be comparing ADTs and practicing writing recursive functions.

You can prepare for this workshop by reviewing the tail recursion code (see week 3 lectures 1, 2 and 3 in Echo 360 and selected solutions in week 3 lecture tab.) [](https://myuni.adelaide.edu.au/courses/85254/files/12528302?wrap=1 "workshop1.cpp")

Your workshop tutor will assist you with any questions and if you need guidance while undertaking the group work during your session.  Post any questions outside of the session time to Piazza.

### Group work (15-20 minutes followed by discussion) - Selecting Abstract Data Types

Form into groups of 4-5.

In the last lecture, we used memoisation to reduce the number of recursive calls made to calculate the Fibonacci number by storing and reusing values that had been calculated instead of calculating them multiple times [fib-dynamic.cpp](https://myuni.adelaide.edu.au/courses/85254/files/12645843?wrap=1 "fib-dynamic.cpp")[](https://myuni.adelaide.edu.au/courses/85254/files/12645843/download?download_frd=1)

[Download fib-dynamic.cpp](https://myuni.adelaide.edu.au/courses/85254/files/12645843/download?download_frd=1).  Implementing this required us to store the values as we calculated them.

There are many containers that we could have chosen [https://cplusplus.com/reference/stl/](https://cplusplus.com/reference/stl/)

[Links to an external site.](https://cplusplus.com/reference/stl/)

As a group, consider the use of Vector, Array, Map and Unordered_Map:

1.  Are there any aspects of the ADT that make it unsuitable to our problem?
3.  Are there any aspects of the ADT that make it suitable to our problem?
4.  How would your answers change, if at all, for the Truckloads problem?

#### Vector
- Can dynamically increase the size of a 
#### Array
1. / 2. Can't dynamically increase the size of a c++ array, therefore only suitable for pre determined tabular values

#### Map
1. cant think of any
2. Can start the iterator from the current fib value as it only needs to find values under the current fib call
3. Same a

#### Unordered Map
1. Would have to start iterating from the start of each map


### Group Work (15 minute Recursive Thinking Challenge)

Write head and tail recursive versions of as many of the problems as you can within 15 minutes

Post solutions at front of room when finished.  1 point for each correct solution, -1 mark for each incorrect (so check with your group before posting!)

If you finish the recursions, how many can you write iterative (using loops instead of recursion) for?  1/2 point for each iterative solution.

Questions will be given out at the start of this challenge.

### Marking Scheme

The workshop is worth 1% of your final mark.


```cpp
numInString(std::string, int i=0) {
	if (string[i] == ascii number)
		return string[i]

	return numInString(std::string, i+1);
}
```

