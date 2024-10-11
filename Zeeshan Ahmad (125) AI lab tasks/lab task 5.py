class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def dfs_with_stack(root):
    if root is None:
        return
    
    stack = [root]
    visited = []
    
    while stack:
        current_node = stack.pop()
        visited.append(current_node.value)
        for child in reversed(current_node.children):
            stack.append(child)
    
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

result = dfs_with_stack(root)
print("DFS Traversal:", result)

