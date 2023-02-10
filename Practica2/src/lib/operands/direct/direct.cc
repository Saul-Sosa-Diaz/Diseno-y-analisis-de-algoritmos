/**
 * @file direct.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of direct operand
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "direct.h"

int DirectOperand::getValue(const DataMemory& registers) {
  return registers.at(index_);
}
int DirectOperand::getIndex(const DataMemory& registers) {
  return index_;
}