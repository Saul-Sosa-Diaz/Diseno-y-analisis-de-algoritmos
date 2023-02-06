/**
 * @file inmediate.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of inmediate operand
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "inmediate.h"

double InmediateOperand::getValue(const DataMemory& registers) {
  return index_;
}