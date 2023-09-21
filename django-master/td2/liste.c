#include <stdio.h>
#include <stdlib.h>
#include "liste.h"

lst creerListe(){
    lst list = (lst) malloc(sizeof(struct liste));
    list->debut = NULL;
    list->nbElem = 0;
    return list;
};

void ajouterEnTete(lst l, int x){
    //creation un maillon qui prend comme adresse suivante le premier maillon de la liste
    ml nouveauElem = (ml) malloc(sizeof(struct maillon));
    nouveauElem->val = x;
    nouveauElem->suivant = l->debut;

    //le debut de la liste devient ensuite le maillon crée
    l->debut=nouveauElem;
    l->nbElem++;
};