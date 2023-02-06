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
#include "../memory/dataMemory/dataMemory.h"

template <class T>
class Operand {
 public:
  Operand( T& index) { index_ = index; }
  virtual double getValue(const DataMemory&) = 0;

 protected:
  T index_;
};