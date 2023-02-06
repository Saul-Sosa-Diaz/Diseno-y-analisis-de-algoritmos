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

double DataMemory::at(int index) const {
  if (index < 0 || index >= content_.size()) {
    throw std::runtime_error("Attempt to access incorrect memory address");
  }
  return content_[index];
}

void DataMemory::setValue(double newValue) {
  content_[0] = newValue;
}

void DataMemory::writeValue(int index, double value) {
  content_[index] = value;
}