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

Jgtz::Jgtz(type type, int lineOfLabel) : Instruction(type) { lineOfLabel_ = lineOfLabel; }

int Jgtz::function(DataMemory& registers) {
  return lineOfLabel_;
}