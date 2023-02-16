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
  read();
};

int FileProgram::read() {
  std::fstream filein;
  filein.open(name_, std::ios_base::in);
  if (filein.is_open()) {
    std::string aux = "";
    std::regex uselessLine("(\\s*#.*)|(^\\s*$)"); // Identify comment line or blank line
    while (getline(filein, aux)) {
      if (!std::regex_match(aux, uselessLine)) { // insert only useful lines
        transform(aux.begin(), aux.end(), aux.begin(), ::toupper);  // Convert into caps
        aux.erase(std::remove(aux.begin(), aux.end(), '\t'), aux.end()); //  Delete \t from string
        srcCode_ += aux + "\n";
        numberOfLines_++;
      }
    }
  } else {
    std::string info_error;
    info_error = name_ + " cannot be opened";
    throw std::system_error(errno, std::system_category(), info_error);
  }
  filein.close();
  return 0;
}