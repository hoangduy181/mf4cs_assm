def bellman_ford(aM, start):
    """
    Bellman-Ford algorithm to find the shortest path in a weighted graph.

    :param aM: Adjacency matrix where aM[u][v] represents the weight of the edge from u to v
               (0 if there is no edge)
    :param start: The starting vertex
    :return: Tuple (dist, prev)
             dist: List of shortest distances from the start vertex to each vertex
             prev: List of predecessors for each vertex to reconstruct the shortest path
    """
    n = len(aM)
    edges = []

    # Convert adjacency matrix to edge list
    for u in range(n):
        for v in range(n):
            if aM[u][v] != 0:  # Assuming 0 means no edge
                edges.append((u, v, aM[u][v]))

    # Initialize distance to all vertices as infinite and distance to the source as 0
    dist = [float('inf')] * n
    dist[start] = 0

    # Initialize the predecessor list
    prev = [-1] * n

    # Relax edges |V| - 1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    # Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist, prev

# Function to reconstruct the path from the predecessors list
def reconstruct_path(prev, start, end):
    path = []
    current = end
    while current != -1:
        path.insert(0, current)
        current = prev[current]
    if path[0] == start:
        return path
    else:
        return []

def solve_bellman_ford(aM, start, end):
    dist, prev = bellman_ford(aM, start)
    print("Shortest distance from A to B:", dist[end])
    path = reconstruct_path(prev, start, end)
    print("Path from A to B:", path)
    return path
