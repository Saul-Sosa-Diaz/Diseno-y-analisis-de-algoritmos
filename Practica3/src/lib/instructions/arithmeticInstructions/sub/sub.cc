/**
 * @file sub.h
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction sub
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "sub.h"

Sub::Sub(Operand* operand) : ArithmeticInstruction(operand) {}

int Sub::function(DataMemory& registers) {
  int temp = registers.at(0) - operand_->getValue(registers);
  registers.setValue(temp);
  return 0;
}

std::string Sub::to_s() const {
  return "Sub " + operand_->to_s(); 
}