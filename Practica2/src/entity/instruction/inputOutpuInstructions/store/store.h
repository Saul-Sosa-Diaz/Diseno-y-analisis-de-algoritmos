/**
 * @file store.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction store
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../inputOutputInstruction.h"

class Store : public InputOutputInstruction {
 public:
  Store();
  int function(DataMemory&);

 private:
};