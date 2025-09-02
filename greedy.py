def greedy_best_first_search(graph, h, start, goal):
    open_list = [(start, [start])]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: h[x[0]])  # Choose node with lowest heuristic
        node, path = open_list.pop(0)

        if node == goal:
            return path

        visited.add(node)

        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                open_list.append((neighbor, path + [neighbor]))

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

path = greedy_best_first_search(graph, h, 'A', 'F')
print("GBFS Path:", " -> ".join(path) if path else "No path")
