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
    std::string exception = "\033[1;31mThe file with the program RAM doesn´t match with: namein.in or nameout.out\033[0m\n";
    throw std::runtime_error(exception);
  }
  in_ = std::regex_match(name, legalTapeFileIn) ? true : false;  // Comprobar si es de entrada o salida
  readHead_ = in_ ? 0 : -1;
  finished_ = false;
  if(in_) {
    read();
  } 
};

int TapeFile::read() {
  
  if (in_) {  // Solo leer si el fichero es de entrada
    std::fstream filein;
    filein.open(name_, std::ios_base::in);
    if (filein.is_open()) {
      int aux;
      while (filein >> aux) {
        buffer_.push_back(aux);
      }
    } else {
      std::string info_error;
      info_error = "\033[1;31m" + name_ + " cannot be opened\033[0m";
      throw std::system_error(errno, std::system_category(), info_error);
    }
    filein.close();
  } else {
    std::string exception = "\033[1;31mAttempting to read in a write file\033[0m\n";
    throw std::runtime_error(exception);
  }

  return 0;
}

/**
 * @brief Writes to the output file the buffer and then clears it.
 * 
 * @return int 
 */
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
      info_error = "\033[1;31m" + name_ + " cannot be opened";
      throw std::system_error(errno, std::system_category(), info_error);
    }
    buffer_.clear();  // limpiar el buffer después de escribir
    fileOut.close();
  } else {
    std::string exception = "\033[1;31mAttempting to write in a read file\033[0m\n";
    throw std::runtime_error(exception);
  }
  return 0;
}

/**
 * @brief Adds an element to the buffer
 * 
 * @param newItem 
 */
void TapeFile::addNewItemToBuffer(int newItem) {
  buffer_.push_back(newItem);
}

/**
 * @brief Returns the element pointed to by the tape head
 * 
 * @return int 
 */
int TapeFile::getItem() {
  if (finished_) {  // Attempting to read from the input tape when there are no more items.
    std::string exception = "\033[1;31mAttempting to read from the input tape when there are no more items.\033[0m\n";
    throw std::runtime_error(exception);
  }
  int result = buffer_[readHead_];
  readHead_++;
  if(readHead_ == buffer_.size() - 1) { // The elements on the input conveyor have been completed.
    finished_ = true;
  }
  return result;
}


/**
 * @brief Returns a string with the input and output file information, cyan shows the read and write head.
 * 
 * @return std::string 
 */
std::string TapeFile::to_s() {
  std::string result = "[";
  if (in_) {
    for (int i = 0; i < buffer_.size(); i++) {
      if (i == readHead_) {
        result += "\033[1;36m" + std::to_string(buffer_[i]) + "\033[0m ";
      } else if( i == buffer_.size() - 1 && finished_ ) {  // The tape is finished and cannot advance any further.
        result += "\033[1;36m" + std::to_string(buffer_[i]) + "\033[0m ";
      } else {
        result += std::to_string(buffer_[i]) + " ";
      }
    }
  }
  
  result += "\b]";
  return result;
}