
tests.out: utils.o test.o dataMemory.o fileProgram.o
	g++ -g -o tests.out test.o utils.o dataMemory.o fileProgram.o
	rm -rf *.o

test.o: test.cc
	g++ -g -c test.cc

utils.o: ../src/utils.cc
	g++ -g -c ../src/utils.cc

dataMemory.o: ../src/entity/memory/dataMemory/dataMemory.cc
	g++ -g -c ../src/entity/memory/dataMemory/dataMemory.cc

fileProgram.o: ../src/entity/file/fileProgram/fileProgram.cc
	g++ -g -c ../src/entity/file/fileProgram/fileProgram.cc

clean:
	rm -rf *.o *.out