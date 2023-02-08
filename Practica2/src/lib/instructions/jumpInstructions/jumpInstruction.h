/**
 * @file jumpInstruction.h
 * @author Saul Sosa Diaz
 * @brief Declaration of abstract class jumpInstruction
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../instruction.h"

class JumpInstruction : public Instruction {
 public:
  JumpInstruction(int lineOfLabel) : Instruction(jump) { lineOfLabel_ = lineOfLabel;};
  virtual int function(DataMemory&) = 0;
 protected:
  int lineOfLabel_;
};