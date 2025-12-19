from get_adj_list import get_adj_list

def bfs_shortest_path(num_nodes, adj_list, start_node, end_node):
    """Find a shortest path from a start node to an end node."""

    # Initialize data structures
    path = []
    queue = [start_node]
    explored = [0] * (num_nodes + 1)
    parent = [0] * (num_nodes + 1)

    # Search until the queue is empty or the end node is found
    while queue != []:
        
        # Retrieve the next node from the queue
        node = queue.pop(0)

        # Mark the node as explored
        explored[node] = 1

        # Investigate node's neighbors.
        for neighbor in adj_list[node]:
                
            if explored[neighbor] == 0 and neighbor not in queue:

                # Mark the neighbor's parent.
                parent[neighbor] = node

                if neighbor == end_node:

                    # Re-trace the path from end node to start node
                    path.append(end_node)
                    while path[-1] != start_node:
                        path.append(parent[path[-1]])

                    return path[::-1]
                
                else:
                    queue.append(neighbor)

    return path


def main():

    # Define a graph
    num_nodes = 9
    edges = [
        [1,2],
        [2,3],
        [1,4],
        [2,6],
        [4,5],
        [5,6],
        [4,7],
        [5,7],
        [6,9],
        [8,9]
    ]

    # Get the adjacency list
    adj_list = get_adj_list(num_nodes, edges)

    # Return the BFS traversal for a starting node
    start_node = 6
    end_node = 7
    shortest_path = bfs_shortest_path(num_nodes, adj_list, start_node, end_node)
    print(shortest_path)
    

if __name__ == '__main__':
    main()