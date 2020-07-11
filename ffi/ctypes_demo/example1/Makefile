clib.so: clib.o
	gcc -shared -o libclib.so clib.o

clib.o: clib.c
	gcc -c -Wall -Werror -fpic clib.c
