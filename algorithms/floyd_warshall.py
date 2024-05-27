def floyd_warshall(aM):
    """
    Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices.

    :param aM: Adjacency matrix where aM[u][v] represents the weight of the edge from u to v
               (float('inf') if there is no edge and 0 if u == v)
    :return: Tuple (dist, next)
             dist: A matrix where dist[i][j] is the shortest distance from vertex i to vertex j
             next: A matrix where next[i][j] is the next vertex on the shortest path from i to j
    """
    # Number of vertices
    n = len(aM)
    
    # Initialize distance and next matrices
    dist = [row[:] for row in aM]  # Make a copy of the adjacency matrix
    next = [[None if aM[i][j] == float('inf') else j for j in range(n)] for i in range(n)]

    # Run Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

    return dist, next

def reconstruct_path(next, start, end):
    """
    Reconstructs the shortest path from start to end using the next matrix.

    :param next: A matrix where next[i][j] is the next vertex on the shortest path from i to j
    :param start: The starting vertex
    :param end: The ending vertex
    :return: A list representing the shortest path from start to end
    """
    if next[start][end] is None:
        return []

    path = [start]
    while start != end:
        start = next[start][end]
        path.append(start)

    return path

def solve_floyd_warshall(aM, start, end):
    inf = float('inf')
    aM = [[inf if x == 0 else x for x in row] for row in aM]
    dist, next = floyd_warshall(aM)
    print("Shortest distance from A to B:", dist[start][end])
    path = reconstruct_path(next, start, end)
    print("Path from A to B:", path)
    return path