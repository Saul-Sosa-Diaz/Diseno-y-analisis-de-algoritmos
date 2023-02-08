/**
 * @file operand.h
 * @author Saul Sosa Diaz
 * @brief Declaration of abstract class Instruction
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include "../memories/dataMemory/dataMemory.h"

class Operand {
 public:
  Operand(int index) { index_ = index; }
  virtual int getValue(const DataMemory&) = 0;

 protected:
  int index_;
};