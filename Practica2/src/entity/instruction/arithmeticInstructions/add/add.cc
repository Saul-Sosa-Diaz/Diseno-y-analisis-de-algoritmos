/**
 * @file add.h
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction add
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "add.h"

Add::Add() {}

int Add::function(DataMemory& registers) {
  double temp = registers.at(0) + operand_->getValue(registers);
  registers.setValue(temp);
  return 0;
}