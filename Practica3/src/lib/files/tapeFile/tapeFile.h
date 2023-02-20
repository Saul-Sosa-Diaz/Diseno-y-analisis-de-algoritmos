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
  std::string to_s();

 protected:
  std::vector<int> buffer_;
  std::vector<int> tapeOut_; // Elementos que se han impreso en la salida.
  int readHead_;
  bool in_;
  bool finished_; // No ha acabado de leer todavía
};