"""
Problem Statement:
Given a Binary Search Tree (BST) and a new node value, insert the new node into the BST.
A Binary Search Tree is a binary tree where for each node:
- All nodes in the left subtree have values less than the node's value.
- All nodes in the right subtree have values greater than the node's value.
- Both the left and right subtrees are also binary search trees.

Time Complexity: O(h), where h is the height of the tree.
- In the worst case (skewed tree), h can be O(n), where n is the number of nodes.
- In the average case (balanced tree), h is O(log n).

Space Complexity: O(h) for the recursive call stack.
- In the worst case, O(n) for a skewed tree.
- In the average case, O(log n) for a balanced tree.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")

# Example usage
if __name__ == "__main__":
    root = None
    values = [5, 3, 7, 1, 4, 6, 8]
    
    for value in values:
        root = insert(root, value)
    
    print("Binary Search Tree after insertion:")
    print_tree(root)