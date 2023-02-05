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

class DataMemory : public Memory<double> {
 public:
  DataMemory(int);
  void load();
  std::vector<double> getContent() {
    return content_;
  }

 private:
};