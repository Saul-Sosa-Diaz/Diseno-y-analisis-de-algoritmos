/**
 * @file inputOutputInstruction.h
 * @author Saul Sosa Diaz
 * @brief Declaration of abstract class memoryManipulationInstrucction
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../instruction.h"

class MemoryManipulationInstrucction : public Instruction {
 public:
  MemoryManipulationInstrucction(Operand* operand) : Instruction(memory, operand){};
  virtual int function(DataMemory&) = 0;
};