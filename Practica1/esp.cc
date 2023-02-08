#include "esp.h"

Esp::Esp() {
  set_diccionario();
}


void Esp::set_diccionario(){
std::map<int, std::string> inicial;
  inicial['0'] = "cero";
  inicial['1'] = "uno";
  inicial['2'] = "dos";
  inicial['3'] = "tres";
  inicial['4'] = "cuatro";
  inicial['5'] = "cinco";
  inicial['6'] = "seis";
  inicial['7'] = "siete";
  inicial['8'] = "ocho";
  inicial['9'] = "nueve";
  diccionario_ = inicial;
}