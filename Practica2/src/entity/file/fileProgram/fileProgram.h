/**
 * @file fileProgram.h
 * @author Saul Sosa Diaz
 * @brief Declaration of class FileProgram
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include "../file.h"
#include <regex>

class FileProgram : public File {
 public:
  FileProgram(std::string name);
  int read(); // IMPLEMENTAR!!!!

 protected:
  std::string name_;
  // Operation*
};