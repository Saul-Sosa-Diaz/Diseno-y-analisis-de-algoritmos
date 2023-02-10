/**
 * @file arithmeticInstruction.h
 * @author Saul Sosa Diaz
 * @brief Declaration of abstract class ArithmeticInstruction
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../instruction.h"

class ArithmeticInstruction : public Instruction {
 public:
  ArithmeticInstruction(Operand* operand) : Instruction(arithmetic, operand) {};
  virtual int function(DataMemory&) = 0;
};