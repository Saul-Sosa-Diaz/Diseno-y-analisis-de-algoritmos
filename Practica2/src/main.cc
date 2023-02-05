/**
 * @file main.cc
 * @author Saul Sosa Diaz
 * @brief main simulator RAM machine
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 * 
 */

#include "utils.h"
#include "entity/memory/dataMemory.h"

int main(int argc, char* argv[]) {
  try {
    Usage(argc, argv);  
  } catch (const std::exception& e) {
    std::cerr << e.what();
  }
  


  return 0;
}