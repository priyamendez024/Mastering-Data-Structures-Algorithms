
# Chapter 16 Python Code - Dijkstra's Algorithm (Shortest Path)
import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {start: 0}
    visited = set()

    while pq:
        dist, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_dist = dist + weight
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    return distances

graph = {'A': [('B', 1), ('C', 4)], 'B': [('A', 1), ('C', 2), ('D', 5)], 'C': [('A', 4), ('B', 2), ('D', 1)], 'D': [('B', 5), ('C', 1)]}
print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
