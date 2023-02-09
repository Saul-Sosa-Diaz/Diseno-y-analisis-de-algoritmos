#include <iostream>
#include <regex>

int main(){
  std::string regex;
  regex = "^\\s*([A-Z][A-Z0-9]*[[:blank:]]*:)?[[:blank:]]*";  // Labels must be at the beginning of the line and not start with a number.
  regex += "(";           // JUMP
  regex += "((WRITE|READ)\\s*(([0-9]+)|(\\*[0-9]+)))|";                  // InputOutput            // Load
  regex += ")";
  regex += "[[:blank:]]*\\n";

  std::regex grammar(regex);

  (std::regex_match("LEE:READ 1\n", grammar)) ? std::cout << "Cachi" : std::cout << "NO";


}