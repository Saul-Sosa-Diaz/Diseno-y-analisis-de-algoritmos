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
#include <regex>

#include "../file.h"

class FileProgram : public File {
 public:
  FileProgram(std::string name);
  int read(); 
  std::string getSrcCode() {return srcCode_;}
  int getNumberOfLines() {return numberOfLines_;}
 protected:
  std::string srcCode_;
  int numberOfLines_;
};