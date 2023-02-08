/**
 * @file read.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction read
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include "../inputOutputInstruction.h"

class Read : public InputOutputInstruction {
 public:
  Read(TapeFile& file);
  int function(DataMemory&);

};