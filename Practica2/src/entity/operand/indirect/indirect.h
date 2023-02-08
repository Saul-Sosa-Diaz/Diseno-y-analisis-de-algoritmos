/**
 * @file indirect.h
 * @author Saul Sosa Diaz
 * @brief Declaration of indirect operand 
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../operand.h"

class IndirectOperand : public Operand {
 public:
  IndirectOperand(int index) : Operand(index){};
  int getValue(const DataMemory&);
 private:
};