#include "idioma.h"

void Idioma::traducir( std::string string_to_convert) {
  std::string result = "";
  for (int j = 0; j < string_to_convert.size(); j++) {
    result += diccionario_[string_to_convert[j]] + " ";
  }
  std::cout << result;
}
