## Linux Basics 
- Everything is a file
- C and Unix are low level and can easily interact with each other

### Navigation
- Each directory contains:
	- File to to the parent directory `..` 
	- Files within the current directory `.`
	- The root directory `/`
- Use `cd` to navigate between them

### File Permissions
- Users / groups have a unique ID that determine whether a user can .. to files:
	- Read
	- Write
	- Execute
- These permissions can be changed using `chmod`

```bash
chmod [type of permission] [file path]

chmod +x my_script.sh
```

```bash
+r will allow read
+w will allow write
+x will allow execute

-r will stop read
-w will stop write
-x will stop execute
```

### Processes
- A program is a series of instructions
- A process is the execution of this program
- Associated with users in a hierarchy
	- If a parent process dies, it's children will also most likely die

### The Kernel
- Base process of the operating system
- Interfaces CPU, memory with peripherals and other applications
- Manages files, users, devices and processes

![[docs/Images/data_center-kernel_layout_half_column_mobile.png]]

### The Shell
- Another process aimed to run other processes, like the kernel

### Redirection
- Direct the output of one process into the input of a new process

```bash
# read from a file
script.sh < file.txt

# save to a file
script.sh > file.txt
```

### Piping
- Chain commands together using redirection

```bash
# get the word count as number of lines from the ls command
ls | wc -l
```


## Bash Basics
- `touch` will update a file to says it's been used, will create the file if it doesn't exist
- `#!/bin/bash` is a shebang added to the start of a script to tell the computer to execute using bash syntax
- `echo` means print
- `./` will execute a binary

```bash
#!/bin/bash

touch hello_world2.sh                         # create the script
chmod +x hello_world2.sh                      # add execute privelages to file
echo '#!/bin/bash' >> hello_world2.sh         # stdout shebang to start of file
echo 'echo Hello World 2' >> hello_world2.sh  # stdout echo line to file
./hello_world2.sh                             # execute file
```

### Arguments
- `$#` number of arguments
- `$1, $2, etc` will print the argument at position x
- `$0` prints the name of the executable (including its relative path if given)
- `$@` prints all of arguments
- `shift x` will delete the left most argument and shift every other argument to the left by x amount

### Debugging
- Can run scripts in explicit mode to print the entire flow of the output and find errors

```bash
/bin/bash -x script.sh
```

### Loops

#### For Loop

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

```bash
count=1
while [ $count -le 5 ]
do
   echo "Count: $count"
   count=$((count + 1))
done
```

#### Until Loop

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
- Can also use `let` and `expr` to do the same thing

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
- Define variables without whitespace `a=1` NOT `a = 1`

### Strings
- Whitespace only allowed in string itself
- Can use single or double quotes
- Echo will print and interpret command substitution


```bash
a=“quack” 
echo '$a$a'           > $a$a
echo $a$a             > quackquack 
echo “${a}s”          > quacks 
echo “${a:1:4}”       > uac
```

### Arrays
- Defined inside circle brackets with whitespace between each element (including first and last)

```bash
array=( A B C D E F G )
```

- `${arr[x]}` will access array at element x
- `${arr[@]}` will get all elements in array
- `${#arr[@]}` will get length of array
- `${arr@:i:j}` get values from index i to j

### Exporting Variables
- Cannot access variables from 1 script inside another script
- `export 'variable'` allows this

### Redirection
- `read` takes input and stores it inside a variable

```bash
read a b # this will prompt a user twice and set the first value to be a and the second to be b
```

- `< and >` redirects the output of 1 command into another
	- `>` will overwrite the file
	- `>>` will append to an existing file

```bash
wc < input_file.txt > output_file.txt 
#  will pass input to word count command, then send the output to be saved in another file
```

### Pipes
- Can pipe the output of a command into another using `|`

