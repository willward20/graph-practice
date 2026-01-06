from get_adj_list import get_adj_list


def bfs_detect_cycle(adj_list, num_nodes, start):
    
    # Prepare the BFS algorithm.
    queue = []
    explored = [0] * (num_nodes + 1)
    parents = [0] * (num_nodes + 1)

    # Add the start node to the queue.
    queue.append(start)

    # Run the BFS algorithm
    while queue != []:

        # Get node from queue and mark explored.
        node = queue.pop(0)
        explored[node] = 1

        # Explore the node's neighbors.
        for neighbor in adj_list[node]:

            # If neighbor is node's parent, skip.
            if parents[node] == neighbor:
                continue

            # Mark neighbor's parent.
            parents[neighbor] = node

            # If neighbor is explored, return True
            if explored[neighbor] == 1:
                return True

            # Add neighbor to the queue
            if neighbor not in queue:
                queue.append(neighbor)

    return False


def main():

    # Get an adjacency list
    num_nodes = 7
    edges = [
        [1, 2],
        [1, 3],
        [2, 5],
        [3, 4],
        [3, 6],
        [5, 7],
        [6, 7]
    ]
    adj_list = get_adj_list(num_nodes, edges)

    # Check whether the graph is cyclic.
    is_cyclic = bfs_detect_cycle(adj_list, num_nodes, 1)
    print("Cyclic? ", is_cyclic)


if __name__ == '__main__':
    main()