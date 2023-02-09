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
  std::string regex;
  regex = "^\\s*([A-Z][A-Z0-9]*[[:blank:]]*:)?[[:blank:]]*"; // Labels must be at the beginning of the line and not start with a number.
  regex += "(";
    regex += "((ADD|SUB|DIV|MULT)\\s*((=[0-9]+)|([0-9]+)|(\\*[0-9]+)))|"; // Arithmetic instruction
    regex += "(HALT)|"; //HALT
    regex += "((JUMP|JGTZ|JZERO)[[:blank:]]*[A-Z][A-Z0-9]*)|"; //JUMP
    regex += "((WRITE|READ)\\s*(([0-9]+)|(\\*[0-9]+)))|"; //InputOutput
    regex += "(STORE\\s*(([0-9]+)|(\\*[0-9]+)))|";  // Store
    regex += "(LOAD\\s*((=[0-9]+)|([0-9]+)|(\\*[0-9]+)))"; // Load
  regex += ")";
  regex += "[[:blank:]]*\\n"; 

  std::regex grammar(regex);
  if (std::regex_match(lineToParse, grammar)) {
    return true;
  } else {
    return false;
  }
}