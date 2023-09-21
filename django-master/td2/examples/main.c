#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char * tampon = malloc(10 * sizeof(char));
    // free (tampon);
    // free (tampon);

    //strcat(tampon + 11, "X");

    strcpy(tampon, "012345678");
    printf("%c \n", tampon[3]);
    printf("%c \n", tampon[12]);
    free(tampon);
    
    return 0;
}