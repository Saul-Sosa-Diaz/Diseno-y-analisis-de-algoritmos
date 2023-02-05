/**
 * @file memory.cc
 * @author Saul Sosa Diaz
 * @brief definition of the abstract class Memory
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include <vector>

template <class T>
class Memory {
 public:
  virtual void load() = 0;

 protected:
  std::vector<T> content_;
};

