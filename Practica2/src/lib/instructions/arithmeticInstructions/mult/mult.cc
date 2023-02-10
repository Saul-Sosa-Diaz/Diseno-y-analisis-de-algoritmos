/**
 * @file mult.h
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction mult
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "mult.h"

Mult::Mult(Operand* operand) : ArithmeticInstruction(operand) {}

int Mult::function(DataMemory& registers) {
  int temp = registers.at(0) * operand_->getValue(registers);
  registers.setValue(temp);
  return 0;
}