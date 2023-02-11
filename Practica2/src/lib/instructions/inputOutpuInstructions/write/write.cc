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

Write::Write(TapeFile* file, Operand* operand) : InputOutputInstruction(file, operand) {}

int Write::function(DataMemory& registers) {
  if (operand_->getIndex(registers) == 0) {
    std::string exception = "Trying to access register 0 with a WRITE operation\n";
    throw std::runtime_error(exception);
  }
  file_->addNewItemToBuffer(registers.at(operand_->getIndex(registers)));
  file_->write();
  return 0;
}