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
#include "../memories/programMemory/programMemory.h"
#include "../memories/dataMemory/dataMemory.h"

class ControlUnit {
 public:
  ControlUnit(ProgramMemory&, DataMemory&);
  void run();

 private:
  int PC_;
  ProgramMemory programMemory_;
  DataMemory dataMemory_;
  int numberOfInstructions_;
};
