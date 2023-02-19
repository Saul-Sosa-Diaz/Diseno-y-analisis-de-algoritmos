/**
 * @file jzero.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction jzero
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "jzero.h"

Jzero::Jzero(int lineOfLabel) : JumpInstruction(lineOfLabel) {}

int Jzero::function(DataMemory& registers) {
  int result = -1;
  if (registers.at(0) == 0) {
    result = lineOfLabel_;
  }
  return result;
}

std::string Jzero::to_s() const {
  return "Jzero numberOfLabel(" + std::to_string(lineOfLabel_) + ")"; 
}