/**
 * @file halt.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction halt
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../inputOutputInstruction.h"

class Halt : public InputOutputInstruction {
 public:
  Halt(TapeFile* file);
  int function(DataMemory&);
};