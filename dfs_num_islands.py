


def dfs_num_islands(grid):

    # Prepare to run DFS
    num_islands = 0
    num_rows = len(grid)
    num_cols = len(grid[0])
    explored = [[0] * num_cols for _ in range(num_rows)]
    directions = [
            (-1, -1),
            (-1,  0),
            (-1,  1),
            ( 0, -1),
            ( 0,  1),
            ( 1, -1),
            ( 1,  0),
            ( 1,  1)
        ]

    def dfs(row, col):
        # Mark node as explored.
        explored[row][col] = 1

        # For each neighbor, run DFS.        
        for dir in directions:
            new_row = row + dir[0]
            new_col = col + dir[1]

            if new_row >= 0 and new_row < num_rows and new_col >= 0 and new_col < num_cols:
                if grid[new_row][new_col] == 1 and explored[new_row][new_col] == 0:
                    dfs(new_row, new_col)


    # Traverse through the grid
    for row in range(num_rows):
        for col in range(num_cols):

            # If node is land, traverse the island.
            if grid[row][col] == 1 and explored[row][col] == 0:

                # Increment the number of islands
                num_islands += 1

                # Run DFS on the new start node.
                dfs(row, col)


    return num_islands


def main():

    # Define a graph
    grid = [
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1],
    ]

    num_islands = dfs_num_islands(grid)
    print(f"Number of Islands: ", num_islands)
    

if __name__ == '__main__':
    main()