#include <iostream>
#include "utils.h"

int main() {
    int a = 10;
    int b = 5;

    std::cout << "Calculadora\n";
    std::cout << a << "+" << b << "=" << suma(a,b) << "\n";
    std::cout << a << "-" << b << "=" << resta(a,b) << "\n";

    return 0;
}