/**
 * @file programMemory.cc
 * @author Saul Sosa Diaz
 * @brief IMplementation of the programMemory class
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */

#include "programMemory.h"

ProgramMemory::ProgramMemory(std::string nameOfTheFileWithProgram) {
  nameOfTheFileWithProgram_ = nameOfTheFileWithProgram;
}

void ProgramMemory::load() {
  FileProgram program(nameOfTheFileWithProgram_);
  std::string srcCode = program.getSrcCode();
}


/**
 * @brief Analyzes if a program line can be constructed
 * 
 * @param lineToParse string to test
 * @return bool true if the sentence can be constructed
 */
bool ProgramMemory::parseLine(std::string lineToParse) {
  std::regex label("^\\s*[A-Z][A-Z0-9]*:.*"); // Labels must be at the beginning of the line and not start with a number.
  std::regex arithmetic("(ADD|LOAD|DIV|MULT)\s*((=[0-9]+)|([0-9]+)|(\*[0-9]+))\n")


  if () {
    return true
  } else {
    return false
  }
}