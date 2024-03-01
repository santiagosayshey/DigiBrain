## Linux Basics

### Multiple Choice Questions

1.  What is the function of `chmod -[permission type] [file]` in Unix?
    -   A) Changes the ownership of a file
    **-   B) Changes the permissions of a file**
    -   C) Changes the location of a file
    -   D) Changes the size of a file

1.  What does the `cd` command do in Unix?
    -   A) It creates a directory
    **-   B) It changes the current directory**
    -   C) It checks the size of a directory
    -   D) It deletes a directory

1.  In the context of Unix, what does the kernel do?
    -   A) It provides a graphical user interface for users
    **-   B) It manages files, users, devices, and processes**
    -   C) It stores files and directories
    -   D) It is the command-line interpreter

### Short Answer Questions

4.  Explain the role of an Operating System in the context of Unix.

Low level software that interfaces programs and devices

1.  Describe the concept of file permissions in Unix and how they can be manipulated

Files have the ability to be read, written and executed. Users inside an operating system have permissions to do each of these things to files. File persmissions can be changed using the `chmod` function

### Coding Questions

6.  Write a Unix command to change the permissions of a file named `testfile.txt` to read and write for the user, read for the group, and no permissions for others.

```bash
chmod u=rw g=r o= textfile.txt
```

## Bash Basics

### Multiple Choice Questions

7.  How are arguments accessed in Bash scripts?
    
    -   A) `$a`, `$b`, etc.
    -   **B) `$1`, `$2`, etc.**
    -   C) `$@`, `$#`, etc.
    -   D) `$0`, `$1`, etc. - $0 is the file itself
8.  Which Bash loop continues execution until a certain condition is true?
    
    -   A) For loop
    -   B) While loop
    -   **C) Until loop**
    -   D) Do loop
9.  What is the output of the following command `val=$[5 + 5]; echo "Value: $val"`?
    
    -   A) Value: 5 + 5
    -   **B) Value: 10**
    -   C) 5 + 5
    -   D) 10

### Short Answer Questions

10.  Explain what the `#!/bin/bash` line does in a Bash script.

Is a shebang that tells the file to execute the commands using bash

1.  Describe how to use the `shift` command in the context of Bash script arguments.

Deletes the front most argument in the argument list, and shifts the other arguments to the front by 1

i.e. $2 becomes $1, etc


### Coding Questions

12.  Write a Bash script that loops over the numbers 1 to 5, printing each number to the console.

```bash
for i in {1..5}
do
	echo $i
done
```


## Bash Variables

### Multiple Choice Questions

13.  How can you access all the elements of an array `arr` in Bash?

-   A) `arr[]`
-   B) `arr`
-   C) **`${arr[@]}`**
-   D) `${arr}`

14.  What is the output of the following command `var="quack"; echo '$var$var'`?

-   **A) $var$var**
-   B) quackquack
-   C) quack$var
-   D) $quackquack

15.  What command is used to make a variable accessible from other scripts?

-   A) `echo`
-   B) `source`
-   **C) `export`**
-   D) `declare`

### Short Answer Questions

16.  Explain the difference between single and double quotes in Bash.
17.  Describe how arrays are defined and accessed in Bash.

### Coding Questions

18.  Write a Bash script that creates an array of numbers from 1 to 5 and prints the third element of the array.


## Bash Expansion

### Multiple Choice Questions

19.  What does the wildcard `*` do in Bash?

-   A) Matches exactly one character
-   B) **Matches any number of any characters**
-   C) Matches any number of digits
-   D) Matches any single digit

20.  What does `${#var}` return in Bash?

-   A) The value of the variable 'var'
-   B) The number of items in the array 'var'
-   **C) The length of the value of the variable 'var'**
-   D) The first character of the value of the variable 'var'

21.  In Bash, what is the result of the following command `echo ${USER:-root}` if the variable USER is unset?

-   A) An error message
-   B) Empty output
-   **C) The string 'root'**
-   D) The string 'USER'

### Short Answer Questions

22.  Explain what brace expansion is in Bash and provide an example.

Used to glob things together or to iterate over in loops.

{a..z}.txt is all files with a up to z as a txt file

1.  Describe how to use command substitution in Bash and give an example.

$(command goes here)

### Coding Questions

24.  Write a Bash command that creates a list of file names test1.txt, test2.txt, test3.txt using brace expansion.

```bash
touch test{1..3}.txt
```

## Bash Control Structures

### Multiple Choice Questions

25.  In a Bash script, how do you perform an action only if a command succeeds?

-   **A) Using the `&&` operator**
-   B) Using the `||` operator
-   C) Using the `==` operator
-   D) Using the `!=` operator

26.  What is the function of the `break` command in a Bash loop?

-   A) It causes the script to exit
-   B) It causes the current iteration of the loop to skip
-   **C) It causes the loop to terminate immediately**
-   D) It causes the loop to start over

27.  What does the `case` construct do in Bash?

-   A) It checks for file existence
-   **B) It tests a variable against different patterns**
-   C) It tests a variable for null or zero value
-   D) It repeats a block of commands a specified number of times

### Short Answer Questions

28.  Explain the difference between `if [ "$a" = "$b" ]` and `if [[ "$a" = "$b" ]]` in Bash.
29.  Describe how to use a for loop in Bash.

There are many ways to use a for loop in bash

```bash
for i in 1 2 3 4 5
do
	...
done

for i in {1..2}
do
	...
done
```

### Coding Questions

30.  Write a Bash script that prints "Hello, World!" if the variable greeting is set to "Hello", otherwise it prints "Goodbye, World!".

```bash
if [[ $greeting == "Hello"]]
then
	echo "Hello, World"
else
	echo "Goodbye, World"
fi
```


## Functions and Subshells

### Multiple Choice Questions

