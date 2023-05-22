import random


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)


def preorder_traversal(node):
    if node is not None:
        print(node.key, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.key, end=" ")


keys = []
for i in range(16):
    keys.append(random.randint(0 , 100))

print(keys)

root = None
for key in keys:
    root = insert(root, key)

print("Binary Search Tree:")
print("Inorder Traversal:")
inorder_traversal(root)
print("\nPreorder Traversal:")
preorder_traversal(root)
print("\nPostorder Traversal:")
postorder_traversal(root)
