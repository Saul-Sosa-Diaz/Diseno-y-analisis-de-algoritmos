/**
 * @file load.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of Instruction load
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "load.h"

Load::Load(Operand* operand) : MemoryManipulationInstrucction(operand){}

/**
*/
int Load::function(DataMemory& registers) {
  registers.setValue(operand_->getValue(registers));
  return 0;
}

std::string Load::to_s() const {
  return "Load " + operand_->to_s(); 
}