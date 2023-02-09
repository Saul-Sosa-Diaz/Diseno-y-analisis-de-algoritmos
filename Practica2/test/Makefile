
tests.out: utils.o test.o dataMemory.o fileProgram.o indirect.o direct.o inmediate.o programMemory.o
	g++ -g -o tests.out test.o utils.o dataMemory.o fileProgram.o indirect.o direct.o inmediate.o programMemory.o

test.o: test.cc
	g++ -g -c test.cc

utils.o: ../src/lib/functions/utils.cc
	g++ -g -c ../src/lib/functions/utils.cc

dataMemory.o: ../src/lib/memories/dataMemory/dataMemory.cc
	g++ -g -c ../src/lib/memories/dataMemory/dataMemory.cc

programMemory.o: ../src/lib/memories/programMemory/programMemory.cc
	g++ -g -c ../src/lib/memories/programMemory/programMemory.cc

fileProgram.o: ../src/lib/files/fileProgram/fileProgram.cc
	g++ -g -c ../src/lib/files/fileProgram/fileProgram.cc

indirect.o: ../src/lib/operands/indirect/indirect.cc
	g++ -g -c ../src/lib/operands/indirect/indirect.cc

direct.o: ../src/lib/operands/direct/direct.cc
	g++ -g -c ../src/lib/operands/direct/direct.cc

inmediate.o: ../src/lib/operands/inmediate/inmediate.cc
	g++ -g -c ../src/lib/operands/inmediate/inmediate.cc


clean:
	rm -rf *.o *.out