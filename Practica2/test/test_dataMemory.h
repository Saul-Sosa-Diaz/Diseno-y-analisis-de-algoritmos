#include "var_tests.h"

#include "../src/lib/memories/dataMemory/dataMemory.h"
#include "../src/lib/operands/inmediate/inmediate.h"
#include "../src/lib/operands/direct/direct.h"
#include "../src/lib/operands/indirect/indirect.h"

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
