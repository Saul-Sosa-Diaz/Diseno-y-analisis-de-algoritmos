/**
 * @file halt.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction Halt
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "halt.h"

Halt::Halt(TapeFile* file) : InputOutputInstruction(file, NULL){};

int Halt::function(DataMemory& registers) {
  file_->addNewItemToBuffer(registers.at(0));
  file_->write();
  return 0;
}