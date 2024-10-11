def bfs_no_queue(graph, start):
    visited = []
    to_visit = [start]

    while to_visit:
        current = to_visit[0]
        to_visit = to_visit[1:]
        if current not in visited:
            visited.append(current)
            to_visit += [node for node in graph[current] if node not in visited]

    return visited

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

result = bfs_no_queue(graph, 1)
print("BFS Traversal:", result)
