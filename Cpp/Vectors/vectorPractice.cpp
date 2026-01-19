#include <iostream>
#include <vector>
#include <chrono>

/*
Any event ID < 0 is invalid and must be removed.

If the same event ID appears multiple times consecutively, keep only one.

After compaction, if events.size() > maxSize, remove the oldest events (elements at the beginning) until events.size() == maxSize.

After all operations, ensure the vector releases unused capacity if it has shrunk significantly.
*/

void compactEvents(std::vector<int>& events, std::size_t maxSize) {

    // If input vector is empty, return early.
    if (events.size() == 0) {return;}

    // Compact the vector.
    int previous;
    bool previous_available = false;
    for (int i = 0; i < events.size();) {

        int current = events[i];

        // Check for duplicates.
        bool duplicates = false;
        if (previous_available) {
            duplicates = (current == previous);
        }

        // Check for invalid IDs.
        if (current < 0 || duplicates) {
            events.erase(events.begin() + i);
        }
        else {
            i++;
            previous = current; 

            // On first iteration, set flag to true.
            if (i == 0) {
                previous_available = true;
            }
        }
    }

    // Remove oldest values until size equals max size.
    if (maxSize < events.size()) {
        int num_to_remove = events.size() - maxSize;
        events.erase(events.begin(), events.begin() + num_to_remove);
    }

    // Reduce vector capacity.
    events.shrink_to_fit();

}

void compactEvents2(std::vector<int>& events, std::size_t maxSize) {

    // If input vector is empty, return early.
    if (events.size() == 0) {return;}

    if (maxSize == 0) {
        events.clear();
        return;
    }

    std::vector<int> processed;
    processed.reserve(events.size());

    // Compact the vector.
    int previous;
    bool previous_available = false;
    for (int i = 0; i < events.size(); i++) {

        int current = events[i];

        // Check for duplicates.
        bool duplicates = false;
        if (previous_available) {
            duplicates = (current == previous);
        }

        // Check for invalid IDs.
        if (current < 0 || duplicates) {continue;}
        else {
            processed.push_back(current);
            previous = current; 

            // On first iteration, set flag to true.
            previous_available = true;
        }
    }

    // Remove oldest values until size equals max size.
    if (maxSize < processed.size()) {
        std::vector<int> tail(
            processed.end() - maxSize,
            processed.end()
        );
        processed = std::move(tail);
    }

    // Reduce vector capacity.
    processed.shrink_to_fit();

    // Move new vector to old vector.
    events = std::move(processed);
}



int main() {

    // Create a vector of events.
    std::vector<int> events = {1, 1, -2, 3, 3, 3, 4, -1, 5};

    // Process the vector and evaluate the execution time.
    auto t1 = std::chrono::high_resolution_clock::now();
    compactEvents2(events, 3);
    auto t2 = std::chrono::high_resolution_clock::now();

    // Print the final vector.
    std::cout << "Processed vector is " << std::endl;
    for (int element : events) {
        std::cout << element << ", ";
    }
    std::cout << std::endl;
    std::cout << "Final vector capacity is " << events.capacity() << std::endl;

    // Getting number of milliseconds as a double. 
    std::chrono::duration<double, std::milli> ms_double = t2 - t1;
    std::cout << ms_double.count() << "ms\n";


    return 0;
}