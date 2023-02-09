#pragma once

#include <iostream>
template <class T>
bool ASSERT_EQ(const T& t1, const T& t2) {
  if (t1 != t2) {
    throw std::runtime_error("Error de comparación de " + std::to_string(t1) + " y " + std::to_string(t2) + "\n");
  }
  return true;
}

bool ASSERT_EQ(const std::string& t1, const std::string& t2) {
  return t1.compare(t2);
}

int TEST_DONE = 0;
int TEST_PASSED = 0;
int TEST_FAILED = 0;
