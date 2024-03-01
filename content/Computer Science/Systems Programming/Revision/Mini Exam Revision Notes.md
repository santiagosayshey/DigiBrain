## Linux Basics

### Operating Systems / UNIX
-   OS: Low-level software interfacing programs and devices.
-   UNIX: All elements treated as files - files, directories, executables, devices.

### Navigation
-   UNIX uses forward slashes.
-   `cd` is used to navigate directories.

### File Permissions
-   User IDs determine file access.
-   Three types: read, write, execute.
-   Permissions can be changed using `chmod -[permission type] [file]`.

### The Kernel
-   Central part of the OS, it interfaces the CPU, memory, peripherals with applications.
-   Manages files, users, devices, and processes

## Bash Basics

### Bash Scripting

-   `touch my_script.sh`: Creates a new file named "my_script.sh".
-   `chmod +x my_script.sh`: Adds execute permissions to "my_script.sh".
-   `#!/bin/bash`: Shebang line that tells the system to interpret the script using Bash.
-   `echo "Howdy World"`: Print "Howdy World" to the console.
-   `./my_script.sh`: Executes the script "my_script.sh".

### Bash Script Arguments

-   Arguments can be accessed in scripts via `$1`, `$2`, etc.
-   `$#`: Returns the number of arguments.
-   `$0`: Returns the name of the script.
-   `$@`: Returns all arguments.
-   `shift`: Shifts arguments, removing the first argument and moving the others forward.

### Debugging in Bash

-   Run Bash in explicit mode with `-x` flag for debugging.
-   Explicit mode prints each executed command before its output.

### Loops

#### For Loop
The for loop is used to perform a command or series of commands for each item in a list.

```bash
# Loop over a static list of items 
for i in 1 2 3 4 5 
do    
	echo "Number: $i" 
done  

# Loop over a range
for i in {1..5} 
do    
	echo "Number: $i" 
done  

# Loop over output of a command (command substitution) 
for file in $(ls) 
do    
	echo "File: $file" 
done
```

#### While Loop
The while loop is used to perform a command or series of commands as long as a certain condition is true.

```bash
count=1
while [ $count -le 5 ]
do
   echo "Count: $count"
   count=$((count + 1))
done
```

#### Until Loop
The until loop is used to perform a command or series of commands until a certain condition is true.

```bash
count=1
until [ $count -gt 5 ]
do
   echo "Count: $count"
   count=$((count + 1))
done

```

### Bracket Notation

#### Command Substitution `$()`
This is used when you want to use the output of a command as an argument to another command.

```bash
for file in $(ls)
do
    echo "File: $file"
done

```

#### Arithmetic Operations `$[]` or `$(( ))`
This is used when you want to perform arithmetic operations.

```bash
# Using $[]
val=$[5 + 5]
echo "Value: $val"  # Outputs: Value: 10

# Using $(())
val=$((5 * 5))
echo "Value: $val"  # Outputs: Value: 25

````

#### Condition Testing `[]` or `[[]]`
This is used for conditional expressions.

```bash
# Using []
if [ "$a" -gt "$b" ]; then
    echo "$a is greater than $b"
fi

# Using [[]]
if [[ "$a" == "$b" ]]; then
    echo "$a is equal to $b"
fi

