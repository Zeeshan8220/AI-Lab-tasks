def a_star(graph, start, goal, h):
    open_list = [start]
    g_scores = {start: 0}
    f_scores = {start: h[start]}
    came_from = {}

    while open_list:
        current = min(open_list, key=lambda node: f_scores[node])

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_list.remove(current)

        for neighbor, cost in graph[current]:
            tentative_g_score = g_scores[current] + cost
            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = g_scores[neighbor] + h[neighbor]
                came_from[neighbor] = current
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': [('E', 2)],
    'E': []
}

h = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 0
}

result = a_star(graph, 'A', 'E', h)
print("A* Path:", result)
