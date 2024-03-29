/**
 * @file read.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction read
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "read.h"

Read::Read(TapeFile* file, Operand* operand) : InputOutputInstruction(file, operand) {}

int Read::function(DataMemory& registers) {
  if (operand_->getIndex(registers) == 0) {
    std::string exception = "\033[1;31mTrying to access register 0 with a READ operation\n";
    throw std::runtime_error(exception);
  }
  registers.writeValue(operand_->getIndex(registers), file_->getItem());
  return 0;
}

std::string Read::to_s() const {
  return "Read " + operand_->to_s(); 
}