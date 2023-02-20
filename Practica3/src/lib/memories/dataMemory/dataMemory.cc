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
  reducedSize_ = 0;
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
  if (index > reducedSize_) {
    reducedSize_ = index;
  }
  content_[index] = value;
}

std::ostream &operator<<(std::ostream &output, const DataMemory &dataMemory) {
  tabulate::Table registers;
  registers.add_row(tabulate::Table::Row_t{"Registers","Data"});
  for (int i = 0; i <= dataMemory.reducedSize_; i++) {
    registers.add_row(tabulate::Table::Row_t{"R"+std::to_string(i),std::to_string(dataMemory.content_[i])});
  }
  output << registers;
  return output;
}