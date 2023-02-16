/**
 * @file controlUnit.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction controlUnit
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "controlUnit.h"

/**
 * @brief Construct a new Control Unit:: Control Unit object
 *
 * @param programMemory
 * @param dataMemory
 */
ControlUnit::ControlUnit(ProgramMemory* programMemory, DataMemory* dataMemory) {
  PC_ = 0;
  programMemory_ = programMemory;
  dataMemory_ = dataMemory;
  numberOfInstructions_ = programMemory_->getNumberOfInstructions();
}

/**
 * @brief Main function execute the entire ram program.
 *
 */
void ControlUnit::run() {
  while (PC_ < numberOfInstructions_)  {
    Instruction* instruction = programMemory_->getContent()[PC_];
    if (instruction->getType() == halt) {
      instruction->function(*dataMemory_);
      return;
    } else if (instruction->getType() == jump) {
      int testJump = instruction->function(*dataMemory_); // Check that the jump is performed
      if (testJump != -1) {
        PC_ = testJump;
        continue;
      } 
    } else  {
      instruction->function(*dataMemory_);
    }
    PC_++;
  }
}