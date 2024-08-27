### Group work

### Q1 - (10 minutes followed by discussion) - Practical 9 design

1.  What information was stored and what data structures were used by people on your table?
2.  Why were those structures chosen?

```
3 Unordered Maps

documents (KEY: string (name), document d(custom object))
name2id (KEY: int id, string name)
patrons (KEY: int id)

name2id used to provide O(1) complexity for borrow and return
patrons not nessecary, only useful for checking validity of borrow / return
documents provides O(1) complexity for search
```

### Q2 - (5-10 minutes)

ChatGPT made to [following suggestion](https://myuni.adelaide.edu.au/courses/85254/pages/chat-gpts-design-for-prac-9 "Chat GPT's design for prac 9") for the design of prac 9.  Evaluate the accuracy and precision of ChatGPT's justification of its choices.  How would you improve on the answer?

```
no constant way to implement search using these data structures, as none use the name as their key. 
Good use of unordered set for patrons, I should have done this. 

I would combine the 1st and 3rd data structures by creating a Document object to store as the foreign key (which itself stores name, copies, limit, etc)

Also add another data structure that keeps track of name as a key with id as a foreign key for constant search time
```

### Q3 - (5-10 minutes)

On reflection, what do you think is the best design and why?

### Q4 (5-10 minutes)

Problem 1: You have the problem of converting between prefix and postfix notation.  You have seen this done with both a stack and a binary expression tree.  (tutor can review these options for you if requested).  Which structure would you choose for this problem and why?

```
stack

operators can be moved from one end to the other in constant time using a stack as (last in first out). or (last operator becomes first operator)
```

Problem 2: You want to implement a spell checker.  What data structure would you choose and why?

```
trie

each path from the root to an end node in a trie represents a word, therefore we can efficiently check if a word exists. We cross check if a word exists within the trie and underline if it does not exist.
```

Problem 3: All of the data structures we studied in the course were ordered.  If unordered maps and sets were not available, what containers would you have chosen for prac 9?  What are the underlying data structures that implement those containers?

```
red black tree

logn time complexity for insertion, deletion and search
```

