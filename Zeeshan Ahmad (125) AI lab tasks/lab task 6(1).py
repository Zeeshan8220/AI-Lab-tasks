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


#part 2

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def bfs_with_queue(root):
    if not root:
        return []
    
    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node.value)
        queue.extend(node.children)

    return visited

root = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)
child4 = Node(5)

root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)
child1.add_child(child4)

result = bfs_with_queue(root)
print("BFS Traversal:", result)
