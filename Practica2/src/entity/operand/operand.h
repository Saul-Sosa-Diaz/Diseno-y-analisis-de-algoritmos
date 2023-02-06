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


class Operand {
 public:
  virtual double value(DataMemory&) = 0;

 protected:

};