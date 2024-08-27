## Prep Questions

### Question 1

#### Prompt
Write a bash script called **marks_merge.sh** that takes on the command line files of the format:

```
number, assess_mark  
a1000001,20  
a1000201,30  
a1000030,21
```

and so on, where the first column is a student number and the second column is a text representation of an integer mark. The script **marks_merge.sh** should merge the marks into a single file with the student number in the left column and the marks in the files in succeeding columns. The produced file should be in student number order. Where there is no mark for one student in a particular file then a "-" should be included. So, for example if the files marks1.csv contains:

```
number, prac_mark  
a1000001,20  
a1000201,30  
a1000030,21
```

 and the file marks2.csv contains:

```
number, exam_mark  
a1000003,70  
a1000201,65  
a1000030,90
```

Then the output (to stdout) for the command:

`./marks_merge.sh marks1.csv marks2.csv`

is

```
number,prac_mark,exam_mark  
a1000001,20,-  
a1000003,-,70  
a1000030,21,90  
a1000201,30,65
```

Hint, you _might_ find the unix utilities cut, paste and sort useful. When building your solution start with strong assumptions about the input - e.g. first assume that each file contains the same set of student numbers before relaxing this assumption in later solutions.

#### Solution

```bash
#!/bin/bash

# Sort the input files based on the name column
sort -t, -k1,1 $1 > data1_sorted.csv
sort -t, -k1,1 $2 > data2_sorted.csv

# Merge the sorted files using the join command
join -t, -1 1 -2 1 -a 1 -a 2 -e "-" -o 0,1.2,2.2 data1_sorted.csv data2_sorted.csv > merged_data.csv

# Move the last row into the first row
last_row=$(tail -n 1 merged_data.csv)
remaining_data=$(head -n -1 merged_data.csv)

# Remove temp files
rm data1_sorted.csv data2_sorted.csv
rm merged_data.csv

echo "$last_row"
echo "$remaining_data"
```

```terminal
./marks_merge marks1.csv marks2.csv
number, prac_mark, exam_mark
a1000001,20,-
a1000003,-,70
a1000030,21,90
```

### Question 2
#### Prompt
Write a bash script called **interleave_data.sh** that takes the names of files with the following format:

```
timestamp,value1  
100.1,45.3  
100.3,47.4  
100.7,48.3
```

And so on and interleaves the files by time-stamp ordering. Thus, for example, given a file: data1.csv with the content:

```
timestamp,value1  
100.1,45.3  
100.3,47.4  
100.7,48.3
```

and a file called data2.csv with the content:

```
timestamp,value1  
100.1,45.5  
100.2,46.8  
100.6,49.2
```

The output (to stdout)  of the command: 

`./interleave_data.sh data1.csv data2.csv `

is:

```
timestamp,value1  
100.1,45.5  
100.2,46.8  
100.3,47.4  
100.6,49.2  
100.7,48.3
```

Note how the clash on the first timestamp is resolved in favour of the second data set. Hint, you may find the "bash calculator" utility (bc) helpful in your solution.

#### Solution

```bash
#!/bin/bash

cat $1 <(tail -n +2 $2) | sort -t, -k1,1 > merged_data.csv

# Move the last row into the first row
last_row=$(tail -n 1 merged_data.csv)
remaining_data=$(head -n -1 merged_data.csv)

# Remove temp files
rm merged_data.csv

echo "$last_row"
echo "$remaining_data"

# Can't figure out how to overwrite existing data
```

```terminal
./interleave_data data1.csv data2.csv
timestamp,value1
100.1,45.3
100.2,46.8
100.3,47.4
100.6,49.2
100.7,48.3100.1,45.5
```

### Question 3
#### Prompt
Look at the C program for "cp" at the [following link](https://cs.adelaide.edu.au/users/second/spc/16s1-spc-adelaide/tutorials/tutorial2/cp1.c). 

Download this code and compile it. Run your cp code on two small files. Time how long the program you have compiled takes to copy a large file (use a bash script to create a large file if you like). Record the times for 10 runs of the experiment and bring the results along to the workshop session. Note, it is not enough to bring a set of timestamps that say 0.000, 0.000, 0.000, you will either need a more precise timing utility or larger file if you get these numbers!

#### Solution
##### Other
- ChatGPT generated bash script to create a file of size $1
```bash
#!/bin/bash

# Default values
filename="source.txt"
size="25m"


# Read command line arguments
while getopts "s:" opt; do
  case $opt in
    s)
      size="${OPTARG}"
      ;;
    *)
      echo "Usage: $0 [-s size]"
      echo "Example: $0 -s 25m"
      exit 1
      ;;
  esac
done

# Convert the size argument to bytes
size_bytes=$(echo "${size}" | awk '/[0-9]/{mult=1} /[kK]/{mult=1024} /[mM]/{mult=1048576} /[gG]/{mult=1073741824} {printf "%.0f", $0*mult}')
  
# Create and populate the file
current_size=0
block_size=1048576 # 1MB
block="$(head -c $block_size /dev/zero | tr '\0' 'A')"

while (( current_size < size_bytes )); do
  remaining=$((size_bytes - current_size))
  if (( remaining < block_size )); then
    echo -n "${block:0:remaining}" >> "$filename"
  else
    echo -n "$block" >> "$filename"
  fi
  current_size=$((current_size + block_size))
done

echo "File '$filename' created with size ${size}"
```

##### Modified C
- Modified C file to determine speed of copy
- Used bash script to create files of varying sizes

```C
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <time.h> // Add this header to use clock()

#define BUFFERSIZE 100
#define COPYMODE 0644

void errExit(char*, char*);

  
int main(int argC, char* argV[]) // Change return type to int
{
    int srcFd;
    int dstFd;
    int charCnt;
    char buf[BUFFERSIZE];
    
    /* Check args */
    if (argC != 3)
    {
        fprintf(stderr, "usage: %s source destination\n", argV[0]);
        exit(1);
    }

    /* Open the files */
    srcFd = open(argV[1], O_RDONLY);
    if (srcFd == -1)
    {
        errExit("Cannot open ", argV[1]);
    }

    dstFd = creat(argV[2], COPYMODE);
    
    if (dstFd == -1)
    {
        errExit("Cannot create ", argV[2]);
    }

    clock_t start = clock(); // Record the start time

    /* Copy the data */
    while ((charCnt = read(srcFd, buf, BUFFERSIZE)) > 0)
    {
        if (write(dstFd, buf, charCnt) != charCnt)
        {
            errExit("Write error to ", argV[2]);
        }
    }

    if (charCnt == -1)
    {
        errExit("Read error from ", argV[1]);
    }

    clock_t end = clock(); // Record the end time

    /* Close files */
    if (close(srcFd) == -1 || close(dstFd) == -1)
    {
        errExit("Error closing files", "");
    }
  
    // Calculate and display the time taken in seconds
    double duration = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken to copy the file: %f seconds\n", duration);

    return 0; // Add return statement
}

void errExit(char *s1, char *s2)
{
    fprintf(stderr, "Error: %s ", s1);
    perror(s2);
    exit(1);
}
```

- Combining the two to generate 10 files and find their copy speeds

##### Results ( 10 sig fig )

| File Size | Time (s)   |
|-----------|------------|
| 1m        | 0.033468   |
| 10m       | 0.414186   |
| 25m       | 1.080295   |
| 50m       | 2.175452   |
| 75m       | 3.359102   |
| 100m      | 2.577725   |
| 125m      | 5.135439   |
| 150m      | 4.137182   |
| 175m      | 8.019317   |
| 200m      | 5.887127   |

