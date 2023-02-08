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
      std::string exception = "This program will simulñate a RAM machine\nThis program needs 3";
      exception += "parameters:\n\tprogram.ram: Name of the file with the ram machine.\n\tinput_tape.in\n\toutput_tape.out\n";
      throw std::runtime_error(exception);
    }
  }
  if (argc != 4) {
    std::string exception = "This program needs 3 parameters:\n\tprogram.ram: ";
    exception += "Name of the file with the ram machine.\n\tinput_tape.in\n\toutput_tape.out\nWrite: \"--help\" for more information.\n";
    throw std::runtime_error(exception);
  }
  return EXIT_SUCCESS;
}
