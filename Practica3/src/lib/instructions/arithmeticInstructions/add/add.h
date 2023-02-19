/**
 * @file add.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction add
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once


#include "../arithmeticInstruction.h"

class Add : public ArithmeticInstruction {
 public:
  Add(Operand* operand);
  int function(DataMemory&);
  std::string to_s() const; 
 private:
};