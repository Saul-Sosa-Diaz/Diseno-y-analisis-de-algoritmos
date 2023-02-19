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

#include "../memories/dataMemory/dataMemory.h"
#include "../operands/operand.h"

enum type {
  jump = 0,
  halt = 1,
  io = 2,
  memory = 3,
  arithmetic = 4
};

class Instruction {
 public:
  Instruction(type type, Operand* operand) {type_ = type; operand_ = operand; };
  virtual int function(DataMemory&) = 0;
  virtual std::string to_s() const = 0;
  type getType() { return type_; }
  std::string getTypeDebug();

  friend std::ostream &operator<<(std::ostream &output, const Instruction*);

 protected:
  type type_;
  Operand* operand_;
};

