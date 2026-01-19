#include <iostream>

int factorial(int n) {
    if (n == 1) {
        return n;
    }
    else {
        return n * factorial(n-1);
    }
}

int main() {

    int n = 4; 
    std::cout << n << " factorial = " << factorial(n) << std::endl;
    return 0;
}