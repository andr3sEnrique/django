#include <stdio.h>


void main () {
    int x = 0;
    int *ptr_x = &x;
    *ptr_x += 3;
    printf("%d\n",x);
}