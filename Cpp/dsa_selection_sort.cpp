#include <iostream>
#include <array>

int main() {
    
    // Define an array with values to sort.
    std::array<int, 10> values = {5, 10, 2, 7, 15, 18, 3, 8, 9, 12};
    int length = std::size(values);

    // Perform a selection sort.
    for (int ii = 0; ii < length - 1; ii++) {

        // Initialize the starting index.
        int idx = ii;
        
        // Find the lowest value from ii to the end. 
        for (int jj = ii + 1; jj < length; jj++) {
            if (values[jj] < values[idx]) {
                idx = jj;
            }
        }

        // Move the lowest value up to the ii-th position. 
        std::swap(values[idx], values[ii]);
    }

    // Print the sorted array.
    for (int item : values) {
        std::cout << item << ", ";
    }

    return 0;
}