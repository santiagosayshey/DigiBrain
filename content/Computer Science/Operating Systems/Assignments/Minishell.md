
| Test Case                                         | Command Input                | Expected Result                                                                                      | Actual Result |
| ------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------- | ------------- |
| Normal command execution                          | `ls`                         | Lists files in the current directory                                                                 |               |
| Background command execution                      | `sleep 5 &`                  | `[Running background job]` followed by a prompt. After 5 seconds: `sleep done`                       |               |
| Background command with another command execution | `sleep 5 &` followed by `ls` | `[Running background job]` followed by listing files in the directory. After 5 seconds: `sleep done` |               |
| `cd` command to change directory                  | `cd /tmp`                    | Changes directory to /tmp, prompt displayed in /tmp directory                                        |               |
| `cd` command with no arguments                    | `cd`                         | Displays error message: `cd: No such file or directory`                                              |               |
| Invalid command                                   | `invalidcommand`             | Displays error message: `invalidcommand: No such file or directory`                                  |               |
| Command execution after `exec` fails              | `invalidcommand`             | Error message: `execvp: No such file or directory`                                                   |               |
| Command execution with multiple arguments         | `echo hello world`           | Prints: `hello world`                                                                                |               |
| Handling of EOF (Ctrl+D)                          | `Ctrl+D`                     | Displays: `EOF pid [pid] feof 1 ferror 0` and exits the shell                                        |               |
