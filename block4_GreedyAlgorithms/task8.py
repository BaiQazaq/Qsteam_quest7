# 8. Create a greedy algorithm to solve the graph coloring problem.

# In this implementation, the greedy_coloring function takes an adjacency list representation of the graph as input. 
# It iterates through the vertices in descending order of their degree (number of neighbors) and assigns colors 
# to each vertex by choosing the smallest available color not used by its neighbors.

# Keep in mind that the greedy algorithm may not always produce the optimal coloring, and the number of colors 
# used might be more than the chromatic number of the graph (the minimum number of colors needed for a valid coloring). 
# However, it provides a reasonable solution in many cases and is computationally efficient

def greedy_coloring(graph):
    """
    Solve the graph coloring problem using a greedy algorithm.

    Parameters:
    - graph: An adjacency list representation of the graph. Each element is a tuple (neighbor,).

    Returns:
    - A dictionary where keys are vertices and values are colors assigned to the vertices.
    """
    colors = {}  # Dictionary to store the assigned colors

    # Sort vertices by their degree (number of neighbors) in descending order
    vertices = sorted(graph.keys(), key=lambda vertex: len(graph[vertex]), reverse=True)

    for vertex in vertices:
        neighbor_colors = {colors[neighbor] for neighbor in graph[vertex] if neighbor in colors}

        # Find the smallest available color for the current vertex
        color = 1
        while color in neighbor_colors:
            color += 1

        colors[vertex] = color

    return colors

# Example usage:
graph_coloring = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}

result_coloring = greedy_coloring(graph_coloring)
print("Vertex Colors (Greedy Algorithm):", result_coloring)
