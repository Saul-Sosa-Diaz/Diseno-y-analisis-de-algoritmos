/**
 * @file write.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction write
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "write.h"

Write::Write(TapeFile& file) : InputOutputInstruction(file) {}

int Write::function(DataMemory& registers) {
  file_.addNewItemToBuffer(registers.at(operand_->getValue(registers)));
  file_.write();
  return 0;
}