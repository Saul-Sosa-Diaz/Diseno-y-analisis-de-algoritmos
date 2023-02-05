/**
 * @file file.h
 * @author Saul Sosa Diaz
 * @brief Declaration of abstract class File
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include <fstream>
#include <string>

class File {
 public:
  File(std::string name) { name_ = name; }
  virtual int read() = 0;

 protected:
  std::string name_;
  // Operation*
};