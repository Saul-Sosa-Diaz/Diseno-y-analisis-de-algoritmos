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
enum typeOfOperand {
  direct = 0,
  inmediate = 1,
  indirect = 2
};

class Operand {
 public:
  Operand(int index, typeOfOperand type) {
    index_ = index;
    type_ = type;
  }
  virtual int getValue(const DataMemory&) = 0;
  virtual int getIndex(const DataMemory&) = 0;
  typeOfOperand getType() { return type_; }

 protected:
  int index_;
  typeOfOperand type_;
};