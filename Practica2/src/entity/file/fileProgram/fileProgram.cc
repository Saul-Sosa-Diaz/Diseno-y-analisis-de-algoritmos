/**
 * @file fileProgram.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of FileProgram
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "fileProgram.h"

FileProgram::FileProgram(std::string name) : File(name) {
  std::regex nameProgramRam(".*\\.ram");
  if (!std::regex_match(name, nameProgramRam)) {
    std::string exception = "The file with the program RAM doesn´t match with: namein.ram\n";
    throw std::runtime_error(exception);
  }
};

int FileProgram::read() {
  return 1;
}
