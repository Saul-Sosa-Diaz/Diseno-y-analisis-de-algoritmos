/**
 * @file dataMemory.h
 * @author Saul Sosa Diaz
 * @brief definition of the  programMemory
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include "../memory.h"

class DataMemory : public Memory<int> {
 public:
  DataMemory(int n = 32);
  void load();
  std::vector<int> getContent() {
    return content_;
  }
  int at(int) const;
  void setValue(int);
  void writeValue(int, int);
 private:
};