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

Read::Read(TapeFile& file) : InputOutputInstruction(file) {}

int Read::function(DataMemory& registers) {
  registers.writeValue(operand_->getValue(registers), file_.getItem());
  return 0;
}