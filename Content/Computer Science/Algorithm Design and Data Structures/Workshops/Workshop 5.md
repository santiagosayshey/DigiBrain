### Preparatory work

1.  What are the fundamental differences between a stack and a queue? How does their internal structure affect their functionality and the order in which elements are accessed?

```
Stacks: Operate in Last in, First Out, element operations occur at the top end (push, pop)

Queues: Operate in First in, First Out, element operations occur at both ends (enqueue pushes to back, dequeue removes from front)
```


1.  How can you implement a queue data structure using a doubly linked list? Is there an advantage to using a doubly linked list rather than a singly linked list?

```
Each node has a pointer to the node in front and behind it, where the head contains pointers to the first and last elements in the list. This allows for O(1) complexity to access both the front and end of the list, meaning that enqeue and dequeue can be done in O(1) time. In  a singly linked list, only 1 end can be accessed in O(1) time and therefore either, insert or delete must be done in O(n). This would be better to suited to a stack (whose operations occur at the same top end)

Works with a singly linked list if the head contains a pointer to the last element (tail)
O(1) time complexity if inserting to the back, deleting from the front
```

1.  Can a Red-Black Tree contain only red nodes? Why or why not?

```
No. The root must always be black. If a node is red, then both of it's children are black. 
```

### Group work (20 minutes followed by discussion) - Stacks and queues

Form into groups of 4-5.

1.  Explain how you can simulate a queue using two stacks. Provide a step-by-step process for enqueue and dequeue operations and analyse the time complexity of each operation. **(10 minutes to design solution)**

```pseudocode
Initialize: 
StackNewestOnTop
StackOldestOnTop 

Function enqueue(element):                                                 // O(1)
    Push the new element onto StackNewestOnTop

Function dequeue():                                                        // O(n)
    If StackOldestOnTop is empty: {
         While StackNewestOnTop is not empty: {
			Pop an element from StackNewestOnTop
            Push this element onto StackOldestOnTop
        }   
    }
    Pop and return the top element from StackOldestOnTop
```

```cpp
#include <stack>
#include <iostream>

class Queue {
private:
    std::stack<int> StackNewestOnTop, StackOldestOnTop;

public:
    void enqueue(int value) {
        StackNewestOnTop.push(value);
    }

    void dequeue() {
        // If StackOldestOnTop is empty, move elements from StackNewestOnTop
        if(StackOldestOnTop.empty()) {
            while(!StackNewestOnTop.empty()) {
                StackOldestOnTop.push(StackNewestOnTop.top());
                StackNewestOnTop.pop();
            }
        }
        // Pop the top element from StackOldestOnTop
        if(!StackOldestOnTop.empty()) {
            StackOldestOnTop.pop();
        }
    }
};
```

2. Consider a scenario where you need to design a stack data structure that supports constant time complexity for push, pop, and finding the minimum element (finding does not remove the element). Discuss how you can achieve such a structure efficiently. Analyse the time complexity of each operation and discuss any limitations or trade-offs involved. **(10 minutes to design solution)**


```
Employ a secondary stack that keeps track of the minimum element
    
Push Operation:
- Push the element onto the main stack (mainStack).
- If the minStack is empty or the top element of minStack is greater than the new element, push the new element onto minStack.
    
Pop Operation:
- Pop the element from mainStack.
- If the popped value == the minStack.front(), pop the element from minStack
    
Min Operation:
- Return the top element of minStack, which represents the current minimum of the stack.
    
Time Complexity:
- Push Operation: O(1), as we are just pushing elements onto the stacks.
- Pop Operation: O(1), as we are just popping off the top elements of the stacks.
- Min Operation: O(1), as we are just looking at the top element of minStack.
    
Trade-offs:
- Constant time complexity for each pop, push and min
- Increase space complexity to store two seperate stacks
```

### Group work (15 minutes followed by discussion) - Understanding Trees

Consider the following tasks. Discuss and decide which tree traversal will best fit each task.  Be ready to explain your reasoning:

1.  In the tree destructor, we want to delete each of the nodes that we created.  We need to be careful not to leave any dangling pointers (memory where we no longer have any reference to that memory).

```
Post Order

Ensures that child nodes are deleted before their preceding parent nodes
```

1.  We want to copy a tree to another tree.

```
Pre Order

Ensures that the natural order of the original tree is kept intact without needing to balance it
```

1.  We want to list all of the node values of a binary search tree in increasing order.

```
In Order

First visits the left subtree (all elements smaller than the root), then the root itself, and finally the right subtree (all elements larger than the root), which yields the node values in ascending order.
```

1.  We are using a binary tree to represent a mathematical equation, where leaf nodes are operands and non-leaf nodes are operators.  For example, the mathematical operation: 5 + 2 * 3 is represented as:

```
wut
```

