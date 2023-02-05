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


class Instruction {
 public:
  virtual int function() = 0;

 protected:
  std::string type_;
  //Operation*

};