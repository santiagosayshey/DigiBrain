```html
<div style="page-break-after: always;"></div>
```

###### Exercise 1


> [!exercise]+ Exercise 1
> Go to /home/q1/. Exploit the program to get the secret.
> 
> **Answer:**
> Analysing the code in `run_me.c`, it becomes evident that we are trying to cause a buffer overflow inside `buffer` to overwrite `changeme`. An obvious hint to this is the use of `strcopy`, which is notorious for causing buffer overflows. 
> 
> To achieve this, we notice that `buffer` takes 1024 characters

