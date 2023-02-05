all: simulador

simulador: utils.o main.o dataMemory.o
	g++ -g -o simulador main.o utils.o dataMemory.o

main.o: ../src/main.cc
	g++ -g -c ../src/main.cc

utils.o: ../src/utils.cc
	g++ -g -c ../src/utils.cc

dataMemory.o: ../src/entity/memory/dataMemory.cc
	g++ -g -c ../src/entity/memory/dataMemory.cc

clean:
	rm -rf *.o simulador