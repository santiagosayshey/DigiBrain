This worksheet has some exercises to get you used to bash scripting.

Do these exercises and bring your answers along to your next workshop session. We will assume that you have worked at these exercises when you start your session and we will check that you have prepared so you can participate – that is you will need to make sure you have prepared to get full marks for participation! Note: it is ok if you have really tried to answer these questions but have some errors – your participation is based on you having made a serious attempt at your preparation and your questions during the session.

Answer the questions as best you can. Show your answers to your lab supervisor at the **start** of this session. Note: the supervisors will devote most time to work you had trouble with – there will be limited time for other feedback.

### Exercise 1: First Shell Script

A shell script is nothing more than shell commands placed in a file. If we set the permissions  
on the file so it can be executed, the system will view the script just like any other built-in  
command.  
The first line of a bash script must look like this:

```bash
#!/bin/bash
```

This tells the system that it is a script for the bash shell. (You can, if you wish, use a  
different shell, but you are then “on your own” — the tutors will not be able to give you  
help.) The remainder of the file contains commands that you want the system to execute.  
When you have created the file, you need to make the script executable, by turning on  
the x (execute) permission, using the change mode command:

```bash
chmod +x FILENAME
```

You can now execute your script by typing:

```bash
./FILENAME parameters
```

Inside a shell script, you can use the values of the parameters that were passed on the  
command line: use $1 to refer to the first parameter, $2 for the second, and so on. You can  
only refer to nine parameters in this way, because $10 will be interpreted as the value of  
$1 with a zero appended to it. If you want to refer to higher numbered parameters, you  
must enclose the number in braces, like this:

```bash
${10}.
```

### Exercise 2: Debugging shell scripts

Debugging shell scripts can be as easy as cutting and pasting commands to the terminal  
(to try out each command, and see what is happening), but there are some other tricks you  
should be aware of. The bash command set can be used to turn on some useful options; For  
example set -x will cause the shell to echo each expanded command before it is  
executed.

You can do this via: /bin/bash -x ./my_script.sh

You can also insert echo commands at various places in your script to print things out so  
you can see them.

Be prepared to show your preparation code for this file to the demonstrators in your  
workshop.

### Exercise 3: Trivial Script

Write a script named trivial, that prints out the parameters it is passed, one per line.  
For example if we type:

```bash
trivial -f wombat.txt some more words
```

It will print:

```bash
1= -f  
2= wombat.txt  
3= some  
4= more  
5= words  
6=  
7=  
8=  
9=
```

Again, save your code so it can be shown to the demonstrator.

### Exercise 4: String Experiments

Try calling the trivial script with commands involving quotes, for example:  
trivial "This is a string" ’and another’  
Can you predict what will happen when you type this? Try it:

```bash
trivial "This is a string" ’$1’
```

What about this?

```bash
trivial "This is a string" "$1"
```

The way that single and double quotes work is not entirely obvious. (And the description  
in the bash manual is not a lot of help, either!) You will need to conduct some experiments to see what happens in each case. Be prepared to describe the outcome to the demonstrator.

## Workshop 2b - In class exercises.

Try the following questions - complete as many as you can (also feel free to bring them prepped)  If you get stuck ask for help. The the tutor will assess your participation both in terms of your preparation and the work you complete in this session.

### 1. Personal phone book

Create a (shortish) phone book in a text file. Each line should have a name and a phone number on it, for example:

```
alan smith 8313-4484 
mary contrary 0403-980-123 
coles 8310-9999   
mary o’hagan 1800-261-331   
... etc
```
Now write a script named _phone_ that prints out any lines that match the parameter, eg:

phone alan

would print: alan smith 8313-4484 or if we typed:

phone 4484

it would again display: alan smith 8313-4484

If your script is written correctly, the following command will generate the same output as before: phone ala. What do you predict will happen for the query:

phone mary

### 2. Recently changed files

Write a script named _recent_ that takes a parameter _n_ (a number) and lists the names of the n most-recently-modified files in the current directory but without any file extensions. (This question is substantially harder than the previous two problems.) Hint 1: The ls command can be asked to list files in time-order rather than name-order... Hint 2: Use the man -k command to find a command that will chop the tail off a file...

### 3. Finished already?

Write a script named _sizeof_ that can be called like this:

sizeof FILE

that prints out the size of the given FILE.

### 4. Too easy?

Modify the script to accept a list of filenames, and print the sum of the sizes of the files. You can find out about shell arithmetic by reading the bash manual.

### 5. Still too easy?

If FILE is the name of a directory, make your sizeof script add the sizes of all the files in that directory (ignoring sub-directories).

### 6. Champion level!

Modify your sizeof function so that it recursively explores subdirectories, and adds up the size of all the contained files.

Make sure your participation is checked before the end of this session.