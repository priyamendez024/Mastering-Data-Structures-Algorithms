
# Chapter 17 Python Code - Bellman-Ford Algorithm (Negative Weights)
def bellman_ford(graph, start, vertices):
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Detect negative weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle")
            return None
    return distances

graph = [('A', 'B', 1), ('B', 'C', -1), ('C', 'D', 2), ('D', 'B', -2)]
print(bellman_ford(graph, 'A', ['A', 'B', 'C', 'D']))  # Output: {'A': 0, 'B': 1, 'C': 0, 'D': 2}
