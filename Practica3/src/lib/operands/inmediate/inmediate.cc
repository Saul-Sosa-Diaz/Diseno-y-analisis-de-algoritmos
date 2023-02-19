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

int InmediateOperand::getValue(const DataMemory& registers) {
  return index_;
}
 int InmediateOperand::getIndex(const DataMemory& registers) {
  return index_;
 };

std::string InmediateOperand::to_s() const{
  return "="+std::to_string(index_);
}