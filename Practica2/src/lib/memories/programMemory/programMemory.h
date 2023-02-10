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

#include "../../files/fileProgram/fileProgram.h"
#include "../../instructions/instruction.h"
#include "../memory.h"

enum SpecificInstruction {
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
  ProgramMemory(std::string);
  void load();
  bool parseLine(std::string);
  void checkForLabel(std::string, int numberOfLine);
  SpecificInstruction getTypeOfInstrucction(std::string test);

 private:
  std::string nameOfTheFileWithProgram_;
  std::map<std::string, int> labels_;
};