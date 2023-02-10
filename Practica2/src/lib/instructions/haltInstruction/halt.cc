/**
 * @file halt.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction Halt
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "halt.h"

Halt::Halt() : Instruction(halt, NULL){};

int Halt::function(DataMemory& registers) {
  return 0;
}