#include <stdio.h>

union obj2
{
    char c;
    int i;
};

struct obj1
{
    char c;
    int i;
};

int main()
{
    struct obj1 s1;
    union obj2 s2;
    s1.c = 'a';
    s1.i = 42;
    s2.c = 'b';
    s2.i = 12345678;
    printf("%ld %ld \n", sizeof(struct obj1), sizeof(union obj2));
    printf("%c %d \n", s2.c, s2.i);

    return 0;
};
