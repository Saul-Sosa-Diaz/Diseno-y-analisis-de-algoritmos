/**
 * @file mult.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction mult
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include "../arithmeticInstruction.h"

class Mult : public ArithmeticInstruction {
 public:
  Mult(Operand* operand);
  int function(DataMemory&);
 private:
};