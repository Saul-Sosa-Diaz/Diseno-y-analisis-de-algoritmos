/**
 * @file direct.h
 * @author Saul Sosa Diaz
 * @brief Declaration of direct operand 
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../operand.h"

class DirectOperand : public Operand {
 public:
  DirectOperand(int index) : Operand(index){};
  double getValue(const DataMemory&);
 private:
};