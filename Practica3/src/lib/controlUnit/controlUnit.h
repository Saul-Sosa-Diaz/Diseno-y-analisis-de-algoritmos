/**
 * @file controlUnit.h
 * @author Saul Sosa Diaz
 * @brief Definition of the controlUnit, it will be the heart of the RAM machine.
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include <stdlib.h>

#include "../memories/dataMemory/dataMemory.h"
#include "../memories/programMemory/programMemory.h"

class ControlUnit {
 public:
  ControlUnit(ProgramMemory*, DataMemory*, int debugmode = 0);
  void run();

 private:
  int PC_;
  ProgramMemory* programMemory_;
  DataMemory* dataMemory_;
  int numberOfInstructions_;
  int debugMode_;
};
