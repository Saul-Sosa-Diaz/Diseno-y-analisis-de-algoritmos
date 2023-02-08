/**
 * @file jump.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction jump
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../jumpInstruction.h"

class Jump : public JumpInstruction {
 public:
  Jump(int lineOfLabel) : JumpInstruction(lineOfLabel) {};
  int function(DataMemory&);
};