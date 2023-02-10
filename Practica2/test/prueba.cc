#include <regex>
#include <iostream>

int main() {
 std::regex read("READ");
if (std::regex_match("READ", read)) {
   std::cout << "a";
}


}