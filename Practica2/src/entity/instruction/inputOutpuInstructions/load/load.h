/**
 * @file load.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction load
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../inputOutputInstruction.h"

class Load : public InputOutputInstruction {
 public:
  Load();
  int function(DataMemory&);

 private:
};