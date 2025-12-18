from get_adj_list import get_adj_list

def get_dfs_traversal(num_nodes, adj_list, start_node):

    # Initialize data structures
    dfs_traversal = []
    explored = [0 for ii in range(0, num_nodes + 1)]

    # Run DFS
    dfs(start_node, adj_list, explored, dfs_traversal)

    return dfs_traversal


def dfs(node, adj_list, explored, dfs_traversal):

    # Mark the node as explored and add to the traversal
    explored[node] = 1
    dfs_traversal.append(node)

    # Retrieve node's neighbors
    neighbors = adj_list[node]
    
    # Explore the depth of neighbor if not explored
    for neighbor in neighbors:
        if explored[neighbor] == 0:
            dfs(neighbor, adj_list, explored, dfs_traversal)


def main():

    # Define a graph
    num_nodes = 8
    edges = [
        [0,1],
        [0,2],
        [0,4],
        [1,0],
        [2,0],
        [3,4],
        [4,0],
        [4,3]
    ]

    # Get the adjacency list
    adj_list = get_adj_list(num_nodes, edges)

    # Return the DFS traversal for a starting node
    start_node = 0
    dfs_traversal = get_dfs_traversal(num_nodes, adj_list, start_node)
    print(dfs_traversal)
    

if __name__ == '__main__':
    main()