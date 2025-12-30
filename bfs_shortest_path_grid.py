
def bfs_shortest_path_grid(grid, start, end):
    """Find a shortest path from a start node to an end node on a grid."""

    # Initialize data structures
    path = []
    queue = [start]
    explored = grid
    parent = {}
    directions = [[-1,0], [1,0], [0,-1], [0,1]]

    n_rows = len(grid)
    n_cols = len(grid[0])

    # Search until the queue is empty or the end node is found
    while queue != []:
        
        # Retrieve the next node from the queue
        node_i, node_j = queue.pop(0)

        # Mark the node as explored
        explored[node_i][node_j] = 1

        # Investigate node's neighbors.
        for i_dir, j_dir in directions:
            
            d_row = node_i + i_dir
            d_col = node_j + j_dir

            if d_row >= 0 and d_row < n_rows and d_col >= 0 and d_col < n_cols:
                
                neighbor = (d_row, d_col)

                if explored[neighbor[0]][neighbor[1]] == 0 and neighbor not in queue:

                    # Mark the neighbor's parent.
                    parent[neighbor] = (node_i, node_j)

                    if neighbor == end:

                        # Re-trace the path from end node to start node
                        path.append(end)
                        while path[-1] != start:
                            path.append(parent[path[-1]])

                        return path[::-1]
                    
                    else:
                        queue.append(neighbor)

    return path


def main():

    # Define a graph
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # Return the BFS traversal for a starting node
    start = (8,1)
    end = (1,8)
    shortest_path = bfs_shortest_path_grid(grid, start, end)
    print(shortest_path)
    

if __name__ == '__main__':
    main()