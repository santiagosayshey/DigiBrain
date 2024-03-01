## SOLID Problems

### 1. Single Responsibility Principle (SRP): 
Problem 1: A class handles both database operations and user input validation.
```java
class User {
    function validateInput(input) { // Input validation logic }
    function createUser(data) { // Create a user in the database }
    function deleteUser(id) { // Delete a user from the database }
}
```

#### Solution: 
Create a new a class to handle all input validation and remove from user

Problem 2: A class is responsible for logging and file operations.

Pseudocode:
```java
class FileManager {
    function log(message) {
        // Log a message
    }

    function readFile(filepath) {
        // Read file contents
    }

    function writeFile(filepath, data) {
        // Write data to a file
    }
}
```

#### Solution: 
Remove the log function from filemanager and create a new class to handle documentation, including the logging file.

### 2. Open / Closed Principle
Problem 1: A function that calculates the area of different shapes but requires modifications whenever a new shape is added.
```java
function calculateArea(shape) {
    if (shape.type == "circle") {
        return pi * (shape.radius ^ 2)
    } else if (shape.type == "rectangle") {
        return shape.width * shape.height
    } // Requires modification for a new shape
}
```

#### Solution: 
Create a function in the parent abstract class that can be overriden in each of the derived classes

```java
function calculateArea(shape) {
	shape.getArea(); // this function is overriden in each child class
}
```

Problem 2: A class that handles notifications and needs to be changed whenever a new notification method is added.

Pseudocode:
```java
class Notification {
    function sendNotification(type, message) {
        if (type == "email") {
            // Send email notification
        } else if (type == "sms") {
            // Send SMS notification
        } // Requires modification for a new notification method
    }
}
```

#### Solution: 
Create a notification function for each child class that overrides a base notification function in the parent class

### 3. Liskov Substitution
Problem 1: A `Bird` class is extended by `Penguin` class, but the `fly` method is not applicable to penguins.
```java
class Bird {
    function fly() {// Flying logic }
}
class Penguin extends Bird {
    function fly() { // Penguins cannot fly - LSP violation}
}
```

#### Solution:
Create a fly interface that a derived duck can inherit from

Problem 2: A `Transport` class has a `startEngine` method, but it's not applicable to `Bicycle` subclass.

Pseudocode:
```java
class Transport {
    function startEngine() {
        // Start engine logic
    }
}

class Bicycle extends Transport {
    function startEngine() {
        // Bicycles don't have engines - LSP violation
    }
}
```

#### Solution:
Create an engine interface that a car, NOT bike can inherit from. 

### 4. Interface Segeregation
Problem 1: An interface has multiple methods, but a class only needs to implement a few of them.
```java
interface Vehicle {
    function startEngine()
    function stopEngine()
    function honk()
}
class Bicycle implements Vehicle {
    function startEngine() { // Not applicable for Bicycle }
    function stopEngine() { // Not applicable for Bicycle }
    function honk() { // Honk logic}
}
```

#### Solution: 
Implement an engine interface that handles engine functions

Problem 2: An interface has methods for both reading and writing data, but a class only needs to read data.

Pseudocode:
```java
interface DataHandler {
    function readData()
    function writeData(data)
}

class DataReader implements DataHandler {
    function readData() {
        // Read data logic
    }

    function writeData(data) {
        // Not applicable for DataReader
    }
}
```

#### Solution:
Remove data handler interface and create a new interface for writing data, seperating the two

### 5. Dependency Inversion
Problem 1: A high-level class depends on a low-level class directly, making it difficult to switch to a different implementation.
```java
class Database {
    function saveData(data) { // Save data logic }
}

class UserManager {
    private database
    function UserManager() { this.database = new Database() }
    function saveUserData(data) { this.database.saveData(data) }
}
```

Problem 2: A class depends on a specific email service instead of an interface, making it hard to change the email service.

Pseudocode:
```java
class EmailService {
    function sendEmail(recipient, message) {
        // Send email logic
    }
}

class NotificationManager {
    private emailService

    function NotificationManager() {
        this.emailService = new EmailService()
    }

    function sendEmailNotification(recipient, message) {
        this.emailService.sendEmail(recipient, message)
    }
}
```

#### Solution:
Use an interface for an email service instead of a specific email service and inherit from that

### SOLID Tips:
1.  SRP: Split classes into separate classes that handle only one responsibility.
2.  OCP: Use inheritance and polymorphism to extend the behavior of a class without modifying its code.
3.  LSP: Make sure subclasses can replace their parent classes without affecting the correctness of the program.
4.  ISP: Create smaller interfaces so that classes only need to implement the methods they require.
5.  DIP: Depend on abstractions (interfaces) rather than concrete implementations to make it easier to change components.

## Abstract Data Types

### Implementing an ADT

1.  Stack ADT: Implement a stack with the following methods:

```
push: Add an element to the top of the stack.
pop: Remove and return the top element from the stack.
peek: Return the top element without removing it.
is_empty: Check if the stack is empty.
size: Return the number of elements in the stack.
```

2.  Queue ADT: Implement a queue with the following methods:

```
enqueue: Add an element to the end of the queue.
dequeue: Remove and return the first element from the queue.
front: Return the first element without removing it.
is_empty: Check if the queue is empty.
size: Return the number of elements in the queue.
```

3.  Set ADT: Implement a set with the following methods:

