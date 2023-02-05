#include <iostream>

#include "../src/entity/memory/dataMemory.h"

int TEST_DONE = 0;
int TEST_PASSED = 0;
int TEST_FAILED = 0;

void constructor_data_memory() {
  TEST_DONE++;
  try {
    DataMemory datamemo(32);
  } catch (const std::exception& e) {
    std::cout << "Error Constructor\n";
    TEST_FAILED++;
    return;
  }
  TEST_PASSED++;
}

void load_data_memory() {
  TEST_DONE++;
  try {
    DataMemory datamemo(32);
    datamemo.load();
    auto init = datamemo.getContent();
    for ( int i = 0; i < init.size(); i++) {
      if (init[i] != 0.) {
        throw "Error";
      }
    }
  } catch (const std::exception& e) {
    std::cout << "Error\n";
    TEST_FAILED++;
    return;
  }
  TEST_PASSED++;
}

void test_data_memory() {
  constructor_data_memory();
  load_data_memory();
}

int main(int argc, char** argv) {
  test_data_memory();

  std::cout << "Totales: " << TEST_DONE << std::endl
            << "\033[1;32m"
            << "Pasados: " << TEST_PASSED << std::endl
            << "\033[1;31m"
            << "Fallados: " << TEST_FAILED << std::endl;
  return 0;
}