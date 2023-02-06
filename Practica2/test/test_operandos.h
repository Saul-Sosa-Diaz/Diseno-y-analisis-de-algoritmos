#include "var_tests.h"

#include "../src/entity/memory/dataMemory/dataMemory.h"
#include "../src/entity/operand/inmediate/inmediate.h"
#include "../src/entity/operand/direct/direct.h"
#include "../src/entity/operand/indirect/indirect.h"

void operandos(){
  TEST_DONE++;
  try {
    DataMemory datamemo(32);
    datamemo.load();
    Operand<double>* operando = new InmediateOperand(10.0);
    ASSERT_EQ(operando->getValue(datamemo), 10.0);
    datamemo.writeValue(10, 15.0);
    Operand<int>* operando2 = new DirectOperand(10);
    ASSERT_EQ(operando2->getValue(datamemo), 15.0);
    datamemo.writeValue(15,7);
    Operand<int>* operando1 = new IndirectOperand(10);
    ASSERT_EQ(operando1->getValue(datamemo), 7.0);

  } catch (const std::exception& e) {
    std::cout << "Error\n";
    TEST_FAILED++;
    return;
  }
  TEST_PASSED++;
}

void test_operandos() {
  operandos();
}