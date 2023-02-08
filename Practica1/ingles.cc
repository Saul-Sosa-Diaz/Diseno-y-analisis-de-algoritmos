#include "ingles.h"

Ing::Ing() {
  set_diccionario();
}
void Ing::set_diccionario(){
std::map<int, std::string> inicial;
  inicial['0'] = "zero";
  inicial['1'] = "one";
  inicial['2'] = "two";
  inicial['3'] = "three";
  inicial['4'] = "four";
  inicial['5'] = "five";
  inicial['6'] = "six";
  inicial['7'] = "seven";
  inicial['8'] = "eight";
  inicial['9'] = "nine";
  diccionario_ = inicial;
}