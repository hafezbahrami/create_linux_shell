#include<stdio.h>
#include"header.h"  //hello() function is defined there

void main(){
    printf("\n I am in the main.c \n");
    printf("\n calling the hello function, in header.h \n");
    hello();
    printf("\n calling add function \n");
    add(3, 5);
    printf("\n back into main.c \n");
}