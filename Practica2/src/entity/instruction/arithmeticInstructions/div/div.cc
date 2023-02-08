/**
 * @file div.h
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction div
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "div.h"

Div::Div() {}

int Div::function(DataMemory& registers) {
  int temp = registers.at(0) / operand_->getValue(registers);
  registers.setValue(temp);
  return 0;
}