/**
 * @file div.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction div
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include "../arithmeticInstruction.h"

class Div : public ArithmeticInstruction {
 public:
  Div();
  int function(DataMemory&);
 private:
};