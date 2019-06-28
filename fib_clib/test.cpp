#include <cstdint>
#include <iostream>
#include "imp.cpp"

int main() {
    int64_t n = 92;
    std::cout << iterative(n) << std::endl;
    int64_t answer = iterative_asm(n);
    std::cout << answer << std::endl;
}
