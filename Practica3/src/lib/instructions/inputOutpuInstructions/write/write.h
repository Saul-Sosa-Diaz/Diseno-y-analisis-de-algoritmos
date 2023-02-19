/**
 * @file write.h
 * @author Saul Sosa Diaz
 * @brief Declaration of Instruction write
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../inputOutputInstruction.h"

class Write : public InputOutputInstruction {
 public:
  Write(TapeFile* file, Operand* operand);
  int function(DataMemory&);
  std::string to_s() const;
};
