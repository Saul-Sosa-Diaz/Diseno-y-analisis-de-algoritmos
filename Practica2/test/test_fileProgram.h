#include "var_tests.h"

#include "../src/entity/file/fileProgram/fileProgram.h"

void constructor_file_program_fail() {
  TEST_DONE++;
  try {
    FileProgram datamemo("aaaaram");
  } catch (const std::exception& e) {
    TEST_PASSED++;
    return;
  }
  TEST_FAILED++;
}

void constructor_file_program() {
  TEST_DONE++;
  try {
    FileProgram datamemo("program.ram");
  } catch (const std::exception& e) {
    std::cout << "Error Constructor\n";
    TEST_FAILED++;
    return;
  }
  TEST_PASSED++;
}


void test_file_program() {
  constructor_file_program();
  constructor_file_program_fail();
}