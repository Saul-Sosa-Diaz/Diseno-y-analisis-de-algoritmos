/**
 * @file inmediate.h
 * @author Saul Sosa Diaz
 * @brief declaration of inmediate operand
 * @version 0.1
 * @date 2023-02-04
 *
 * @copyright Copyright (c) 2023
 *
 */
#pragma once

#include "../operand.h"

class InmediateOperand : public Operand<double> {
 public:
  InmediateOperand(double index) : Operand(index){};
  double getValue(const DataMemory&);

 private:
};