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

Write::Write(TapeFile& file) {}

int Write::function(DataMemory& registers) {
  file_->write(registers.at(operand_->getValue(registers)));
  return 0;
}