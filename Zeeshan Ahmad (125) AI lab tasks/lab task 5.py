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

#2

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root):
    result = []
    stack = []
    current = root

    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            result.append(current.value)
            current = current.right
        else:
            break
    
    return result

def preorder(root):
    result = []
    if root is None:
        return result
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

def postorder(root):
    result = []
    if root is None:
        return result
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result[::-1]  
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder_traversal = inorder(root)
preorder_traversal = preorder(root)
postorder_traversal = postorder(root)

print("Inorder Traversal:", inorder_traversal)
print("Preorder Traversal:", preorder_traversal)
print("Postorder Traversal:", postorder_traversal)

