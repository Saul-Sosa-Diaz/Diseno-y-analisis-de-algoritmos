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

#include "../instruction.h"

class InputOutputInstruction : public Instruction {
 public:
  InputOutputInstruction() : Instruction(io) {};
  virtual int function(DataMemory&) = 0;
};