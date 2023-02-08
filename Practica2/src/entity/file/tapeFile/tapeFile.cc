/**
 * @file tapeFile.cc
 * @author Saul Sosa Diaz
 * @brief Implementation of tapeFile
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "tapeFile.h"

TapeFile::TapeFile(std::string name) : File(name) {
  std::regex legalTapeFileIn(".*\\.in");
  std::regex legalTapeFileOut(".*\\.out");
  std::vector<int> buffer;
  buffer_ = buffer;
  if (!std::regex_match(name, legalTapeFileIn) && !std::regex_match(name, legalTapeFileOut)) {  // Comprobar que es un archivo legal
    std::string exception = "The file with the program RAM doesn´t match with: namein.in or nameout.out\n";
    throw std::runtime_error(exception);
  }
  in_ = std::regex_match(name, legalTapeFileIn) ? true : false;  // Comprobar si es de entrada o salida
  readHead_ = in_ ? 0 : NULL;
};

int TapeFile::read() {
  if (in_) {  // Solo leer si el fichero es de entrada
    std::fstream filein;
    filein.open(name_, std::ios_base::in);
    if (filein.is_open()) {
    } else {
      std::string info_error;
      info_error = name_ + " cannot be opened";
      throw std::system_error(errno, std::system_category(), info_error);
    }
    filein.close();
  } else {
    std::string exception = "Attempting to read in a write file\n";
    throw std::runtime_error(exception);
  }
  return 0;
}

int TapeFile::write() {
  if (!in_) {  // Solo escribir si el fichero es de salida
    std::fstream fileOut;
    fileOut.open(name_, std::ios_base::app);
    if (fileOut.is_open()) {
      for (int i = 0; i < buffer_.size(); i++) {
        fileOut << buffer_[i] << " ";
      }
    } else {
      std::string info_error;
      info_error = name_ + " cannot be opened";
      throw std::system_error(errno, std::system_category(), info_error);
    }
    buffer_.clear();  // limpiar el buffer después de escribir
    fileOut.close();
  } else {
    std::string exception = "Attempting to write in a read file\n";
    throw std::runtime_error(exception);
  }
  return 0;
}