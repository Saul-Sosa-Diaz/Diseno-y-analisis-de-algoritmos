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
#include <regex>

#include "../../files/fileProgram/fileProgram.h"
#include "../../instructions/instruction.h"
#include "../memory.h"

class ProgramMemory : public Memory<Instruction*> {
 public:
  ProgramMemory(std::string);
  void load();
  bool parseLine(std::string);

 private:
  std::string nameOfTheFileWithProgram_;
};