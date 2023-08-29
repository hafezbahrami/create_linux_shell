#include<stdio.h>
#include"header.h"
#include<unistd.h>

void hello() {
    printf("\n I am in hello.c function \n");
    printf("\n PID of hello.c is (%d) \n", getpid()); // system call --> getpid()
}