```bash
ls | wc -l
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
- Group things together to make it easier to work with multiple files at once

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

#### Exclamation Point !
- `!` is used for indirect variable referencing, i.e., getting the value of a variable whose name is stored in another variable.

```bash
my_var=51 
var_name="my_var" 
echo ${!var_name}               # Prints '51'
```

### Environment Variables
- Global variables provided by the system to provide information about the system environment
	-   `$HOME` : The home directory of the current user.
	-   `$PATH` : The list of directories that the system searches when looking for a command.
		- `cd` is not in the path as it is built into the shell
	-   `$SHELL` : The shell program currently in use (e.g., /bin/bash).
	-   `$USER` : The username of the current user.
	-   `$HOSTNAME` : The hostname of the machine the script is running on.
	-   `$RANDOM` : A random number from 0-32767.
	-   `$LINENO` : The current line number in the Bash script.

## Functions and Subshells

### Bash Functions
- Bash functions work like regular bash scripts that can be used with arguments
- Return value is the entire stdout of the function

```bash
a=$(ls) # a is the entire output of the ls function, all the files listed in the current directory
echo $a
```

#### Return / Exit
- Use `exit` to return the state of the function
	- `0` is success
	- `1` is failure
	- Opposite in C / C++, 0 is failure and 1 is success
- Use `$?` to get the status of the previously executed function / command

```bash
a=$(ls)
echo $?
echo $?
```

### Local Variables
- All variables are global by default in Bash
- Declare a variable as `local` to limit it's scope to the function

### Subshells
- Invoked by calling a function within another function
	- `a=$(ls)`
- Have their own scope, variables defined within a subshell aren't accessible outside of it
- `$PPID` provides the current process ID
- `$BASH_SUBSHELL` provides the subshell level

## C Basics / Memory Allocation
### Booleans
- Do not exist in C, use ints instead
	- 0 is false, everything else is true


### Casting
- Converting one data type into a different one
- Dangerous, may lose large amounts of precision with large or negative numbers

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


## Memory and Inodes

### Arrays as Function Parameters


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
-   In C, to concatenate strings, `strcat(string1, string2)` is used. Example:

```c
char url[100] = 'www.';
char domain[100] = 'adelaide.edu.au';
strcat(url, domain); // Result is stored in url
```

```c
char dest[50], src[50];
strcpy(dest, "hello"); // dest now contains "hello"
strcat(dest, " world"); // dest now contains "hello world"
```

### Inodes
- Files in Linux contain a file name and an associated inode number
- An inode contains the size of the file, it's relative location, permissions, owners and modification / access date as well as the number of hardlinks to it
- Inodes contain a set number of blocks 
	- Direct, which is useful for storing small parts of a file
	- Indirect, useful for storing bigger files
- By making inodes static, we can have a pre determined set number of them on a file system and allow for faster lookup times for larger files using indirect blocks
- Especially larger files can link indirect blocks within indirect blocks to further increase the size
- We can access the data in an inode table using `stat` on a file

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

## Make
- In a `Makefile`, the first target is the default, executed when `make` is called with no arguments.
- Custom `Makefile` names can be used with the `-f` option (e.g., `make -f MyMakefile`).

### What does make do?
- `make` is a utility for managing program compilation. It optimizes the process by only recompiling changed files and their dependencies.
- A `Makefile` controls the `make` process. It contains targets (outputs), dependencies (inputs), and instructions on how to create the target from the dependencies.
- `make` uses timestamps to determine if a file needs to be recompiled - if a target's timestamp is older than any of its dependencies, `make` triggers a recompilation.

### Dependencies
- `make` commands can be chained to create a dependency tree, allowing complex build processes to be automated.
- A dependency occurs when one piece of code relies on another. `make` helps manage these dependencies, reducing compilation time.

### Make Shortcuts
- `make` provides several shortcuts:
    - `$@` refers to the current target.
    - `$^` refers to all of the current target's dependencies.
    - `$<` refers to the first dependency.
- The wildcard character `*` can be used to match multiple files in a rule.
- The wildcard character `%` can be used to define pattern rules, allowing the same rule to be applied to multiple targets.


### Macros
- Macros (e.g., `CC=gcc`) are variables that can be used to simplify `Makefile` instructions.


## Threads
