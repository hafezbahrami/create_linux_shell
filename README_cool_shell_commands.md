Reference: https://www.youtube.com/watch?v=Dq8l1_-QgAc&ab_channel=LowLevelLearning

# Summary
Here we want to create our own shell. We will explore a couple of important system-calls, such as fork(), wait(), execv().
We will explore, when we write "ls -l -a" in command line, how does it get run.

# Linux shell commands

## ls (for listing)

ls is a program that we run in the shell it will gets run. Normally it outputs inthe shell. However,
we can output it in a txt file and then cat it to see what it is inside
```
ls > output.txt
cat output.txt
```

## pipe:
It is when the output of one program wantsto go to the input of another program.

Example: Let's see how we can count the # of items out of a "ls" command.
```
ls > output.txt
wc -l output.txt
```
"wc -l" means ==> WordCount Lines.

Bu instead of two lines of codes above, we can pipe the output of first command into the WordCount program:
```
ls | wc -l
```

## man page
If we have trouble with one command in shell, or c, we can man page that. For instance we want to use 
fork() in uor c program, but do not know how, then the help is at:

```
man fork
```

# the wish.c

## fork()
fork() creates a copy of the current process (parent), sa a child processor. And then, runs the
code for both processors. The code is:
```
int main() {   
    (void) fork();

    // create new process
    printf("Hello: \n");
    
    return 0;
}
```

We can compile this code:
```
gcc -o wish ./03_c_codes_traning/wish.c -Wall
```

We can run the compiled file by:
```
./wish
```

We see the hello twice, meaning both processors (created by fork(), one parent and one child) will be called.
We can change it if we change the output file of fork() method:

```
int main() {
    int rc = fork();
    // create new process
    printf("Hello: \n");
    if (rc == 0){
        // we are in child process
        printf("I am the child process: \n");
    } else if (rc >0){
        //we are in the parent process
        printf("I am the parent process: \n");

    } else{
        // failure
    }
    
    return 0;
}
```

Now, we cann compile and run the compiled file. We sould know, there is no order which one (parent or child) gets called first.

In Linu, processors have id, and we can get it by:
```
(int) getpid()
```

## wait()
We can make the parent processor wait till the child gets finished, and then parent gets started.

Actually this waiting is very common. For instance, in a shell, if we type ls and right after gcc ..., gcc should wait till 
the ls is done.

The command line we need to add in our c program, in the parent section is: Let's say, at this point we do not care about the
return value, alos Null as whatever child-ifo that could be passed into the parent.
```
(void) wait(NULL)
```

Adding this wait, makes our code more determinsitic, and running it multiple times, we get the same results.

## execv()

In the child processor section:
```
        char* cmd_argv[10];
        cmd_argv[0] = strdup("/bin/ls");
        cmd_argv[1] = strdup("-l");
        cmd_argv[2] = NULL; // NULL is the way to say the array ended, since we id not specify  the size of the array

        execv(cmd_argv[0], cmd_argv)
```

When the os hits the line that we have "execv(XXX)", it goes to the Kernel, and Kernel says you were running
wish_system_calls, so far. But now I am switching to ls program stored in "/bin/ls", and create a new heap and new stack,
and jump into the main of that program ls.
We basically, killing the shell and creating new program ls to run.

If the execv() is successful, it never returns, and will be stuck in the ls program.

Instead of calling the "/bin/ls" program, we could have called any program. Even, a c program that we wrote ourselves. 

## pipe and rediction
We can also write the pipe and redirection that we normally do in command line.

First, let's close the file output to the screen, and create a new Write_only file (named: output.txt)
```
    (void) close(STDOUT_FILENO); // no longer can print into screen
    open("output.txt", O_WRONGLY | O_CREATE | O_TRANC);
```