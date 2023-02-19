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

#include "../instruction.h"

class Halt : public Instruction {
 public:
  Halt();
  int function(DataMemory&);
  std::string to_s() const;
};