#include <cstdint>
#include <iostream>
#include "imp.cpp"

int main() {
    int64_t n = 1;
    std::cout << "it(1): " << iterative(n) << std::endl;
    ++n;
    std::cout << "it(2): " << iterative(n) << std::endl;
    ++n;
    std::cout << "it(3): " << iterative(n) << std::endl;
    ++n;
    std::cout << "it(4): " << iterative(n) << std::endl;
    ++n;
    std::cout << "it(5): " << iterative(n) << std::endl;
    //int64_t answer = iterative_asm(n);
    //std::cout << answer << std::endl;
    n = 1;
    std::cout << "it_asm(1): " << iterative_asm(n) << std::endl;
    ++n;
    std::cout << "it_asm(2): " << iterative_asm(n) << std::endl;
    ++n;
    std::cout << "it_asm(3): " << iterative_asm(n) << std::endl;
    ++n;
    std::cout << "it_asm(4): " << iterative_asm(n) << std::endl;
    ++n;
    std::cout << "it_asm(5): " << iterative_asm(n) << std::endl;
}
