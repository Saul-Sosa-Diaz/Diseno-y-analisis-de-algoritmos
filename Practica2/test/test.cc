#include "test_dataMemory.h"
#include "test_fileProgram.h"
#include "test_operandos.h"


int main(int argc, char** argv) {

  std::cout << "Memoria: " << std::endl;
  test_data_memory();
  std::cout << "Ficheros: " << std::endl;
  test_file_program();
  std::cout << "Operandos: " << std::endl;
  test_operandos();

  std::cout << "Totales: " << TEST_DONE << std::endl
            << "\033[1;32m"
            << "Pasados: " << TEST_PASSED << std::endl
            << "\033[1;31m"
            << "Fallados: " << TEST_FAILED << std::endl;
  return 0;
}