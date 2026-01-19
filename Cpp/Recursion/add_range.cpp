#include <iostream>

int sum(int range) {

    if (range == 0) {
        return range;
    }
    else {
        return range + sum(range-1);
    }
}

int main() {

    int n = 20;
    std::cout << "The sum of numbers between 1 and " << n << " are " << sum(n) << std::endl;
    return 0;
}