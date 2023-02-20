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
  int addToBuff = 0;
  if (operand_->getType() == inmediate) {
    addToBuff = operand_->getIndex(registers);
  } else {
    if (operand_->getIndex(registers) == 0) {
      std::string exception = "\033[1;31mTrying to access register 0 with a WRITE operation\n";
      throw std::runtime_error(exception);
    }
    addToBuff = registers.at(operand_->getIndex(registers));
  }
  file_->addNewItemToBuffer(addToBuff);
  file_->write();
  return 0;
}

std::string Write::to_s() const {
  return "Write " + operand_->to_s(); 
}