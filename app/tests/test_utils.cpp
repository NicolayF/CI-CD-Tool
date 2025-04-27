#include <cassert>
#include "../src/utils.h"

int main() {
    assert(suma(2,3)==5);
    assert(suma(-2,0)==-2);

    assert(resta(5,3)==2);
    assert(resta(3,5)==-2);

    return 0;
}