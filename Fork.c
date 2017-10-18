//Holden Hall Operating Systems 10/18/2017
// Program: Introduction into fork() and processes
#include <stdio.h>
#include <sys/types.h> 
#include <unistd.h>
#include <stdlib.h>

int main()
{
    pid_t pid; //sys/types
    pid_t getpgrp(void);
    pid_t setpgrp(void);

    printf("main program process id is %d\n", (int)getpid());
    pid = fork();
    if (pid == 0) //child process
    {
        printf("this is child process id %d\n", (int)getpid());
        printf("this is parent process id %d\n", (int)getppid());
        setpgrp(); //sets child process to group leader
        getpgrp(); //return group id
    }
    return  0;
}
