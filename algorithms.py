import heapq
from graph_data import graph

# Get all nodes (for dropdown)
def get_all_cities():
    cities = set(graph.keys())
    for edges in graph.values():
        for dest, _, _ in edges:
            cities.add(dest)
    return sorted(cities)

# Traffic based time calculation
def travel_time(distance, traffic):
    if traffic == "Green":
        speed = 40
        delay = 0
    else:
        speed = 20
        delay = 3
    return (distance / speed) * 60 + delay

# Dijkstra (SSSP based on time)
def dijkstra(source="Majestic"):
    cities = get_all_cities()
    time = {c: float('inf') for c in cities}
    dist = {c: 0 for c in cities}
    parent = {c: None for c in cities}

    time[source] = 0
    pq = [(0, source)]

    while pq:
        curr_time, u = heapq.heappop(pq)

        for v, d, traffic in graph.get(u, []):
            t = travel_time(d, traffic)
            new_time = curr_time + t

            if new_time < time[v]:
                time[v] = new_time
                dist[v] = dist[u] + d
                parent[v] = u
                heapq.heappush(pq, (new_time, v))

    return time, dist, parent

# Reconstruct path from Dijkstra
def get_path(parent, dest):
    path = []
    while dest:
        path.append(dest)
        dest = parent[dest]
    return path[::-1]

# DFS to find all possible routes
def find_all_paths(start, end, path=None, all_paths=None):
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []

    path = path + [start]

    if start == end:
        all_paths.append(path)
        return all_paths

    for (next_node, _, _) in graph.get(start, []):
        if next_node not in path:
            find_all_paths(next_node, end, path, all_paths)

    return all_paths

# Compute metrics for each route
def path_metrics(route):
    total_distance = 0
    total_time = 0

    for i in range(len(route)-1):
        u, v = route[i], route[i+1]
        for dest, d, traffic in graph[u]:
            if dest == v:
                total_distance += d
                total_time += travel_time(d, traffic)
                break

    return total_distance, total_time
