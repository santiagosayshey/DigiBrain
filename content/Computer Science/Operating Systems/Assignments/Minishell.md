
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