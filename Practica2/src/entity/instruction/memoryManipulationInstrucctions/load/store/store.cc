/**
 * @file store.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction store
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "store.h"

Store::Store() {}

int Store::function(DataMemory& registers) {
  registers.writeValue(operand_->getValue(registers), registers.at(0));
  return 0;
}