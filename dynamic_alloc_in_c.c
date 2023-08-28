#include <stdio.h>  // for functions like printf, scanf, ...
#include <stdlib.h> // for malloc

int main() {   
    int n = 4;

    int* age_ptr;
    age_ptr = (int*) malloc(n * sizeof(int));

    if(age_ptr == NULL){
        printf("Dynamic allocation of memory has failed!");
    }

    printf("Enter 4 int values: \n");
    for (int i=0; i<n; ++i){
        scanf("%d", age_ptr+i);
    }

    // Now lets allocate 2 more integer to our dynamic memory
    n = 6;
    age_ptr = realloc(age_ptr, n*sizeof(int));

    printf("Printing the input values: \n");
    for (int i=0; i<n; ++i){
        printf("%d \n", *(age_ptr+i));
    }

    free(age_ptr);
    
    return 0;
}
