all: simulador

simulador: utils.o main.o dataMemory.o controlUnit.o fileProgram.o tapeFile.o programMemory.o indirect.o direct.o inmediate.o add.o div.o mult.o sub.o halt.o read.o write.o jgtz.o jump.o jzero.o load.o store.o
	g++ -g -o simulador main.o utils.o dataMemory.o controlUnit.o fileProgram.o tapeFile.o programMemory.o indirect.o direct.o inmediate.o add.o div.o mult.o sub.o halt.o read.o write.o jgtz.o jump.o jzero.o load.o store.o

main.o: ../src/main.cc
	g++ -g -c ../src/main.cc

controlUnit.o: ../src/lib/controlUnit/controlUnit.cc
	g++ -g -c ../src/lib/controlUnit/controlUnit.cc

fileProgram.o: ../src/lib/files/fileProgram/fileProgram.cc
	g++ -g -c ../src/lib/files/fileProgram/fileProgram.cc

tapeFile.o: ../src/lib/files/tapeFile/tapeFile.cc
	g++ -g -c ../src/lib/files/tapeFile/tapeFile.cc

utils.o: ../src/lib/functions/utils.cc
	g++ -g -c ../src/lib/functions/utils.cc

dataMemory.o: ../src/lib/memories/dataMemory/dataMemory.cc
	g++ -g -c ../src/lib/memories/dataMemory/dataMemory.cc

programMemory.o: ../src/lib/memories/programMemory/programMemory.cc
	g++ -g -c ../src/lib/memories/programMemory/programMemory.cc

indirect.o: ../src/lib/operands/indirect/indirect.cc
	g++ -g -c ../src/lib/operands/indirect/indirect.cc

direct.o: ../src/lib/operands/direct/direct.cc
	g++ -g -c ../src/lib/operands/direct/direct.cc

inmediate.o: ../src/lib/operands/inmediate/inmediate.cc
	g++ -g -c ../src/lib/operands/inmediate/inmediate.cc

add.o: ../src/lib/instructions/arithmeticInstructions/add/add.cc
	g++ -g -c ../src/lib/instructions/arithmeticInstructions/add/add.cc

div.o: ../src/lib/instructions/arithmeticInstructions/div/div.cc
	g++ -g -c ../src/lib/instructions/arithmeticInstructions/div/div.cc

mult.o: ../src/lib/instructions/arithmeticInstructions/mult/mult.cc
	g++ -g -c ../src/lib/instructions/arithmeticInstructions/mult/mult.cc

sub.o: ../src/lib/instructions/arithmeticInstructions/sub/sub.cc
	g++ -g -c ../src/lib/instructions/arithmeticInstructions/sub/sub.cc

halt.o: ../src/lib/instructions/inputOutpuInstructions/halt/halt.cc
	g++ -g -c ../src/lib/instructions/inputOutpuInstructions/halt/halt.cc

read.o: ../src/lib/instructions/inputOutpuInstructions/read/read.cc
	g++ -g -c ../src/lib/instructions/inputOutpuInstructions/read/read.cc

write.o: ../src/lib/instructions/inputOutpuInstructions/write/write.cc
	g++ -g -c ../src/lib/instructions/inputOutpuInstructions/write/write.cc

jgtz.o: ../src/lib/instructions/jumpInstructions/jgtz/jgtz.cc
	g++ -g -c ../src/lib/instructions/jumpInstructions/jgtz/jgtz.cc

jump.o: ../src/lib/instructions/jumpInstructions/jump/jump.cc
	g++ -g -c ../src/lib/instructions/jumpInstructions/jump/jump.cc

jzero.o: ../src/lib/instructions/jumpInstructions/jzero/jzero.cc
	g++ -g -c ../src/lib/instructions/jumpInstructions/jzero/jzero.cc

load.o: ../src/lib/instructions/memoryManipulationInstrucctions/load/load.cc
	g++ -g -c ../src/lib/instructions/memoryManipulationInstrucctions/load/load.cc

store.o: ../src/lib/instructions/memoryManipulationInstrucctions/store/store.cc
	g++ -g -c ../src/lib/instructions/memoryManipulationInstrucctions/store/store.cc




clean:
	rm -rf *.o simulador