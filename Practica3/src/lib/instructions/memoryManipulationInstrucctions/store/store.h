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

#include "../memoryManipulationInstrucction.h"

class Store : public MemoryManipulationInstrucction {
 public:
  Store(Operand* operand);
  int function(DataMemory&);
  std::string to_s() const;

 private:
};