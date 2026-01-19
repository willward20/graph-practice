#include <iostream>

/*
Fibonacci =  0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

F(n) = F(n-1) + F(n-2)

*/

int F(int n) {

    if (n > 1) {
        return F(n-1) + F(n-2);
    }
    else {
        return n;
    }

    return 0;
}

int main() {

    int n = 7;

    int result = F(n-1);

    std::cout << n << "-th Fibonacci number is " << result << std::endl;

    return 0;
}