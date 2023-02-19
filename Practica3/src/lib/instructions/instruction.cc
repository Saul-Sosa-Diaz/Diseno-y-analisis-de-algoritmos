#include "instruction.h"

std::ostream &operator<<(std::ostream &output, const Instruction *Instruction) {
  output << Instruction->to_s();
  return output;
}
