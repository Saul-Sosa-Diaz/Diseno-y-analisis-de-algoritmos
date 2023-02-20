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
 *        debug mode can be 0, 1, 2
 *
 * @param programMemory
 * @param dataMemory
 */
ControlUnit::ControlUnit(ProgramMemory* programMemory, DataMemory* dataMemory, int debugmode) {
  PC_ = 0;
  programMemory_ = programMemory;
  dataMemory_ = dataMemory;
  debugMode_ = debugmode;
  numberOfInstructions_ = programMemory_->getNumberOfInstructions();
}

/**
 * @brief Main function execute the entire ram program.
 *
 */
void ControlUnit::run() {
  int numberOfInstructionExecuted = 0;

  while (PC_ < numberOfInstructions_) {
    numberOfInstructionExecuted++;
    Instruction* instruction = programMemory_->getContent()[PC_];
    if (debugMode_ == 2) {
      info(instruction);
    }
    if (instruction->getType() == halt) {
      instruction->function(*dataMemory_);
      break;
    } else if (instruction->getType() == jump) {
      int testJump = instruction->function(*dataMemory_);  // Check that the jump is performed
      if (testJump != -1) {
        PC_ = testJump;
        continue;
      }
    } else {
      instruction->function(*dataMemory_);
    }
    PC_++;
  }

  // Display the number of instructions performed if debug mode is 1
  if (debugMode_ > 0) {
    std::cout << "The number of instructions where executed: " << numberOfInstructionExecuted << std::endl;
  }
}

/**
 * @brief Displays machine status information on screen RAM
 *
 */
void ControlUnit::info(const Instruction* instruction) {
  system("clear");
  std::cout << "Instruction executing:\n  " << instruction << std::endl << std::endl;
  std::cout << "Data Memory:\n" <<  *dataMemory_ << std::endl;
  // std::cout << "Program Memory:\n\t" <<  programMemory_ << std::endl;
  std::cout << std::endl << "Press enter to continue:" << std::endl ;
  std::cin.ignore();
  
}
