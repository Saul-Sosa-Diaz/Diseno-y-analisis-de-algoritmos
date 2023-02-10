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

ProgramMemory::ProgramMemory(std::string nameOfTheFileWithProgram, std::string nameOfTheTapeFileIn, std::string nameOfTheTapeFileOut) {
  nameOfTheFileWithProgram_ = nameOfTheFileWithProgram;
  nameOfTheTapeFileIn_ = nameOfTheTapeFileIn;
  nameOfTheTapeFileOut_ = nameOfTheTapeFileOut;
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

      // 1) Check if it has a label
      if (checkForLabel(test, numberOfLine)) {
        test = test.substr(test.find(':') + 1, test.size() - 1);
      }
      // 2) search operator type.
      SpecificOperator operato = getTypeOfOperator(test);
      test = test.substr(test.find(' ') + 1, test.size() - 1);

      // 4) Type of operand.
      Operand* operand = getOperand(test);
      // 3) Create the instrucction and push into the content.
      content_.push_back(getInstruction(test, operato, operand));

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
  regex += "(?!((ADD)|(SUB)|(DIV)|(MULT)|(HALT)|(JUMP)|(JGTZ)|(WRITE)|(READ)|(STORE)|(LOAD)))";  // Check the label is not a reserved word
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
 * @return bool true if in the instrucction exists a label
 */
bool ProgramMemory::checkForLabel(std::string test, int numberOfLine) {
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
    return true;
  } else {
    return false;
  }
}

/**
 * @brief Returns the type of the build instruction
 *
 * @param test
 * @return SpecificOperator
 */
SpecificOperator ProgramMemory::getTypeOfOperator(std::string test) {
  std::regex load("LOAD");
  std::regex store("STORE");
  std::regex add("ADD");
  std::regex sub("SUB");
  std::regex mult("MULT");
  std::regex div("DIV");
  std::regex read("READ");
  std::regex write("WRITE");
  std::regex jump("JUMP");
  std::regex jzero("JZERO");
  std::regex jgtz("JGTZ");
  // It is important that the jump instructions are the first ones in case there is a label containing a substring.
  if (std::regex_match(test, load)) {
    return JUMP;
  }
  if (std::regex_match(test, load)) {
    return JZERO;
  }
  if (std::regex_match(test, load)) {
    return JGTZ;
  }
  if (std::regex_match(test, load)) {
    return LOAD;
  }
  if (std::regex_match(test, load)) {
    return STORE;
  }
  if (std::regex_match(test, load)) {
    return ADD;
  }
  if (std::regex_match(test, load)) {
    return SUB;
  }
  if (std::regex_match(test, load)) {
    return MULT;
  }
  if (std::regex_match(test, load)) {
    return DIV;
  }
  if (std::regex_match(test, load)) {
    return READ;
  }
  if (std::regex_match(test, load)) {
    return WRITE;
  }

  return HALT;
}

/**
 * @brief Get the operand for the instruction
 *
 * @param test
 * @return Operand*
 */
Operand* ProgramMemory::getOperand(std::string test) {
  std::regex indirect("\\*[0-9]+");
  std::regex inmediate("=[0-9]+");
  std::regex direct("[0-9]+");

  if (std::regex_match(test, indirect)) {
    test = test.substr(test.find('*') + 1, test.size());
    return new IndirectOperand(stoi(test));
  } else if (std::regex_match(test, inmediate)) {
    test = test.substr(test.find('=') + 1, test.size());
    return new IndirectOperand(stoi(test));
  } else if (std::regex_match(test, direct)) {
    return new IndirectOperand(stoi(test));
  } else {
    return NULL;
  }
}

/**
 * @brief Construct the corresponding instruction
 * 
 * @param test 
 * @param operato 
 * @param operand 
 * @return Instruction* 
 */
Instruction* ProgramMemory::getInstruction(std::string test, SpecificOperator operato, Operand* operand) {
  Instruction* result = NULL;
  test.erase(std::remove(test.begin(), test.end(), ' '), test.end());  //  Delete ' ' from string

  switch (operato) {
    case LOAD:
      result = new Load(operand);
      break;
    case STORE:
      result = new Store(operand);
      break;
    case ADD:
      result = new Add(operand);
      break;
    case SUB:
      result = new Sub(operand);
      break;
    case MULT:
      result = new Mult(operand);
      break;
    case DIV:
      result = new Div(operand);
      break;
    case READ: {
        TapeFile tapeFileIn(nameOfTheTapeFileIn_);
        result = new Read(tapeFileIn, operand);
      }
      break;
    case WRITE: {
        TapeFile tapeFileOut(nameOfTheTapeFileOut_);
        result = new Write(tapeFileOut, operand);
      }
      break;
    case JUMP:
      result = new Jump(labels_[test]);
      break;
    case JZERO:
      result = new Jzero(labels_[test]);
      break;
    case JGTZ:
      result = new Jgtz(labels_[test]);
      break;
    case HALT:
      result = new Halt();
      break;
  }
  return result;
}