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

void getSrcCode() {
  TEST_DONE++;
  try {
    FileProgram datamemo("prueba.ram");
    datamemo.read();
    ASSERT_EQ(datamemo.getSrcCode(), 
      "ETIQ: GRTZ 01\n"
      "HALT 69\n"
      "ADD  *3"
    );
  } catch (const std::exception& e) {
    std::cout << "getSrcCode\n";
    TEST_FAILED++;
    return;
  }
  TEST_PASSED++;
}

void getNumberOfLines() {
  TEST_DONE++;
  try {
    FileProgram datamemo("prueba.ram");
    datamemo.read();
    ASSERT_EQ(datamemo.getNumberOfLines(),3);
  } catch (const std::exception& e) {
    std::cout << "getNumberOfLines\n";
    TEST_FAILED++;
    return;
  }
  TEST_PASSED++;
}

void test_file_program() {
  constructor_file_program();
  constructor_file_program_fail();
  getSrcCode();
  getNumberOfLines();
}