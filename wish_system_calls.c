// for this please read the README_cool_shell_commands
#include <stdio.h>  // for functions like printf, scanf, ...
#include <unistd.h> // for fork()
#include <sys/wait.h> // for wait()
#include <string.h> // for strdup
#include <fcntl.h> // for open() openning a file

int main() {
    // case 1: if we do not care about the return val of the fork method   
    // (void) fork();  // at this point child processor is created, and OS runs the rest of the code for both branches

    // // create new process
    // printf("Hello: \n");


    // case 2: Caring the return type of fork() method

    int rc = fork(); // at this point child processor is created, and OS runs the rest of the code for both branches
    // create new process
    printf("Hello: \n");
    if (rc == 0){
        // we are in child process
        printf("I am the child process, with process id (%d): \n", (int) getpid());

        char* cmd_argv[10];
        cmd_argv[0] = strdup("/bin/ls");  // we could address any complied c program here
        cmd_argv[1] = strdup("-l");
        cmd_argv[2] = NULL; // NULL is the way to say the array ended, since we id not specify  the size of the array

        // do some set up works
        (void) close(STDOUT_FILENO); // no longer can print into screen
        open("output.txt", O_WRONLY | O_CREAT | O_TRUNC); // O_WRONLY=Write_only

        execv(cmd_argv[0], cmd_argv);

    } else if (rc >0){
        //we are in the parent process
        (void) wait(NULL);
        printf("parent processor id (%d): and child process id (%d) \n", (int) getpid(), rc);

    } else{
        // failure
    }
    
    return 0;
}
