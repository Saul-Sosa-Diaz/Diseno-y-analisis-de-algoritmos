/**
 * @file programMemory.h
 * @author Saul Sosa Diaz
 * @brief definition of the  programMemory
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include <map>
#include <regex>
#include <string>

#include "../../files/fileProgram/fileProgram.h"
#include "../../instructions/arithmeticInstructions/add/add.h"
#include "../../instructions/arithmeticInstructions/div/div.h"
#include "../../instructions/arithmeticInstructions/mult/mult.h"
#include "../../instructions/arithmeticInstructions/sub/sub.h"
#include "../../instructions/halt/halt.h"
#include "../../instructions/inputOutpuInstructions/read/read.h"
#include "../../instructions/inputOutpuInstructions/write/write.h"
#include "../../instructions/instruction.h"
#include "../../instructions/jumpInstructions/jgtz/jgtz.h"
#include "../../instructions/jumpInstructions/jump/jump.h"
#include "../../instructions/jumpInstructions/jzero/jzero.h"
#include "../../instructions/memoryManipulationInstrucctions/load/load.h"
#include "../../instructions/memoryManipulationInstrucctions/store/store.h"
#include "../../operands/direct/direct.h"
#include "../../operands/indirect/indirect.h"
#include "../../operands/inmediate/inmediate.h"
#include "../memory.h"

enum SpecificOperator {
  LOAD = 0,
  STORE = 1,
  ADD = 2,
  SUB = 3,
  MULT = 4,
  DIV = 5,
  READ = 6,
  WRITE = 7,
  JUMP = 8,
  JZERO = 9,
  JGTZ = 10,
  HALT = 11
};

class ProgramMemory : public Memory<Instruction*> {
 public:
  ProgramMemory(std::string nameOfTheFileWithProgram = "defaultValue", std::string nameOfTheTapeFileIn = "defaultValue", std::string nameOfTheTapeFileOut = "defaultValue");
  void load();
  bool parseLine(std::string);
  bool parsing(std::string);
  bool checkForLabel(std::string, int);
  SpecificOperator getTypeOfOperator(std::string);
  Operand* getOperand(std::string);
  Instruction* getInstruction(std::string, SpecificOperator, Operand*);
  int getNumberOfInstructions() { return content_.size(); }
  TapeFile* getTapeFileIn() { return tapeFileIn_;}
  TapeFile* getTapeFileOut() { return tapeFileOut_;}
  std::vector<Instruction*> getContent() { return content_; }

 private:
  std::string nameOfTheFileWithProgram_;
  TapeFile* tapeFileIn_;
  TapeFile* tapeFileOut_;
  std::map<std::string, int> labels_;
};