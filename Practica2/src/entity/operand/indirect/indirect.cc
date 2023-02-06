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

double IndirectOperand::getValue(const DataMemory& registers) {
  return registers.at(int(registers.at(index_)));
}