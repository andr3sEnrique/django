#include <stdio.h>

void main(){

    int t[3] = {0, 1, 2};
    int *p = &t[0];
    (*(p+1))++;
    printf("[%d, %d, %d]\n",t[0],t[1],t[2]);
    *(p+2) += *p + 1;
    printf("[%d, %d, %d]\n",t[0],t[1],t[2]);
    t[t[t[0]]] = 1;
    printf("[%d, %d, %d]\n",t[0],t[1],t[2]);

}
