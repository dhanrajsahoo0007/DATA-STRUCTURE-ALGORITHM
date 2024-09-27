"""
Problem Statement:
    Implement a method to find the ceiling of a given number in a Binary Search Tree (BST).
    The ceiling of a number X in a BST is the smallest element in the BST that is greater than or equal to X.

Time Complexity: O(h), where h is the height of the tree
Space Complexity: O(h) due to the recursive call stack

Example BST:
       8
     /   \
    4     12
   / \   /  \
  2   6 10  14

For this BST:
    ceil(5) = 6
    ceil(13) = 14
    ceil(15) = None
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findCeil(root, key):
    ceil = None
    
    while root:
        if root.val == key:
            return root.val
        
        if key > root.val:
            root = root.right
        else:
            ceil = root.val
            root = root.left
    
    return ceil

# Example usage
root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(12)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)

print(findCeil(root, 5))  # Output: 6
print(findCeil(root, 11))  # Output: 12
print(findCeil(root, 15))  # Output: None