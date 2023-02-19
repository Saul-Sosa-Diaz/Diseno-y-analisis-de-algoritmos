/**
 * @file jgtz.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction jgtz
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "jgtz.h"

Jgtz::Jgtz(int lineOfLabel) : JumpInstruction(lineOfLabel) {}

int Jgtz::function(DataMemory& registers) {
  int result = -1;
  if (registers.at(0) > 0) {
    result = lineOfLabel_;
  }
  return result;
}

std::string Jgtz::to_s() const {
  return "Jgtz numberOfLabel(" + std::to_string(lineOfLabel_) + ")"; 
}