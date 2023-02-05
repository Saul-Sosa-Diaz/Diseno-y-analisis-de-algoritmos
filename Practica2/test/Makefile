
tests.out: utils.o test.o dataMemory.o
	g++ -g -o tests.out test.o utils.o dataMemory.o
	rm -rf *.o

test.o: test.cc
	g++ -g -c test.cc

utils.o: ../src/utils.cc
	g++ -g -c ../src/utils.cc

dataMemory.o: ../src/entity/memory/dataMemory.cc
	g++ -g -c ../src/entity/memory/dataMemory.cc

clean:
	rm -rf *.o