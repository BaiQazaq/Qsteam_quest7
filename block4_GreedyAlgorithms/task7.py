# 7. Write a program for the single-source shortest path problem (Dijkstra's algorithm).

# In this implementation, the dijkstra function takes an adjacency list representation of the graph and the source vertex as input. 
# It uses a priority queue to efficiently explore vertices in the order of increasing distance from the source. 
# The algorithm continues until all reachable vertices are processed, and the final distances are returned as a dictionary.

# Note that this implementation assumes non-negative edge weights. If the graph contains negative weights, 
# you might want to consider Bellman-Ford algorithm instead.

import heapq

def dijkstra(graph, start_vertex):
    """
    Find the single-source shortest paths using Dijkstra's algorithm.

    Parameters:
    - graph: An adjacency list representation of the graph. Each element is a tuple (neighbor, weight).
    - start_vertex: The source vertex.

    Returns:
    - A dictionary of the shortest distances from the start vertex to each vertex.
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start_vertex] = 0

    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If we have already found a shorter path to the current vertex, skip
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph_dijkstra = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_vertex_dijkstra = 'A'

result_dijkstra = dijkstra(graph_dijkstra, start_vertex_dijkstra)
print(f"Shortest distances from vertex {start_vertex_dijkstra}:", result_dijkstra)
