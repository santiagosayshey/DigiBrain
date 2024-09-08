
| Command                                 | Expected Output                             | Actual Output |
| --------------------------------------- | ------------------------------------------- | ------------- |
| `cd /tmp`                               | No output (changes directory to /tmp)       |               |
| `cd`                                    | No output (changes to home directory)       |               |
| `cd /nonexistent`                       | "cd: No such file or directory"             |               |
| `ls &`                                  | "[1] <pid>" (where <pid> is the process ID) |               |
| `sleep 5 &`                             | "[2] <pid>"                                 |               |
| `echo hello`                            | "hello"                                     |               |
| `nonexistentcommand`                    | "execvp: No such file or directory"         |               |
| `ls /tmp && echo "Done"`                | (Contents of /tmp directory)<br>"Done"      |               |
| (After background job completes)        | "[1]+ Done                    ls"           |               |
| (After second background job completes) | "[2]+ Done                    sleep 5"      |               |
| (Empty input)                           | (No output, returns to prompt)              |               |
| `exit`                                  | (Shell exits)                               |               |

Notes:
1. The exact process IDs (<pid>) will vary each time you run the commands.
2. The output for `ls /tmp` will depend on the contents of your /tmp directory.
3. The "Done" messages for background jobs should appear before the next prompt, after the job completes.
4. Error messages (like for `cd /nonexistent` or `nonexistentcommand`) may vary slightly depending on the system, but should convey the same information.

You can run these commands in your implemented shell and fill in the "Actual Output" column to compare with the expected behavior. This will help you verify if your implementation is working as intended.

```shell
foo@bar:/ $ sleep 8 &
[5] 10973
foo@bar:/ $ sleep 7 &
[6] 10974
foo@bar:/ $ sleep 6 &
[7] 10975
foo@bar:/ $ sleep 5 &
[8] 10976
foo@bar:/ $ ls
Makefile  README.md  even.c  minishell  minishell.c  temp
[5]   Done                    sleep 8
[6]   Done                    sleep 7
[7]-  Done                    sleep 6
[8]+  Done                    sleep 5
foo@bar:/ $
```

```
foo@bar:/ $ ./minishell
sleep 8 &
[1] 11033
sleep 7 &
[2] 11034
sleep 6 &
[3] 11035
sleep 5 &
[4] 11036
ls
Makefile  README.md  even.c  minishell  minishell.c  temp
[1]  Done sleep 8
[2]  Done sleep 7
[3]- Done sleep 6
[4]+ Done sleep 5

```