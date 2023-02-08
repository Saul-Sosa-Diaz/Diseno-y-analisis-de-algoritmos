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

#include "../jumpInstruction.h"

class Jgtz : public JumpInstruction {
 public:
  Jgtz(int lineOfLabel) : JumpInstruction(lineOfLabel) {};
  int function(DataMemory&);
};