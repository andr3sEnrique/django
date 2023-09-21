main: main.o liste.o
	gcc -std=c11 -Wall -Wextra -O0 main.o liste.o -o main

main.o: main.c liste.c
	gcc -c main.c

liste.o: liste.c liste.h
	gcc -c liste.c 

clean:
	rm -f main *.o

.PHONY: clean