INF = 99999  # Define a large enough value for infinity
V = 4  # Number of vertices in the graph


def floyd_warshall_recursive(graph, i, j, k):
    """
    Update the shortest path between vertices i and j through vertex k using recursion.

    Parameters:
        graph: 2D list of integers
            The adjacency matrix representing the graph.
        i, j, k: integers
            The vertices in question.
    
    Returns:
        int
            The updated shortest path from i to j through k.
    """
    if i == j:
        return 0

    if k < 0:
        return graph[i][j]

    without_k = floyd_warshall_recursive(graph, i, j, k - 1)
    through_k = floyd_warshall_recursive(graph, i, k, k - 1) + floyd_warshall_recursive(graph, k, j, k - 1)

    graph[i][j] = min(without_k, through_k)
    
    return graph[i][j]


def main():
    """
    Main function to execute the Floyd-Warshall algorithm.
    """
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    for i in range(V):
        for j in range(V):
            floyd_warshall_recursive(graph, i, j, V - 1)

    for i in range(V):
        for j in range(V):
            if graph[i][j] == INF:
                graph[i][j] = "INF"

    print("The updated adjacency matrix is:")
    print(graph)


if __name__ == "__main__":
    main()