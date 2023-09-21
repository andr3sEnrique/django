#include <stdio.h>
#include <stdlib.h>

int multiplication(int x, int y){
    return x*y;
}

int multiplication2(int *x, int *y){
    return *x * *y;
}


int somme(){
    int a = NULL;
    return a;
}

int
main(void)
{
    int x, y;
    x = 2;
    y = 3;
    printf("%d\n",multiplication(x,y));
    printf("%d \n", multiplication2(&x,&y));

    int *t;
    t = malloc(10*sizeof(int));
    for (int i=O;i<=10; i++)
    {
        t[i] = i;
    }

}