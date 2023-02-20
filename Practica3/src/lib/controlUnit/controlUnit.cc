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

    // Mostrar instruction
    std::cout << std::endl
              << "\033[4mInstruction executing:\033[0m\n  " << instruction << std::endl
              << std::endl;

    // Mostrar Memoria de programa
    std::cout << "\033[4mProgram Memory:\033[0m\n"
              << *programMemory_ << std::endl;
    if (instruction->getType() == halt) {
      std::cout << "\033[4mData Memory:\033[0m\n"
                << *dataMemory_ << std::endl
                << std::endl;
      instruction->function(*dataMemory_);
      break;

    } else if (instruction->getType() == jump) {
      int testJump = instruction->function(*dataMemory_);  // Check that the jump is performed
      if (testJump != -1) {
        PC_ = testJump;
        std::cout << "\033[4mData Memory:\033[0m\n"
                  << *dataMemory_ << std::endl
                  << std::endl;
        std::cout << std::endl
                  << "\033[1;33m<-------------------------------------------------------------------------------------------->\033[0m" << std::endl;
        continue;
      }
    } else {
      instruction->function(*dataMemory_);
    }

    // Mostrar Data memory
    std::cout << "\033[4mData Memory:\033[0m\n"
              << *dataMemory_ << std::endl
              << std::endl;
    std::cout << std::endl
              << "\033[1;33m<-------------------------------------------------------------------------------------------->\033[0m" << std::endl;
    PC_++;
  }

  // Display the number of instructions performed if debug mode is 1
  if (debugMode_ > 0) {
    std::cout << "\033[1;35mThe number of instructions where executed: " << numberOfInstructionExecuted << "\033[0m" << std::endl;
  }
}
