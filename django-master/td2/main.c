#include "liste.h"
#include <stdio.h>

int main(){
    lst liste = creerListe();
    printf("%d \n", liste->nbElem);
    ajouterEnTete(liste, 3);
    printf("%d \n", liste->nbElem);
    return 0;
}