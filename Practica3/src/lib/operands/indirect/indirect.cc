/**
 * @file indirect.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of indirect operand
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "indirect.h"

int IndirectOperand::getValue(const DataMemory& registers) {
  return registers.at(registers.at(index_));
}

int IndirectOperand::getIndex(const DataMemory& registers) {
  return registers.at(index_);
}

std::string IndirectOperand::to_s() const{
  return "*" + std::to_string(index_);
}