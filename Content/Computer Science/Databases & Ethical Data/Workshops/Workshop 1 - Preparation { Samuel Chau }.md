These workshop preparation sheets will usually set up between 3-6 questions that we expect you to look at and attempt prior to the workshop session. To avoid people in later workshops getting an advantage, worksheet submissions are due before the first workshop. However, what we're looking at is an attempt on at least some of the questions to get the 1% submission mark. The other 1% comes from workshop participation through the on-line or face-to-face sessions. All of these questions will help you prepare for the exam at the end of the semester. 

This assignment must be submitted as PDF or one of the commons graphics formats. We do not accept Office or LibreOffice and the submission gateway should reject it. We do not accept submissions outside of the digital submission gateway associated with this assignment.

## Question 1

```
You look at a menu which has four first courses, three main courses, and two desserts. If a meal has one of each course, how many possible different meals could you make from this menu?
```

Multiply each of the options together:

$$ 4 \cdot 3 \cdot 2 = 24 $$

## Question 2

```
Relational databases define tables, sets of variables, and the relationships between them. Sometimes we want to associate a variable directly with a given table, sometimes we want to use a relationship.

Think about a table called PeopleIDs, which contains "ID number, Name, Age". You are asked to store the height of the People listed in the PeopleID table. Is this better stored as a new variable (column) inside PeopleIDs or in a table called PeopleHeights that is linked back to PeopleIDs? Justify your thinking with examples. (Hint: think about children.)
```

Since height is not a static number - it changes as we get older, it makes more sense to create a new table specific to heights and create a new column to associate with a person’s id and their age at a specific time. If we were to store the heights for say, people only over 18, then it would be beneficial to store heights directly in the peopleID table as there would be no situation where that data would need to be changed

## Question 3

```
How do you generate random numbers in Python? How random are these numbers? Is there more than one way to generate these numbers?
```

In python, we can import the random module and use the random object to generate random numbers.

```python
import random

print(random.random())
```

Can also print a random number within a range:

```python
import random

print(random.randint(1,10))
```

Can also print from a pre defined array, floats, etc


## Question 4

```
Without just copying them from the Internet, think about what the terms "morals" and "ethics" mean and write down definitions in your own words. (This is worth almost zero marks in the grand scheme so go with what's in your head!)
```

Both are very similar and touch on the idea of wrong vs right. Morals are the ideas that individuals strive to follow and define the type of person that they want to be. Ethics, on the other hand, are agreed upon rules that the collective have decided are right. 

## Question 5

```
Write a Python program that uses a random number generator to "flip" a fair coin and achieve an outcome of "heads" or "tails. Your program should prompt for an integer, which is then used to run your flipper that many times, count how many heads and tails occurred and summarise the results.

Eg
How many iterations: 1000  
Running 1000 iterations  
Finished  
Heads: 503 (50.30%)  
Tails: 497 (49.70%)


Run your code several times with different iterations. How many iterations do you need to get 50.04%/49.96% ratios reliably? (Reliably should be read as "at least 9 times out of 10".)
```

```python
import random


flips = int(input("How many iterations: "))
print("Running " + str(flips) + " iterations")

  

heads=tails=0

for i in range(flips):
    throw = random.randint(1,2)
    
    if throw == 1:
        heads += 1
    else:
        tails += 1

print("Heads: " + str(heads) + " (" + format((heads/flips)*100, '.2f') + "%)")
print("Tails: " + str(tails) + " (" + format((tails/flips)*100, '.2f') + "%)")
```


This number should get more reliable as the number of flips gets larger and larger, but I'm unsure of how to quantify this. 

## Question 6

```
You are playing a guessing game with a friend where one of you picks a letter of the English alphabet and the other has to guess it. The chances of your friend picking one letter is the same as picking any other. However you choose to ask the question, your friend will answer "Yes/No" (truthfully)!
```

### Q6.1 

```
How much information is conveyed by each answer?
```

Recall:

![[docs/Computer Science/Databases & Ethical Data/Definitions/Entropy]]

Where, entropy is expressed as:
$$  H(X) = - \sum_{i=1}^{n} P(x_i) \cdot \log_b P(x_i) $$
Since there is a 1/2 chance that each answer is selected, we can say:

$$  H(X) = - 2(\frac{1}{2} \cdot \log_2 \frac{1}{2}) = 1\,bit  $$

This means that there is **1 bit of information for each answer**

### Q6.2 

```
Given your answer to 6.1, what is the maximum number of questions you should be able to find that letter, if you construct your questions carefully. (Hint: start with entropy.)
```

Recall:
$$  H(X) = - \sum_{i=1}^{n} P(x_i) \cdot \log_b P(x_i) $$
Since there are 26 letters in the alphabet and each guess constitues a 1/26 chance, we can say:

$$  H(X) = - 26(\frac{1}{26} \cdot \log_2 \frac{1}{26}) \approx 4.7 \,bits  $$

- This means it would take roughly 4.7 bits of information to guess the right answer, meaning that it would take at most 5 questions ( if you construct your questions properly ) to guess the right letter. 


### Q6.3 

```
How did you construct the questions?
```

We could use a binary search method to halve the sample size each question. 

```
Guess: F
1.  Is the letter between A-M? *yes*
2.  Is the letter between A-G? *yes*
3.  Is the letter between A-D? *no*
4.  Is the letter 'E'? *no*
5.  Is the letter 'F'? *yes*
```