1.  What does `a=$(ls)` do in Bash?
    
    -   A) Assigns the output of `ls` to variable `a`
    -   B) Runs the `ls` command in a subshell
    -   **C) Both A and B**
    -   D) Neither A nor B
2.  What is the difference between functions in Bash and C++?
    
    -   **A) Bash functions return the entire output, while C++ functions return a specific value**
    -   B) C++ functions return the entire output, while Bash functions return a specific value
    -   C) Both Bash and C++ functions return the entire output
    -   D) Both Bash and C++ functions return a specific value
3.  In Bash, what does `exit 1` indicate?
    
    -   A) Successful execution
    -   **B) An error occurred**
    -   C) The script is continuing to the next command
    -   D) The script is restarting

### Short Answer Questions

4.  What is the role of the `$?` variable in Bash?
5.  How does the concept of success and failure in Bash differ from that in C/C++?
6.  What is a subshell in Bash, and how does it handle variable scope?

### Coding Questions

7.  Write a Bash function that uses local variables and returns the output of a command.
8.  Write a Bash script that demonstrates the use of subshells and their effect on variable scope.

## C Basics

### Multiple Choice Questions

9.  How are booleans typically represented in C?
    
    -   A) Using `int` or a boolean library, with non-zero values interpreted as true
    -   B) Using a dedicated boolean data type, with `true` and `false` as possible values
    -   C) Using `char`, with 'T' and 'F' representing true and false respectively
    -   D) Using `string`, with "true" and "false" as possible values
10.  What is casting in C++?
    

-   A) Changing the value of a variable
-   B) Changing the data type of a variable
-   C) Changing the scope of a variable
-   D) Changing the lifetime of a variable

### Short Answer Questions

11.  What's the difference between C and C++ in terms of semantics and structure?
12.  What is the purpose of memory allocation in C and how does it differ from C++?

### Coding Questions

13.  Write a C function that uses casting to convert a float to an integer.
14.  Write a C program that demonstrates the use of `malloc`, `calloc`, `realloc`, and `free`.

## C I/O

### Multiple Choice Questions

15.  What is the role of static variables in C?

-   A) They keep their value across multiple function calls
-   B) They are only initialized once
-   C) Both A and B
-   D) Neither A nor B

16.  How does the `scanf` function work in C?

-   A) It's used for output
-   B) It's used for input
-   C) It's used for opening files
-   D) It's used for closing files

### Short Answer Questions

17.  How do function arguments work in C, and what's the difference between pass by copy and pass by pointer?
18.  What are static functions in C and when should they be used?

### Coding Questions

19.  Write a C program that demonstrates the use of static variables and static functions.
20.  Write a C program that asks for user input using `scanf` and prints it out using `printf`. Also write a C program that performs file I/O operations.

## Memory & Inodes

### Multiple Choice Questions

1.  In C, how is a string concatenation achieved?
    
    -   A) `strcat(string1, string2)`
    -   B) `strcpy(string1, string2)`
    -   C) `string1 + string2`
    -   D) `string1.concat(string2)`
2.  What is an inode in the context of Unix filesystems?
    
    -   A) A specific file
    -   B) A type of error
    -   C) A data structure that stores file information
    -   D) A command to navigate directories

### Short Answer Questions

3.  Explain the difference between the stack and the heap in the context of function calls.
4.  How can variables persist after returning from a function in C?

### Coding Questions

5.  Write a C function that uses dynamic memory allocation to create a new integer, assign it a value, and return its address.
6.  Demonstrate using string functions in C to concatenate two strings.

## Processes

### Multiple Choice Questions

7.  In Unix, which command is used to view current processes?
    
    -   A) `ls`
    -   B) `ps`
    -   C) `cd`
    -   D) `mv`
8.  What is the difference between a program and a process?
    
    -   A) There is no difference; the terms are interchangeable
    -   B) A program is a series of instructions, a process is the execution of those instructions
    -   C) A process is a series of instructions, a program is the execution of those instructions
    -   D) A program can be paused, while a process cannot

### Short Answer Questions

9.  Explain the concept of forking and how it is used in Unix systems.
10.  How can Unix commands be executed within a C program?

### Coding Questions

11.  Write a C program that executes a Unix command using the `system` command.
12.  Write a C program that forks a process and executes a different Unix command in each process.

## Redirection

### Multiple Choice Questions

13.  What does the `dup2` function do in C?
    
    -   A) Duplicates a file
    -   B) Duplicates a file descriptor
    -   C) Duplicates a function
    -   D) Duplicates a string
14.  What is a file descriptor in Unix-like systems?
    
    -   A) A label for a file
    -   B) An identifier for a file for a process
    -   C) A type of file error
    -   D) A command to find a file

### Short Answer Questions

15.  What is redirection and how is it used in Unix systems?
16.  How is redirection implemented in C?

### Coding Questions

17.  Write a C program that reads from standard input and prints it out, then closes the standard input stream and reads from a file.
18.  Write a C program that redirects the output of a Unix command to a file.

## Pipes & Redirection

### Multiple Choice Questions

19.  In Unix-like systems, what is the function of the `|` symbol?
    
-   A) It connects two commands, piping the output of the first as the input to the second
-   B) It redirects the output of a command to a file
-   C) It indicates the beginning of a function
-   D) It indicates a logical OR operation
1.  What is a pipe in C?
    
-   A) A connector between two functions
-   B) A way of linking two variables
-   C) A buffer to hold data between program executions
-   D) A tool for error checking

### Short Answer Questions

21.  How are pipes implemented in C?
22.  What are the restrictions of pipes?

### Coding Questions

23.  Write a C program that replicates the `ls | wc` command from Bash using `fork()` and `pipe()` system calls.
24.  Write a C program that creates a pipe and uses it for communication between two processes.