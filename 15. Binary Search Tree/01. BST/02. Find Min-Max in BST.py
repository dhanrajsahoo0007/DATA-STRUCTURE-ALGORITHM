"""
Problem Statement:
Implement a Binary Search Tree (BST) with the following operations:
    1. Insert a value
    2. Search for a value
    3. Find the minimum value
    4. Find the maximum value

A BST is a binary tree where for each node:
- All nodes in the left subtree have values less than the node's value.
- All nodes in the right subtree have values greater than the node's value.

Time Complexity:
- Insert: O(h) - where h is the height of the tree
- Search: O(h)
- Find Min: O(h)
- Find Max: O(h)

In a balanced BST, h = log(n), where n is the number of nodes, 
so these operations would be O(log n).

In the worst case (skewed tree), h = n, so these operations would be O(n).

Space Complexity:
- For all operations: O(h) due to the recursive call stack.
- Overall tree storage: O(n) where n is the number of nodes.

Example BST:
       5
     /   \
    3     7
   / \   / \
  1   4 6   8

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def find_min(self):
        if not self.root:
            return None
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, node):
        if node.left is None:
            return node.value
        return self._find_min_recursive(node.left)

    def find_max(self):
        if not self.root:
            return None
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        if node.right is None:
            return node.value
        return self._find_max_recursive(node.right)

# Example usage
bst = BinarySearchTree()
values = [5, 3, 7, 1, 4, 6, 8]
for value in values:
    bst.insert(value)

# Search for a value
search_value = 4
result = bst.search(search_value)
print(f"Value {search_value} {'found' if result else 'not found'} in the BST")

# Find minimum and maximum
min_value = bst.find_min()
max_value = bst.find_max()
print(f"Minimum value in the BST: {min_value}")
print(f"Maximum value in the BST: {max_value}")