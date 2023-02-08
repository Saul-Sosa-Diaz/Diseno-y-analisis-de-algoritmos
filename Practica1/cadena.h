#pragma once

#include "ingles.h"
#include "esp.h"
#include <string> 
#include <iostream>

class Cadena{
 public:
  Cadena(bool param) {
    
    Idioma* ing = new Ing();

    // Providing a seed value
    srand((unsigned) time(NULL));
    int random = 1 + (rand() % 500);
    cadena_ = std::to_string(random);
     if (param) {
        idioma_ = new Esp();
      } else {
        idioma_  = new Ing();
      }
  }

  void set_strategy(bool param) {

    if (param) {
        idioma_  = new Esp();
      } else {
        idioma_  = new Ing();
      }
  }

  void traducir() {
    std::cout << cadena_ << std::endl;
    idioma_->traducir(cadena_);
  }


 private:
  Idioma* idioma_;
  std::string cadena_;
  
};