```
add: Add an element to the set.
remove: Remove an element from the set.
contains: Check if an element is in the set.
is_empty: Check if the set is empty.
size: Return the number of elements in the set.
union: Return a new set containing all elements from two sets.
intersection: Return a new set containing the common elements between two sets.
```

### Issues with ADTs

1.  Stack ADT with a non-private helper function: 

```
Problem: The Stack ADT has a non-private helper function called "find_element_position" which should not be exposed to the user. 

Solution: Make the "find_element_position" function private to maintain encapsulation.
```

```cpp
class Stack {
public:
    // Other methods ...

private:
    // Change this method to private
    int find_element_position(int element) {
        // Some logic ...
    }
};
```

2.  Set ADT with duplicate functionality: 

```
Problem: The Set ADT has two separate methods "add" and "insert" which both add an element to the set. 

Solution: Remove one of the methods (preferably "insert") and update all references to use the remaining method.
```

``` cpp
class Set {
public:
    void add(int element) {
        // Add logic ...
    }

    // Remove the insert method
    void insert(int element) {
    //    // Insert logic ...
    //}
};
```

3.  Queue ADT with child class implementing a similar function: 

```
Problem: A child class of the Queue ADT, "PriorityQueue", has a "peek" method similar to the "front" method in the parent class. 

Solution: Remove the "peek" method from the "PriorityQueue" child class and use the "front" method from the parent class instead.
```

```cpp
class Queue {
public:
    int front() {
        // Front logic ...
    }
};

class PriorityQueue : public Queue {
public:
    // Remove the peek method and use the front method from the parent class
    // int peek() {
    //    // Peek logic ...
    //}
};
```

4.  Set ADT with a non-private helper function: 

```
Problem: The Set ADT has a non-private helper function called "find_intersection" which should not be exposed to the user. 

Solution: Make the "find_intersection"
```

```cpp
class Set {
public:
    // Other methods ...

private:
    // Change this method to private
    Set find_intersection(const Set& other) {
        // Some logic ...
    }
};
```

## Recursion Problems

1. Recursive Product: 

```
Function: recursive_product(n, m) 

Example Calls: 
a. recursive_product(5, 6) Expected Output: 30
b. recursive_product(7, 8) Expected Output: 56
```


2. Tail Recursive Product: 
```
Function: tail_recursive_product(n, m, accumulator=1) 

Example Calls: 
a. `tail_recursive_product(5, 6)` Expected Output: `30` 
b. `tail_recursive_product(7, 8)` Expected Output: `56`
```

3. Recursive String Length: 
```
Function: `recursive_strlen(s)` 

Example Calls: 
a. `recursive_strlen("hello")` Expected Output: `5` 
b. `recursive_strlen("abcdef")` Expected Output: `6`
```

4. Tail Recursive String Length: 
```
Function: `tail_recursive_strlen(s, accumulator=0)` 

Example Calls: 
a. `tail_recursive_strlen("hello")` Expected Output: `5` 
b. `tail_recursive_strlen("abcdef")` Expected Output: `6
````

5. Recursive Maximum Value in a List: 
```
Function: `recursive_max(arr)` 

Example Calls: 
a. `recursive_max([1, 2, 3, 4, 5])` Expected Output: `5` 
b. `recursive_max([-10, 0, 20, 8, 7])` Expected Output: `20`
```

6. Tail Recursive Maximum Value in a List: 
```
7. Function: `tail_recursive_max(arr, accumulator=float('-inf'))` 

Example Calls: 
a. `tail_recursive_max([1, 2, 3, 4, 5])` Expected Output: `5` 
b. `tail_recursive_max([-10, 0, 20, 8, 7])` Expected Output: `20
````

7. Recursive Binary Search: 
```
Function: `recursive_binary_search(arr, target)` 

Example Calls: 
a. `recursive_binary_search([1, 3, 5, 7, 9], 5)` Expected Output: `True` 

b. `recursive_binary_search([1, 3, 5, 7, 9], 8)` Expected Output: `False`
```

8. Tail Recursive Binary Search: 
```
Function: `tail_recursive_binary_search(arr, target, low=0, high=None)` 

Example Calls: 
a. `tail_recursive_binary_search([1, 3, 5, 7, 9], 5)` Expected Output: `True` 

b. `tail_recursive_binary_search([1, 3, 5, 7, 9], 8)` Expected Output: `False`
```

9. Recursive Reversing a List: 
```
Function: `recursive_reverse(arr)` 

Example Calls: 
a. `recursive_reverse([1, 2, 3, 4, 5])` Expected Output: `[5, 4, 3, 2, 1]` 

b. `recursive_reverse(["a", "b", "c", "d"])` Expected Output: `["d", "c", "b", "a"]
````

10. Tail Recursive Reversing a List: 
```
Function: `tail_recursive_reverse(arr, accumulator=[])` 

Example Calls: 
a. `tail_recursive_reverse([1, 2, 3, 4, 5])` Expected Output: `[5, 4, 3, 2, 1]` 

b. `tail_recursive_reverse
```

## Quizzes

### SOLID Principles + ADTs


### Recursion

https://myuni.adelaide.edu.au/courses/85254/assignments/333947

yo what the fuck this is a typing test i am tpying on my durgod mechanical keyboard yo wassup my name is sam and this is algorithms and data structures practical exam number 1



