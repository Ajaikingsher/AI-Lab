def a_star(graph, h, start, goal):
    open_list = [(start, [start], 0)]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: x[2] + h[x[0]])  # f(n) = g(n)+h(n)
        node, path, cost = open_list.pop(0)

        if node == goal:
            return path

        visited.add(node)

        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                open_list.append((neighbor, path + [neighbor], cost + edge_cost))

    return None


# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values
h = {'A': 7, 'B': 6, 'C': 2, 'D': 4, 'E': 1, 'F': 0}

path = a_star(graph, h, 'A', 'F')
print("A* Path:", " -> ".join(path) if path else "No path")