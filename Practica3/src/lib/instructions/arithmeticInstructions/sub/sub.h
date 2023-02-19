/**
 * @file sub.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction sub
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include "../arithmeticInstruction.h"

class Sub : public ArithmeticInstruction {
 public:
  Sub(Operand* operand);
  int function(DataMemory&);
  std::string to_s() const;
 private:
};