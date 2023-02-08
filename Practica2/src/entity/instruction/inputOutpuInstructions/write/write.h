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

#include "../../../file/tapeFile/tapeFile.h"
#include "../inputOutputInstruction.h"

class Write : public InputOutputInstruction {
 public:
  Write(TapeFile& file);
  int function(DataMemory&);
};