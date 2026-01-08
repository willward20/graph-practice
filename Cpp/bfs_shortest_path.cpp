#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<vector<int>> bfs(
    const vector<vector<int>> &grid,
    const vector<int> &start,
    const vector<int> &end
) {
    
    int num_rows = grid.size();
    int num_cols = grid[0].size();

    // Initialize the shortest path.
    vector<vector<int>> path;

    // Define the directions to travel.
    vector<vector<int>> directions = {
        {0, -1}, {0, 1}, {1, 0}, {-1, 0}
    };

    // Create a vector of explored nodes.
    vector<vector<int>> explored(
        num_rows, vector<int>(num_cols, 0)
    );

    // Create a vector of parent nodes.
    vector<vector<vector<int>>> parent(
        num_rows, vector<vector<int>>(num_cols, vector<int>(2))
    );

    // Create a queue of nodes to explore.
    queue<vector<int>> to_explore;

    // Add the start node to the queue and mark explored.
    to_explore.push(start);
    explored[start[0]][start[1]] = 1;

    // Search until the queue is empty. 
    while (!to_explore.empty()) {
        
        // Retrieve the next node from the queue and remove it.
        vector<int> node = to_explore.front();
        to_explore.pop();

        // Investigate node's neighbors. 
        for (vector<int> dir : directions) {

            vector<int> neighbor = {
                node[0] + dir[0],
                node[1] + dir[1]
            };

            // Return if end node is found.
            if (neighbor == end) {
                
                // Add the end node to the path.
                path.push_back(neighbor);

                // Add each node's parent to the path until reaching the start.
                while (node != start) {
                    path.push_back(node);
                    node = parent[node[0]][node[1]];
                }

                // Add the start node.
                path.push_back(node);

                // Reverse the path.
                reverse(path.begin(), path.end());

                return path;
            }


            if (
                // Check if the neighbor is in bounds.
                neighbor[0] >= 0 &&
                neighbor[1] >= 0 &&
                neighbor[0] < num_rows &&
                neighbor[1] < num_cols &&
                // Check if the neighbor is traversable.
                !grid[neighbor[0]][neighbor[1]] &&
                // Check if the neighbor is explored.
                !explored[neighbor[0]][neighbor[1]]
            ) {
                // Add the neighbor to the queue. 
                to_explore.push(neighbor);

                // Mark node as explored.
                explored[neighbor[0]][neighbor[1]] = 1;

                // Mark the neighbor's parent.
                parent[neighbor[0]][neighbor[1]] = node;
            }
        }
    }

    return path;
}


int main() {
    
    // Create a grid (0 traversable, 1 not).
    const vector<vector<int>> grid = {
        {0, 0, 1, 1, 0},
        {1, 0, 0, 1, 1},
        {0, 0, 0, 0, 1},
        {1, 1, 1, 0, 0},
        {0, 0, 0, 0, 1}
    };

    // Choose the start and end nodes.
    const vector<int> start = {0, 0};
    const vector<int> end = {4, 0};

    // Run BFS to find the shortest path.
    vector<vector<int>> path = bfs(grid, start, end);

    for (vector<int> node : path) {
        cout << "(" << node[0] << ", " << node[1] << ")" << endl;
    }

    return 0;
}