# 6. Implement a greedy algorithm for the minimum spanning tree (Prim's or Kruskal's algorithm)

# These implementations assume that the graph is represented as either an adjacency list (for Prim's) or 
# a list of edges (for Kruskal's). The weights of the edges should be non-negative. 
# The examples provided are for demonstration purposes, and you can adapt them to suit your specific graph representation.

# Prim's Algorithm:

import heapq

def prim(graph):
    """
    Find the minimum spanning tree using Prim's algorithm.

    Parameters:
    - graph: An adjacency list representation of the graph. Each element is a tuple (neighbor, weight).

    Returns:
    - A list of edges in the minimum spanning tree.
    """
    min_spanning_tree = []
    visited = set()

    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)

    priority_queue = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]
    heapq.heapify(priority_queue)

    while priority_queue:
        weight, current_vertex, next_vertex = heapq.heappop(priority_queue)

        if next_vertex not in visited:
            visited.add(next_vertex)
            min_spanning_tree.append((current_vertex, next_vertex, weight))

            for neighbor, weight in graph[next_vertex]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, next_vertex, neighbor))

    return min_spanning_tree

# Example usage:
graph_prim = {
    'A': [('B', 2), ('D', 1)],
    'B': [('A', 2), ('D', 3), ('E', 10)],
    'C': [('E', 5)],
    'D': [('A', 1), ('B', 3), ('E', 7)],
    'E': [('C', 5), ('D', 7), ('B', 10)]
}

result_prim = prim(graph_prim)
print("Minimum Spanning Tree (Prim's Algorithm):", result_prim)


# Kruskal's Algorithm:

def kruskal(graph):
    """
    Find the minimum spanning tree using Kruskal's algorithm.

    Parameters:
    - graph: A list of edges, where each edge is represented as a tuple (vertex1, vertex2, weight).

    Returns:
    - A list of edges in the minimum spanning tree.
    """
    def find(parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return find(parent, parent[vertex])

    def union(parent, rank, vertex1, vertex2):
        root1 = find(parent, vertex1)
        root2 = find(parent, vertex2)

        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            rank[root2] += 1

    min_spanning_tree = []
    graph.sort(key=lambda edge: edge[2])  # Sort edges by weight

    parent = {vertex: vertex for edge in graph for vertex in edge[:2]}
    rank = {vertex: 0 for edge in graph for vertex in edge[:2]}

    for edge in graph:
        vertex1, vertex2, weight = edge
        if find(parent, vertex1) != find(parent, vertex2):
            min_spanning_tree.append(edge)
            union(parent, rank, vertex1, vertex2)

    return min_spanning_tree

# Example usage:
graph_kruskal = [('A', 'B', 2), ('A', 'D', 1), ('B', 'D', 3), ('B', 'E', 10), ('C', 'E', 5), ('D', 'E', 7)]

result_kruskal = kruskal(graph_kruskal)
print("Minimum Spanning Tree (Kruskal's Algorithm):", result_kruskal)
