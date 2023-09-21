#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int factorielle(int a){
    float res = 1;
    for(int i =1; i<=a; i++){
        res = res * i;
    }
    return res;
}

int main(int argc, char *argv[]){
    
    clock_t debut = clock();
    printf("%d \n", factorielle(atoi(argv[1])));
    clock_t fin = clock();
    double temps = (double) (fin-debut) / CLOCKS_PER_SEC;
    printf("%lf\n",temps);
          
}