/**
 * @file programMemory.cc
 * @author Saul Sosa Diaz
 * @brief IMplementation of the programMemory class
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "dataMemory.h"

DataMemory::DataMemory(int numberOfRegisters) {
  content_.resize(numberOfRegisters);
}

void DataMemory::load() {
  std::fill(content_.begin(), content_.end(), 0);
}