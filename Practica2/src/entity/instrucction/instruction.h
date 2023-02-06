/**
 * @file instruction.h
 * @author Saul Sosa Diaz
 * @brief Declaration of abstract class Instruction
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include <string>
#include "../memory/dataMemory/dataMemory.h"
#include "../operand/operand.h"

enum type {
  jump = 0,
  halt = 1,
  io = 2,
  aritmethic = 3
};

class Instruction {
 public:
  Instruction (type type);
  virtual int function(DataMemory&) = 0;

 protected:
  type type_;
  Operand* operand_;

};