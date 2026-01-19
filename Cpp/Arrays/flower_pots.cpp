#include <iostream>
#include <vector>


bool canPlaceFlowers(std::vector<int>& flowerbed, int n) {

    int placed = 0;
    int idx = 0;
    int zero_counter = 0;

    // Loop through the flowerbed and try to place flowers.
    for (int spot : flowerbed) {

        std::cout << spot << std::endl;

        // Check if the new spot it empty.
        if (spot == 1) {
            zero_counter = 0;
        }
        else {
            zero_counter++;
        }

        // Check for 3 0s in a row.
        if (zero_counter == 3) {
            // Place a flower.
            flowerbed[idx - 1] = 1;
            placed++;

            // Check if all flowers were placed.
            if (placed == n) {
                return true;
            }

            // Set number of zeros to 1.
            zero_counter = 1;
        }

        // Update the index.
        idx++;
    }

    return false;
}


int main() {
    int n = 2;
    std::vector<int> flowerbed = {1, 0, 0, 0, 0, 0, 0, 0};
    bool result = canPlaceFlowers(flowerbed, n);
    std::cout << "Can we place the flowers? " << result << std::endl;
}