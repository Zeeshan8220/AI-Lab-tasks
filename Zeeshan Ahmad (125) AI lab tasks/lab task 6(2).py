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
