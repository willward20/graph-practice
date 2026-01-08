#include <iostream>
#include <vector>

int main() {

    std::vector<int> values = {5, 10, 15, 3, 8, 9, 7, 2, 20};
    int length = values.size();
    int target = 9;

    for (int ii = 0; ii < length; ii++) {
        if (values[ii] == target) {
            std::cout << "Target found at " << ii << std::endl;
        }
    }

    return 0;
}