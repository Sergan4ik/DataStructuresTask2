class Node:
    def __init__(self, key, color):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key, "RED")

        if self.root is None:
            self.root = node
        else:
            curr = self.root
            parent = None
            while curr is not None:
                parent = curr
                if key < curr.key:
                    curr = curr.left
                else:
                    curr = curr.right

            node.parent = parent
            if key < parent.key:
                parent.left = node
            else:
                parent.right = node

        self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._left_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def delete(self, key):
        node = self._find_node(key)
        if node is None:
            return

        self._delete_node(node)

    def _delete_node(self, node):
        if node.left is None or node.right is None:
            delete_node = node
        else:
            delete_node = self._successor(node)

        if delete_node.left is not None:
            child = delete_node.left
        else:
            child = delete_node.right

        if child is not None:
            child.parent = delete_node.parent

        if delete_node.parent is None:
            self.root = child
        elif delete_node == delete_node.parent.left:
            delete_node.parent.left = child
        else:
            delete_node.parent.right = child

        if delete_node != node:
            node.key = delete_node.key

        if delete_node.color == "BLACK":
            self._fix_delete(child, delete_node.parent)

    def _fix_delete(self, node, parent):
        while node != self.root and (node is None or node.color == "BLACK"):
            if node == parent.left:
                sibling = parent.right
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    parent.color = "RED"
                    self._left_rotate(parent)
                    sibling = parent.right
                if (sibling.left is None or sibling.left.color == "BLACK") and \
                        (sibling.right is None or sibling.right.color == "BLACK"):
                    sibling.color = "RED"
                    node = parent
                else:
                    if sibling.right is None or sibling.right.color == "BLACK":
                        if sibling.left is not None:
                            sibling.left.color = "BLACK"
                        sibling.color = "RED"
                        self._right_rotate(sibling)
                        sibling = parent.right
                    sibling.color = parent.color
                    parent.color = "BLACK"
                    sibling.right.color = "BLACK"
                    self._left_rotate(parent)
                    node = self.root
            else:
                sibling = parent.left
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    parent.color = "RED"
                    self._right_rotate(parent)
                    sibling = parent.left
                if (sibling.right is None or sibling.right.color == "BLACK") and \
                        (sibling.left is None or sibling.left.color == "BLACK"):
                    sibling.color = "RED"
                    node = parent
                else:
                    if sibling.left is None or sibling.left.color == "BLACK":
                        if sibling.right is not None:
                            sibling.right.color = "BLACK"
                        sibling.color = "RED"
                        self._left_rotate(sibling)
                        sibling = parent.left
                    sibling.color = parent.color
                    parent.color = "BLACK"
                    sibling.left.color = "BLACK"
                    self._right_rotate(parent)
                    node = self.root

        if node is not None:
            node.color = "BLACK"

    def _find_node(self, key):
        curr = self.root
        while curr is not None:
            if key == curr.key:
                return curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child
        left_child.right = node
        node.parent = left_child

    def _successor(self, node):
        if node.right is not None:
            curr = node.right
            while curr.left is not None:
                curr = curr.left
            return curr
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def print_tree(self):
        self._print_tree_helper(self.root, "", True)

    def _print_tree_helper(self, node, indent, is_last):
        if node is not None:
            marker = "└── " if is_last else "├── "
            print(indent + marker + str(node.key) + " (" + node.color + ")")
            indent += "    " if is_last else "│   "
            self._print_tree_helper(node.left, indent, False)
            self._print_tree_helper(node.right, indent, True)


keys = [47, 25, 78, 50, 30, 11, 59, 18, 36, 94]
rb_tree = RedBlackTree()

for key in keys:
    rb_tree.insert(key)

print("Red-Black Tree:")
rb_tree.print_tree()

key_to_delete = 30
rb_tree.delete(key_to_delete)

print("\nAfter deleting element", key_to_delete)
rb_tree.print_tree()
