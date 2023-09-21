#include <stdio.h>

int sommeEntiers(int n)
{
    int somme = 0;
    for(int i=0;i<n+1;i++){
        somme += i;
    }
    return somme;
}
 //exercise 1

//exercise 2 
int mystere (int n){
    int res = 1;
    for (int i=2; i<n+1; i++){
        res *= i;
    }
    return res;
}



void example1()
{
    int x = 12;
    if (x > 9) {
        printf("Bravo! vous avez obtenu votre BUT");
        if (x > 11) {
            printf(" avec mention, bravo!");
        }else {
            printf(" sans mention.");
        }
    }
    printf("\n");
}

void example2()
{
    int a = 1;
    int b = 2;
    int tmp = a;
    a = b;
    b = tmp;
    printf("%d %d\n",a,b);
}

void example3()
{
    int i, j=0 ;
    for (i=0; i<10; i++){
        while (j< 10){
            printf("Bonjour! ");
            j++;
        }
    }
    printf("\n");
}

void expressions(){
    int x= 1, y=2, z=3;
    printf("Expression \n");
    printf("%d\n ",1-2+3);
    printf("%d\n ", 1 - (2+3));
    printf("%d\n ", 1 != 4 -3 + 3 - 2 / 2 + 1);
    printf("%d\n ", 1 +- 2 * 3);
    printf("%d\n ", x < y && y < z && z < x);
    printf("%d\n- ", (!x && y) || (x && !y));

}

int main(void)
{
    printf("%d\n",sommeEntiers(10));
    // %f pour float, %d pour int
    printf("%d\n", mystere(10));
    example1();
    example2();
    example3();
    expressions();
    return 0;
}