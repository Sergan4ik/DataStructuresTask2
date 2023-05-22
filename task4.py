import random
from math import log

class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.degree = 0

    def add_child(self, node):
        self.children.append(node)
        self.degree += 1


class BinomialHeap:
    def __init__(self):
        self.trees = []

    def merge(self, heap):
        self.trees.extend(heap.trees)
        self._consolidate()

    def insert(self, key):
        node = BinomialNode(key)
        heap = BinomialHeap()
        heap.trees.append(node)
        self.merge(heap)

    def find_min(self):
        if not self.trees:
            return None

        min_node = self.trees[0]
        for tree in self.trees:
            if tree.key < min_node.key:
                min_node = tree

        return min_node.key

    def delete_min(self):
        if not self.trees:
            return None

        min_node = self.trees[0]
        for tree in self.trees:
            if tree.key < min_node.key:
                min_node = tree

        self.trees.remove(min_node)
        child_heap = BinomialHeap()
        child_heap.trees = min_node.children[::-1]
        self.merge(child_heap)

        return min_node.key

    def _consolidate(self):
        max_degree = max(tree.degree for tree in self.trees) + 1
        degree_table = [None] * (max_degree + 1)

        i = 0
        while i < len(self.trees):
            tree = self.trees[i]
            degree = tree.degree

            while degree_table[degree] is not None:
                other_tree = degree_table[degree]

                if tree.key > other_tree.key:
                    tree, other_tree = other_tree, tree

                tree.add_child(other_tree)
                self.trees.remove(other_tree)
                degree_table[degree] = None
                degree += 1

            degree_table[degree] = tree
            i += 1


def print_binomial_trees(heaps):
    for i, heap in enumerate(heaps):
        print(f"Binomial Tree {i+1}:")
        for tree in heap.trees:
            print_tree(tree, 0)
        print()


def print_tree(node, level):
    print("  " * level + str(node.key))
    for child in node.children:
        print_tree(child, level + 1)



keys = random.sample(range(101), 15)

heap = BinomialHeap()
for key in keys:
    heap.insert(key)

print("Binominal trees:")
print_binomial_trees([heap])

