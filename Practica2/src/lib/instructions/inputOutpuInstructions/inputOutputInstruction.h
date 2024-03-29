/**
 * @file inputOutputInstruction.h
 * @author Saul Sosa Diaz
 * @brief Declaration of abstract class inputOutputInstruction
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include "../../files/tapeFile/tapeFile.h"
#include "../instruction.h"


class InputOutputInstruction : public Instruction {
 public:
  InputOutputInstruction(TapeFile* file, Operand* operand) : Instruction(io, operand) { file_ = file;};
  virtual int function(DataMemory&) = 0;
  
 protected:
  TapeFile* file_;
};