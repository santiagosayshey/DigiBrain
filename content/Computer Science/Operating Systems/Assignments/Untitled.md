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