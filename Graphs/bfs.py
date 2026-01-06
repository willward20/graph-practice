from get_adj_list import get_adj_list

def bfs(num_nodes, adj_list, start_node):

    # Initialize data structures
    bfs_traversal = []
    queue = [start_node]
    explored = [0 for ii in range(0, num_nodes + 1)]

    # Search until the queue is empty
    while queue != []:
        
        # Retrieve the next node from the queue.
        node = queue.pop(0)

        # Mark the node as explored and add to the traversal
        explored[node] = 1
        bfs_traversal.append(node)

        # Retrieve node's neighbors
        neighbors = adj_list[node]

        # Add neighbor to queue if not explored and not in queue
        for neighbor in neighbors:
            if explored[neighbor] == 0 and neighbor not in queue:
                queue.append(neighbor)

    return bfs_traversal


def main():

    # Define a graph
    num_nodes = 7
    edges = [
        [1,2],
        [1,3],
        [2,4],
        [2,5],
        [3,6],
        [5,7],
        [6,7]
    ]

    # Get the adjacency list
    adj_list = get_adj_list(num_nodes, edges)

    # Return the BFS traversal for a starting node
    start_node = 2
    bfs_traversal = bfs(num_nodes, adj_list, start_node)
    print(bfs_traversal)
    

if __name__ == '__main__':
    main()