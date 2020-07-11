libline.so: point.o line.o
	gcc -shared $^ -o $@

libpoint.so: point.o
	gcc -shared $^ -o $@

%.o: %.c
	gcc -c -Wall -Werror -fpic $^
