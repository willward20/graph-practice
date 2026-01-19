#include <iostream>
#include <vector>

int main() {
    
    // ------- Arrays ---------
    // Define an array and get its length. 
    std::string cars[4] = {"Prius", "CR-V", "Avalon", "Outback"};
    int length = sizeof(cars) / sizeof(cars[0]); // sizeof does not come from std

    // Loop through the array using an index. 
    for (int i = 0; i < length; i++) {
        std::cout << cars[i] << std::endl;
    }

    // Loop through the array by values. 
    for (std::string car : cars) {
        std::cout << car << std::endl;
    }

    // NOTE: you cannot add or remove elements from an array.


    
    // ------- Vectors ---------
    // Define a vector and get its length.
    std::vector<std::string> trucks = {"F1-50", "Tacoma", "Silverado", "1500"};
    length = trucks.size();

    // Loop through the array using an index.
    for (int i = 0; i < length; i++) {
        std::cout << trucks[i] << std::endl;
    }

    // Loop through the array by values. 
    for (std::string truck : trucks) {
        std::cout << truck << std::endl;
    }

    // Add / remove elements
    trucks.push_back("Maverick");
    std::cout << "New size = " << trucks.size() << std::endl;
    trucks.pop_back();
    std::cout << "Removed Maverick, so the last element is " << trucks.back() << std::endl;
    std::vector<std::string>::iterator it = trucks.begin();
    trucks.insert(it+2, "Maverick");
    for (std::string truck : trucks) {
        std::cout << truck << std::endl;
    }


    return 0;
}