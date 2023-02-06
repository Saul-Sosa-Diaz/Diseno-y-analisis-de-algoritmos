
tests.out: utils.o test.o dataMemory.o fileProgram.o indirect.o direct.o inmediate.o
	g++ -g -o tests.out test.o utils.o dataMemory.o fileProgram.o indirect.o direct.o inmediate.o

test.o: test.cc
	g++ -g -c test.cc

utils.o: ../src/utils.cc
	g++ -g -c ../src/utils.cc

dataMemory.o: ../src/entity/memory/dataMemory/dataMemory.cc
	g++ -g -c ../src/entity/memory/dataMemory/dataMemory.cc

fileProgram.o: ../src/entity/file/fileProgram/fileProgram.cc
	g++ -g -c ../src/entity/file/fileProgram/fileProgram.cc

indirect.o: ../src/entity/operand/indirect/indirect.cc
	g++ -g -c ../src/entity/operand/indirect/indirect.cc

direct.o: ../src/entity/operand/direct/direct.cc
	g++ -g -c ../src/entity/operand/direct/direct.cc

inmediate.o: ../src/entity/operand/inmediate/inmediate.cc
	g++ -g -c ../src/entity/operand/inmediate/inmediate.cc


clean:
	rm -rf *.o *.out