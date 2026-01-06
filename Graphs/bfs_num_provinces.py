from get_adj_list import get_adj_list

# Define a node graph. 
num_nodes = 9
edges = [
    [1,2],
    [2,3],
    [4,5],
    [4,6],
    [5,7],
    [8,9]
]

# Get an adjacency list.
adj_list = get_adj_list(num_nodes, edges)

# Prepare to run BFS.
explored = [0] * (num_nodes+1)
queue = []
num_provices = 0

# Define BFS algorithm
def bfs(start_node):

    # Add the start node to the queue.
    queue.append(start_node)

    # Search until the queue is empty.
    while queue != []:

        # Retrieve the next node from the queue.
        node = queue.pop(0)

        # Mark node explored.
        explored[node] = 1

        # Get node's neighbors.
        neighbors = adj_list[node]
        for neighbor in neighbors:
            
            # If not explored or in queue, add to queue.
            if neighbor not in queue and explored[neighbor] == 0:
                queue.append(neighbor)


# For each node unexplored, run BFS.
for node in range(1, num_nodes):
    if explored[node] == 0:
        num_provices += 1
        bfs(node)

# Print the number of provinces.
print(f"Number of provinces = {num_provices}")