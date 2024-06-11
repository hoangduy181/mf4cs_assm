import heapq

def dijkstra(aM, start, end):
    n = len(aM)
    dist = [float('inf')] * n
    dist[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    previous = [-1] * n

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)

        if u in visited:
            continue

        visited.add(u)

        if u == end:
            break

        for v in range(n):
            if aM[u][v] != 0 and v not in visited:
                alt = current_dist + aM[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u
                    heapq.heappush(priority_queue, (alt, v))

    path = []
    if dist[end] != float('inf'):
        while end != -1:
            path.insert(0, end)
            end = previous[end]

    return dist, path


def solve_dijsktra(aM, start, end):
    dist, path = dijkstra(aM, start, end)
    print("Shortest distance from A to B:", dist[end])
    print("Path from A to B:", path)
    return path
