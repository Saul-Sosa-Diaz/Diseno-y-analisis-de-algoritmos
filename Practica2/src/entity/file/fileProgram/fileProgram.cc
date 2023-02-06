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
  srcCode_ = "";
  numberOfLines_ = 0;
  if (!std::regex_match(name, nameProgramRam)) {
    std::string exception = "The file with the program RAM doesn´t match with: namein.ram\n";
    throw std::runtime_error(exception);
  }
};

int FileProgram::read() {
  std::fstream filein;
  filein.open(name_, std::ios_base::in);
  if (filein.is_open()) {
    std::string aux = "";
    while (getline(filein, aux)) {
      transform(aux.begin(), aux.end(), aux.begin(), ::toupper);  // Convert into caps
      srcCode_ += aux + "\n";
      numberOfLines_++;
    }
  } else {
    std::string info_error;
    info_error = name_ + " cannot be opened";
    throw std::system_error(errno, std::system_category(), info_error);
  }
  filein.close();
  return 0;
}