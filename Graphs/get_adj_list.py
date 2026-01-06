def get_adj_list(num_nodes, edges):

    # Initialize the adjacency list
    adj_list = [[] for ii in range(num_nodes + 1)]

    # Add each edge to the adjacency list
    for edge in edges:
        n1, n2 = edge
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    return adj_list


def main():
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
    adj_list = get_adj_list(num_nodes, edges)
    print(adj_list)

if __name__ == '__main__':
    main()