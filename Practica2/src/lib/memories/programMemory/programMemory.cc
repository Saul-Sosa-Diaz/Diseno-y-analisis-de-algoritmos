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

/**
 * @brief Load the file and create the instructions
 *
 */
void ProgramMemory::load() {
  FileProgram program(nameOfTheFileWithProgram_);
  std::stringstream srcCode(program.getSrcCode());
  std::cout << program.getSrcCode();
  std::string test;
  int numberOfLine = 1;
  while (std::getline(srcCode, test, '\n')) {
    test += '\n';
    if (parseLine(test)) {  // The instruction can be constructed

      // 1) Comprobar si tiene una etiqueta.
      checkForLabel(test, numberOfLine);
      // 2) buscar tipo de instrucción.
      //get
      // 3) Crear la instrucción.
      // 4) Tipo de operando.

    } else {
      std::string exception = "File " + nameOfTheFileWithProgram_ + " has a syntax error in the line " + std::to_string(numberOfLine) + ": ";
      exception += test + "\n";
      throw std::runtime_error(exception);
    }
    numberOfLine++;
  }
}

/**
 * @brief Analyzes if a program line can be constructed
 *
 * @param lineToParse string to test
 * @return bool true if the sentence can be constructed
 */
bool ProgramMemory::parseLine(std::string lineToParse) {
  std::string regex;
  regex = "^\\s*("; 
    regex += "(?!((ADD)|(SUB)|(DIV)|(MULT)|(HALT)|(JUMP)|(JGTZ)|(WRITE)|(READ)|(STORE)|(LOAD)))"; // Check the label is not a reserved word
    regex += "[A-Z][A-Z0-9]*[[:blank:]]*:";
  regex += ")?[[:blank:]]*";  // Labels must be at the beginning of the line and not start with a number.
    regex += "(";
      regex += "((ADD|SUB|DIV|MULT)\\s*((=[0-9]+)|([0-9]+)|(\\*[0-9]+)))|";  // Arithmetic instruction
      regex += "(HALT)|";                                                    // HALT
      regex += "((JUMP|JGTZ|JZERO)[[:blank:]]*[A-Z][A-Z0-9]*)|";             // JUMP
      regex += "((WRITE|READ)\\s*(([0-9]+)|(\\*[0-9]+)))|";                  // InputOutput
      regex += "(STORE\\s*(([0-9]+)|(\\*[0-9]+)))|";                         // Store
      regex += "(LOAD\\s*((=[0-9]+)|([0-9]+)|(\\*[0-9]+)))";                 // Load
    regex += ")";
  regex += "[[:blank:]]*\\n";

  std::regex grammar(regex);
  if (std::regex_match(lineToParse, grammar)) {
    return true;
  } else {
    return false;
  }
}

/**
 * @brief Checks if an instruction has a label
 * 
 * @param test string to test
 * @param numberOfLine number of the line of the program 
 */
void ProgramMemory::checkForLabel(std::string test, int numberOfLine) {
  if (test.find(':') != std::string::npos) {
    std::string aux = test.substr(0, test.find(':'));
    aux.erase(std::remove(aux.begin(), aux.end(), ' '), aux.end());  //  Delete ' ' from string
    
    // Put in the hash, if thow error already exists
    if (labels_[aux] == 0) {
      labels_[aux] = numberOfLine;
    } else {
      std::string exception = "The label" + aux + " already exists\n";
      throw std::runtime_error(exception);
    }
  }
}

/*
SpecificInstruction ProgramMemory::getTypeOfInstrucction(std::string test) {

  if () {
    return LOAD;
  }
  if () {
    return STORE;
  } 
  if () {
    return ADD;
  } 
  if () {
    return SUB;
  } 
  if () {
    return MULT;
  } 
  if () {
    return DIV;
  } 
  if () {
    return READ;
  } 
  if () {
    return WRITE;
  } 
  if () {
    return JUMP;
  } 
  if () {
    return JZERO;
  } 
  if () {
    return JGTZ;
  }
  if () {
    return HALT;
  }   
}
*/