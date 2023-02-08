/**
 * @file jgtz.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction jgtz
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../instruction.h"

class ArithmeticInstruction : public Instruction {
 public:
  ArithmeticInstruction(type type = arithmetic) : Instruction(type) {};
  virtual int function(DataMemory&) = 0;
};