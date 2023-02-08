/**
 * @file jzero.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction jzero
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../jumpInstruction.h"

class Jzero : public JumpInstruction {
 public:
  Jzero(int lineOfLabel) : JumpInstruction(lineOfLabel) {};
  int function(DataMemory&);
};