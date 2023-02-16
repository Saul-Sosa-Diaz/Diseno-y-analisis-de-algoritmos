/**
 * @file utils.cc
 * @author Saúl Sosa Díaz
 * @brief Implementation of util functions of the program, Usage, ReadFile, WriteFile and Menu
 * @version 0.1
 * @date 2022-10-12
 *
 * @copyright Copyright (c) 2023
 * @link https://stackoverflow.com/questions/2512931/catch-multiple-custom-exceptions-c
 * 
 */

#include "utils.h"

int Usage(int argc, char* argv[]) {
  const std::string kHelp = "--help";
  if (argc > 1) {
    std::string help = argv[1];
    if (help == kHelp) {
      std::string exception = "This program will simulñate a RAM machine\nThis program needs 3 ";
      exception += "parameters:\n\t-program.ram: Name of the file with the ram machine.\n\t-input_tape.in\n\t-output_tape.out\n\t-debugmode:";
      exception += "\n\t\tIf debug is 0, debug mode is disabled and the simulator will run normal way.";
      exception += "\n\t\tIf debug is 1, the number of instructions executed by the machine at the end of execution shall be displayed on the screen.";
      exception += "\n\t\tIf debug is 2, in addition to displaying the number of instructions executed by the machine at the end of execution.";
      throw std::runtime_error(exception);
    }
  }
  if (argc != 5) {
    std::string exception = "This program needs 4 parameters:\n\tprogram.ram: ";
    exception += "Name of the file with the ram machine.\n\tinput_tape.in\n\toutput_tape.out\n\tdebugmode\nWrite: \"--help\" for more information.\n";
    throw std::runtime_error(exception);
  }
  if ((std::string(argv[4]) != "0" && std::string(argv[4]) != "1" && std::string(argv[4]) != "2")) {
    std::string exception = "Debug mode only can be 0, 1 or 2\n";
    throw std::runtime_error(exception);
  }
  return EXIT_SUCCESS;
}
