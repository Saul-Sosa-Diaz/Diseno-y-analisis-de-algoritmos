/**
 * @file jump.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction jump
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "jump.h"

Jump::Jump(int lineOfLabel) : JumpInstruction(lineOfLabel) {}

int Jump::function(DataMemory& registers) {
  return lineOfLabel_;
}