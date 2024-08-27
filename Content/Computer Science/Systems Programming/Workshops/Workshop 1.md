https://myuni.adelaide.edu.au/courses/85264/pages/workshop-1

### Exercise 1 - Are you in bash?

``` 
Log into the Linux image in your machine. Start up a terminal application. Type at the  
terminal:

>> echo $SHELL

* Note the ">>" is just my shorthand for the prompt, do not type ">>"

* 1) What does it say?

If it replies /bin/bash (or similar) then you are good to get started. Otherwise if says  
something else (like tcsh) then you will need to type the word

>> bash

at the prompt in order to start the bash shell.
```

outputs `/bin/bash`


### Exercise 2 - Echo Echo Echo 

``` 

Type the following commands at the shell prompt (one line at a time)

>> echo “hello world”  
>> echo “hello world”; echo “hello again”  
>> echo –n “hello world”; echo “same line”  
>> echo -e 'hello\011hello'  
>> echo -e '\007'                           # This may not work on your machine...  
>> echo –ne

Now type in:

>> man bash

and type in:

>> /echo
```

1. outputs `hello world`
2. outputs `hello world` on 1 line, then `hello again` on a second line
3. outputs `hello world` on 1 line, then `same line` on *the same line*
4. outputs `hello world   hello world`, the 011 must correspond to a space character
5. does not work
6. no output

### <Exercise 3: Core Unix Commands

``` bash

For each of the following commands type “man <command>”  
Describe briefly in your own words, what each command does

ls  
cp  
rm  
mv  
cat  
grep  
pwd  
cut  
paste  
sed  
awk  
find

Briefly comment on whether the command is simple or more complex in terms of its behaviour.
```

 1. `ls` takes in a file as a parameter and lists all the files within that file (recall that everything is a file and therefore a directory is a file)

 2. `cp` takes in a file as a parameter and copies all the files within that file. Pastes those files in the file which is defined as the second parameter

3. `rm` takes in a file as a parameter and removes it

4. `mv` takes in a file as a parameter and moves it to another file defined as the second parameter

5. `cat` combines two files together 

6. `grep` searches for patterns in each file

7. `pwd` prints the name of the current working directory

8. `cut` takes in file as parameter and cuts sections from each line of files, choose specific bytes, characters. etc

9. `paste` merges seperate lines and seperates them with tabs in a file

10. `sed` finds and changes text within a file

11. `awk` scans and finds patterns within files

12. `find` looks for files within a directory



## *Extension Exercises*

### Exercise 1

```
Find how many files are in the current directory. Hinted functions (ls, wc)
```

```run-bash
ls | wc -l
```
- ls will list the files in the current directory, wc will take them as a parameter and output the number of files (using -l)

### Exercise 2

```
Create two files which contain some random lines of text (at least 5 lines per file). The goal is to print out the three lines which come first in alphabetical order. Hinted functions (cat, sort, head)

i.e) File 1 - a.txt

The rain in Spain  
falls mainly  
on the plain  
Really?  
My fair lady?

File 2 -b.txt

To be or not to be  
that is the question  
Whether tis nobler in the mind  
to suffer the slings and arrows  
of outrageous fortune

**Your command ought print out:**

falls mainly  
My fair lady?  
of outrageous fortune
```

``` bash
cat a.txt b.txt | tr '[:upper:]' '[:lower:]' | sort | head -n 3
```

1. concatenate the two text files
2. convert to lower case
3. sort alphabetically
4. print the first 3 lines from the head


### Exercise 3 

```
Mu ha ha ha ha!!

So what about printing out in numerical order the size of all the files **you own** in the current directory!! The output should be an ascending list of numbers.

Hinted functions. (cut, grep, ls, tr).
```