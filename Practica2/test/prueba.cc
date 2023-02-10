#include <iostream>
#include <regex>
#include <map>

int main(){
  
  std::map<std::string, int> label_;
std::cout << label_["aaa"]; 
std::cout << label_["bbbb"]; 




}

((?!((ADD)|(SUB)|(DIV)|(MULT)|(HALT)|(JUMP)|(JGTZ)|(WRITE)|(READ)|(STORE)|(LOAD)))[A-Z][A-Z0-9]*[[:blank:]]*:)?[[:blank:]]*(((ADD|SUB|DIV|MULT)\\s*((=[0-9]+)|([0-9]+)|(\\*[0-9]+)))|(HALT)|((JUMP|JGTZ|JZERO)[[:blank:]]*[A-Z][A-Z0-9]*)|((WRITE|READ)\\s*(([0-9]+)|(\\*[0-9]+)))|(STORE\\s*(([0-9]+)|(\\*[0-9]+)))|(LOAD\\s*((=[0-9]+)|([0-9]+)|(\\*[0-9]+))))
  regex += "[[:blank:]]*\\n";