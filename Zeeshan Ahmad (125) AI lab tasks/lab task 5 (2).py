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
