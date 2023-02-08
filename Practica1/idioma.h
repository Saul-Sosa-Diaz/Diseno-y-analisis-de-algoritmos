#pragma once
#include <iostream>
#include <map>
#include <string>



class Idioma{
 public:
  void traducir( std::string);
  virtual void set_diccionario() = 0;
 protected:
  std::map<int,std::string> diccionario_;

  
};
