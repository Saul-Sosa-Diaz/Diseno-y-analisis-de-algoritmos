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
  load();
}

void DataMemory::load() {
  std::fill(content_.begin(), content_.end(), 0);
}

int DataMemory::at(int index) const {
  if (index < 0 || index >= content_.size()) {
    throw std::runtime_error("Attempt to access incorrect memory address");
  }
  return content_[index];
}

void DataMemory::setValue(int newValue) {
  content_[0] = newValue;
}

void DataMemory::writeValue(int index, int value) {
  content_[index] = value;
}