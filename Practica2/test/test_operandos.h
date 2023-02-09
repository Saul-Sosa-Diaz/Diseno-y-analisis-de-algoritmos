#include "var_tests.h"

#include "../src/lib/memories/dataMemory/dataMemory.h"
#include "../src/lib/operands/inmediate/inmediate.h"
#include "../src/lib/operands/direct/direct.h"
#include "../src/lib/operands/indirect/indirect.h"

void operandos(){
  TEST_DONE++;
  try {
    DataMemory datamemo(32);
    datamemo.load();
    Operand* operando = new InmediateOperand(10);
    ASSERT_EQ(operando->getValue(datamemo), 10);
    datamemo.writeValue(10, 15);
    Operand* operando2 = new DirectOperand(10);
    ASSERT_EQ(operando2->getValue(datamemo), 15);
    datamemo.writeValue(15,7);
    Operand* operando1 = new IndirectOperand(10);
    ASSERT_EQ(operando1->getValue(datamemo), 7);

  } catch (const std::exception& e) {
    std::cout << e.what() << "en Operandos()";
    TEST_FAILED++;
    return;
  }
  TEST_PASSED++;
}

void test_operandos() {
  operandos();
}