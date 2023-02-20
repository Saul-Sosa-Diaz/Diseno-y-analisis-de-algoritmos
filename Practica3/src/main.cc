/**
 * @file main.cc
 * @author Saul Sosa Diaz
 * @brief main simulator RAM machine
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 * @link https://terminalroot.com/easily-create-tables-in-terminal-with-cpp/
 * 
 */

#include "lib/functions/utils.h"
#include "lib/controlUnit/controlUnit.h"

int main(int argc, char* argv[]) {
  try {
    Usage(argc, argv);
    ProgramMemory programMemory(argv[1], argv[2], argv[3]);
    DataMemory dataMemory(32);
    ControlUnit ramMachine(&programMemory, &dataMemory, std::stoi(argv[4]));
    ramMachine.run();

  } catch (const std::exception& e) {
    std::cerr << e.what();
  }
  return 0;
}