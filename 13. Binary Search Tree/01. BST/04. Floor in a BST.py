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

Initial Binary Search Tree:
       8
     /   \
    4     12
   / \   /  \
  2   6 10  14

Binary Search Tree after inserting 5:
       8
     /   \
    4     12
   / \   /  \
  2   6 10  14
     /
    5
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

# Example usage
if __name__ == "__main__":
    # Create the initial tree
    root = TreeNode(8)
    root.left = TreeNode(4)
    root.right = TreeNode(12)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(14)

    # Insert a new node with value 5
    new_value = 5
    root = insert(root, new_value)

    print(f"New value {new_value} has been inserted into the BST.")