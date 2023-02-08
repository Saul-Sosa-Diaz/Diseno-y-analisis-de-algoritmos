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
#include "../memory.h"
#include "../instrucction/instruction.h"
#include "../file/fileProgram/fileProgram.h"

class ProgramMemory : public Memory<Instruction*> {
 public:
  ProgramMemory(std::string);
  void load();
  std::vector<Instruction*> getContent() {
    return content_;
  }
 private:
  FileProgram program_;
};