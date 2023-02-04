all: simulador

simulador: utils.o main.o
	g++ -g -o simulador main.o utils.o

main.o: ../src/main.cc
	g++ -g -c ../src/main.cc

utils.o: ../src/utils.cc
	g++ -g -c ../src/utils.cc

clean:
	rm -rf *.o simulador