```


In Bash scripting, `[[]]` is more modern and powerful than `[]`. For instance, it supports string comparison with `==`, `!=`, `<`, and `>` using lexicographic order.

![[docs/Images/Pasted image 20230306212611.png]]

## Bash Variables

### Variables in Bash
-   Variables are defined without whitespace, e.g., `a=1` (correct), `a = 1` (incorrect).
-   Bash is not strictly typed, meaning any type can be assigned to any variable without defining its type first.

```bash
x="Hello World"
y=25
z=3.14
```

### Strings in Bash

-   Whitespace is only allowed within the string itself.
-   Strings can be defined using single or double quotes.
-   `echo` command will print exactly what is inside single quotes without interpreting it.

```bash
string='Hello, World!'
echo $string   # This will print: Hello, World!
var="quack"
echo '$var$var' # This will print: $var$var
echo $var$var # This will print: quackquack
```

### Arrays in Bash
-   Arrays are defined inside round brackets `()`, with each element separated by a space.
-   Access values using index notation, e.g., `b=${a[0]}` assigns the first element of array 'a' to variable 'b'.

```bash
array=( A B C D E F G )
echo ${array[0]}   # This will print: A
echo ${array[2]}   # This will print: C
```

- Several operations are available for arrays such as:
	- Getting all elements (`${arr[@]}`)
	- Getting array indices (`${!arr[@]}`)
	- Getting array length (`${#arr[@]}`)
	- Appending value (`a+=(value)`)
	- Accessing a range of values (`${a[@]:i:j}`).

```bash
echo ${array[@]}  # This will print: A B C D E F G
echo ${!array[@]}  # This will print: 0 1 2 3 4 5 6
echo ${#array[@]}  # This will print: 7
array+=(H)
echo ${array[@]}  # This will print: A B C D E F G H
echo ${array[@]:2:4}  # This will print: C D E F
```

### Exporting Variables in Bash
-   Use `export` command to make a variable accessible from other scripts.
-   For example, in `script1.sh` you define `a=5` and `export a`. Then in `script2.sh`, you can `echo $a` to print the value of 'a'.

```bash
# script1.sh
a=5
export a
./script2.sh  

# script2.sh
echo $a  # This will print: 5
```

### Pipes in Bash
-   The `|` operator can be used to pipe the output of one command into another, e.g., `ls | wc -l`.

```bash
ls | wc -l  # This will print the number of files in the current directory
```

### Here Strings in Bash

-   Here strings are used to pass the output of a command into another using `<<<`, e.g., `cat <<< $(ls)`.
-   Combined with the `read` function, they can be used to parse the output of a command into separate variables, e.g., `read lines words chars filename <<< $(wc test_input.txt)`.

```bash
cat <<< $(ls)  # This will print the list of files in the current directory

# Assuming test_input.txt contains: This is a test
read lines words chars filename <<< $(wc test_input.txt)
echo $lines   # Prints the number of lines 
echo $words   # Prints the number of words 
echo $chars   # Prints the number of characters 
echo $filename  # Prints the filename
```

## Bash Expansion

### Globbing
-   Globbing is a feature that allows grouping items together, often used for managing files in batch operations. It simplifies searching and sorting tasks.

#### Wild Card *
-   `*` is a wildcard that can match any sequence of characters in filenames.

```bash
ls *.txt        # Lists files that end with '.txt'
ls *a*.txt      # Lists files that contain 'a' in their names and end with '.txt'
rm *            # Deletes every file in the current directory
```

#### Wild Card ?
-   `?` is another wildcard character that matches exactly one character.

```bash
ls ?.txt     # Lists 'a.txt' but not 'aa.txt'
ls ??.txt    # Lists 'aa.txt' but not 'a.txt'
```

#### Curly Brackets {}
-   Curly brackets allow for creating multiple items or iterating over sequences.

```bash
touch {a..z}.txt                # Creates files from 'a.txt' to 'z.txt'
touch {file1,file2,file3}.txt   # Creates 'file1.txt', 'file2.txt', 'file3.txt'
touch {a..z}{a..z}.txt          # Creates 'aa.txt', 'ab.txt', ..., 'zz.txt'
```

### Exclamation Point !
-   `!` is used for indirect variable referencing, i.e., getting the value of a variable whose name is stored in another variable.

```bash
my_var=51 
var_name="my_var" 
echo ${!var_name}               # Prints '51'
```

### Environment Variables
-   Environment variables are global variables provided by the system that provide information about the system environment.

```bash
echo $PATH       # Prints the PATH environment variable
```

Examples of environment variables:

-   `$HOME` : The home directory of the current user.
-   `$PATH` : The list of directories that the system searches when looking for a command.
-   `$SHELL` : The shell program currently in use (e.g., /bin/bash).
-   `$USER` : The username of the current user.
-   `$HOSTNAME` : The hostname of the machine the script is running on.
-   `$RANDOM` : A random number from 0-32767.
-   `$LINENO` : The current line number in the Bash script.

## Functions and Subshells

### Bash Functions
-   Work like regular Bash scripts.
-   Return value is entire output of the function.
-   Example: `a=$(ls)` where `a` is the entire output of `ls`.

### C++ Functions
-   Takes inputs, performs computation, returns value.

```c++
int sum(int a, int b) {
    return a+b;
}
```

### Return / Exit

-   `exit 0` means successful execution.
-   `exit 1+` means error occurred.
-   `$?` gives exit status of the last executed instruction.

### Bash vs C/C++

-   In Bash, 0 means success; in C/C++, 0 means false.
-   Successful execution of a bash script returns 0, triggering an `if` statement.

### Local Variables in Bash

-   All variables in Bash are global by default.
-   Declare a variable as `local` to limit its scope to the function.

### Subshells

-   Invoked using syntax like `a=$(ls)`.
-   They have their own scope; variables defined inside a subshell aren't accessible outside of it.
-   `$PPID` provides the current process ID; `$BASH_SUBSHELL` provides the subshell level.

```bash
a=$(b=1; echo $b)
echo "$b"
```

The echo statement will print nothing because `b` is defined in the subshell and is inaccessible outside of it.

```bash
echo "Current PID: $PPID"
echo "Subshell level before: $BASH_SUBSHELL"
a=$(echo "Subshell level in subshell: $BASH_SUBSHELL")
echo "Subshell level after: $BASH_SUBSHELL"
```

## C Basics

### C++ vs C
-   Both are different in terms of semantics and structure.
-   C++ is more than just 'C with objects'; it introduces classes, exceptions, templates, and more.

### Booleans
-   These are values that can be true or false.
-   In C, booleans are typically represented using `int` or a boolean library, with non-zero values interpreted as true.
-   Use when you need to evaluate or store a true/false condition.

```c
if (27) // 27 is non-zero, so this is true
{
	// code here will execute
}
```


### Casting
-   Useful for converting data from one type to another in C++.
-   Can be dangerous due to potential loss of information or unexpected behavior, especially when dealing with large numbers or negative values.
-   Use when you need to convert data between compatible types.

```c
float a = 1.5;
int b = int(a); // Casts float to int, b becomes 1
```


### Memory Allocation
- C uses `malloc`, `calloc`, `realloc`, and `free` instead of `new` and `delete` in C++.

#### Malloc
-   Allocates a specified amount of memory.
-   Use when you need to dynamically allocate memory.

```c
int* a = (int*)(malloc(10*sizeof(int))); // Allocates space for 10 integers
```

#### Calloc
-   Allocates memory and initializes it to zero.
-   Slower than `malloc` as it needs to wipe the memory.
-   Use when you need to allocate and initialize memory to zero.

```c
int* a = (int*)(calloc(10,sizeof(int))); 
// Allocates space for 10 integers and initializes them to 0
```

#### Realloc
-   Reallocates previously allocated memory.
-   Use when you need to resize an allocated memory block.

```c
int* a = (int*)(malloc(5*sizeof(int))); // Allocates space for 5 integers
a = (int*)(realloc(a, 10*sizeof(int))); // Reallocates space for 10 integers
```

#### Free
-   Deallocates or frees memory.
-   Use to avoid memory leaks when you're done with a dynamically allocated memory block.

```c
int* a = (int*)(malloc(10*sizeof(int))); // Allocates space for 10 integers
free(a); // Frees the allocated memory
```

## C I/O

### Functions
#### Arguments
-   Functions take copied arguments (pass by copy), but they can also operate on the original variables via pointers (pass by pointer).
-   Changes inside a function do not affect original variables unless pass by pointer is used.

```c
int sum (int i1, int i2)
{
	int local = i1 + i2;
	return local;
}
```

##### Pass By Copy
- Pass by copy is the default behavior in C. When the function scope ends, the variables within it are discarded from memory.

##### Pass By Pointer
- Pass by pointer is an alternative to pass by copy, where a function takes pointers as arguments. Changes made to dereferenced pointer arguments affect the original variables.


### Static Variables
-   Static variables keep their value across multiple function calls and are only initialized once.

```c
int weirdCount() {
	static int not_local = 0;
	not_local++;
	return not_local;
}

int main() {
	int a = weirdCount();
	int b = weirdCount();
	// print everything
}
```

### Static Functions
-   Static functions' scope is limited to the file they're in, enabling the use of the same function names in different files.

### Input & Output

#### Output
-   `printf` function is used for output, with placeholders (%d, %f, etc.) for variable values.

```c
int a = 5; printf("a is %d\n", a);
```

#### Input
-   `scanf` function is used for input, also utilizing placeholders similar to `printf`.

```c
int age;
printf("Enter your age: ");
scanf("%d", &age);
printf("You are %d years old.\n", age);
```

#### File I/O
-   Various functions (fopen, fgets, fputs, fclose, etc.) are used for file operations like opening, reading, writing, and closing files.

```c
FILE *fp = fopen("file.txt", "w+");
if (fp == NULL) {
    printf("Failed to open file\n");
    return 1;
}

fputs("Hello, World!", fp);

fseek(fp, 0, SEEK_SET); // Reset the file position indicator to the beginning

char buf[50];
fgets(buf, 50, fp);
printf("%s\n", buf);

fclose(fp);
```

## Memory & Inodes

### Arrays as Function Parameters
-   In C, to concatenate strings, `strcat(string1, string2)` is used. Example:

```c
char url[100] = 'www.';
char domain[100] = 'adelaide.edu.au';
strcat(url, domain); // Result is stored in url
```

### Function Calling

#### The Stack
-   During function calls, local variables are stored in a 'stack frame' within the 'stack'.

#### Persistence
-   Upon returning to the parent function, specific variables persist. Ways to retain others: file I/O, return value, altering pointers/references, static variables, dynamic memory.

#### The Heap
-   Dynamic memory allocation allows variables to exist beyond their local scope. Beware of memory leaks, when allocated memory can't be freed because there are no pointers to it.

```c
int* newInt(int value) {
    int* result = (int*) malloc(sizeof(int));
    *result = value;
    return result;
}

int* x;
int y = 4;
x = newInt(3); // new dynamically stored variable
x = &y; // Now no pointer points to the dynamically allocated memory
```


### String Functions
-   Strings in C are null-terminated character arrays. Common functions include `strcpy`, `strncpy`, `strdup`, and `strcat`.

```c
char dest[50], src[50];
strcpy(dest, "hello"); // dest now contains "hello"
strcat(dest, " world"); // dest now contains "hello world"
```


### INodes
-   Unix filesystem is based on INodes, data structures storing file info. It's divided into Super Block (general info), INode Table (INode details), and Data (actual file data).
-   INodes and their corresponding data are linked via indirect blocks.

### Access Modifiers
-   Unix `stat` command shows access, modify, and change timestamps for a file.


## Processes
### Process
-   A process is a currently running thread of execution on an operating system.

### Program
-   A program is a series of instructions executed in a sequence to perform a specific task.

#### Program vs Process
-   When a program starts execution, it becomes a process.
-   Processes can pause, and multiple processes can execute the same program.

### Processes in Unix
-   Unix processes can be viewed using commands like `ps`, `ps -a`, and `top`.

#### Executing Programs in Unix
-   Programs can be executed like bash commands. Alternatively, the `system` command can be used to execute Unix commands within a C program.

```c
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () { 
	char command[50]; 
	strcpy( command, "ls -l" ); 
	system(command); 
	return(0); 
}
```

-   The `execvp` command is used to start a new process without waiting for the existing one to finish.

### Forking
-   Forking is the process of duplicating a process. The fork function returns different values to the parent and child, allowing different tasks to be performed.

```c
while (TRUE)
{
    read_command(command, params);
    pid= fork();
    
    if (pid < 0) // fork failed
    {
	    handle_error();
    }

    else if (pid> 0) // parent process, waits for child to finish
    {
	    wait(NULL);
    }

    else // child process, executes command and finishes
    {
	    execvp(command, params);
    }
}
```

In the above example, a program executes a command, forks into a child and parent process, the child executes another program using execvp, and the parent waits for the child to finish.


## Redirection
-  Redirection changes data's source or destination in a command. For instance, `ls > temp.txt` sends `ls` command's output to 'temp.txt'

### Streams and File Descriptors

-   Unix-like systems typically define three default streams: standard input (stdin), standard output (stdout), and standard error (stderr). These are associated with the file descriptors 0, 1, and 2 respectively.
-   A file descriptor is essentially an identifier for a file. It is a way for a process to keep track of all the files it is interacting with.
-   Redirection is essentially telling a process to change its association from a default file descriptor (like stdout) to a different file or stream.

### Redirection in C

The provided C code demonstrates redirection in a C program. The process involves:

1.  Reading from the standard input and printing it out.
2.  Closing the standard input stream.
3.  Opening a file in read-only mode as a replacement for standard input (it also checks if the file opening was successful).
4.  Reading from the file (instead of standard input) and printing the result to the screen.

The `dup2` function is used to duplicate file descriptors. It takes two parameters: the file descriptor to be duplicated and the file descriptor to be overwritten.

```c
#include <stdio.h> // For writing
#include <fcntrl.h> // For <we’ll see>

int main()
{
	int fd; // This will be important later
	char line[100]; // Somewhere to store things
	
	fgets(line, 100, stdin);
	printf(“%s”, line); // Read and print
	
	fgets(line, 100, stdin);
	printf(“%s”, line);
	
	fgets(line, 100, stdin);
	printf(“%s”, line);

	// stdin just disappeared
	close (0);

	fd = open(“<a path>”, 0_RDONLY); // <= This is a flag

	// Die gracefully if file doesn’t exist
	if (fd != 0)
	{
		fprintf(stderr, “Could not open data as fd 0\n”);
		exit (1);
	}
	
	fgets(line, 100, stdin);
	printf(“%s”, line); // Read and print x3
	
	fgets(line, 100, stdin);
	printf(“%s”, line);
	
	fgets(line, 100, stdin);
	printf(“%s”, line);
	
	return 0;
}
```

### File Descriptors and Exec Group of Functions
-   A child process is created using `fork()`.
-   In the child process, the stdout is closed and a new file is created using `create()`.
-   The `execlp()` function is then used to run the `ls` command. Since stdout has been closed and replaced by the new file, the output of the `ls` command goes to the new file.
-   In the parent process, it waits for the child process to finish.


```c
int main()
{
	int id;
	id = fork();
	
	if (id == 0);
	{
		// Child
		{
			close(1);
			fd = creat (“ls_output”, 0644);
			execlp(“ls”, “ls”, NULL);
			perror(“execlp”);
			exit(1);
		}
	}
	else if (id != 0)
	{
		// Parent
		wait (NULL)
	}
}
```

## Pipes & Redirection

### Pipes in Bash

-   The `|` symbol allows for function chaining. E.g., `ls | wc -l` counts the number of lines outputted by `ls`.

### Pipes in C

-   Pipes in C use buffers to hold data between program executions.
-   Two file descriptors are needed for read/write operations, stored in a two-element array.
-   Read/write operations in C pipe communication are handled until the buffer is empty/full.

#### Implementation in C

-   In C, a writer process writes until the buffer is full and a reader process reads until the buffer is empty.
-   Both reader and writer consider standard input/output to be the file descriptors provided by the pipe array.
-   A pseudo pipe in C can replicate `ls | wc` from Bash, requiring careful use of `fork()` and `pipe()` system calls.

```c
int main()
{
	// Setup
	char * commands[2]; // Child Commands
	commands[0] = “ls”;
	commands[1] = NULL;
	
	char * commands[2]; // Parent Commands
	commands2[0] = “wc”;
	commands2[1] = NULL;
	
	char test_buffer[100]; // For printing
	
	// Fork and Pipes
	int my_pipe[2]; // pipe
	if (pipe(my_pipe) == -1) 
		perror(“Cannot create pipe\n”);
	
	pid_t my_pid; // Fork
	my_pid = fork();

	// Error
	if (my_pid < 0) 
		printf(“Failed Fork\n”);
	
	
	// Parent
	if (my_pid > 0) {
		close(my_pipe[1]);
		dup2(my_pipe[0], STDIN_FILENO);
		close(my_pipe[0]);
		wait(NULL); // wait for child
		execvp(“wc”, commands2);
	}
	
	// Child
	else // I.e. my_pid == 0
	{
		close(my_pipe[0]);
		dup2(my_pipe[1], STDOUT_FILENO);
		close(my_pipe[1]);
		execvp(“ls”, commands);
	}
}
```

### Pipe Restrictions

-   Pipes have a limited capacity. Data must be split into manageable chunks to avoid overflow.