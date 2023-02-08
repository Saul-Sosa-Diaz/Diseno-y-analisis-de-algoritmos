/**
 * @file tapeFile.h
 * @author Saul Sosa Diaz
 * @brief Declaration of class tapeFile
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once
#include <vector>
#include <regex>

#include "../file.h"

class TapeFile : public File {
 public:
  TapeFile(std::string name = "defaultName");
  int read();
  int write();
  void addNewItemToBuffer(int);
  int getItem();

 protected:
  std::vector<int> buffer_;
  int readHead_;
  bool in_;
};