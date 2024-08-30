# Base case: If the root is None (empty tree), we return 0.

# Recursive case:
    # We recursively calculate the height of the left subtree.
    # We recursively calculate the height of the right subtree.
    # We return the maximum of these two heights, plus 1 (to account for the current node).


# This recursive approach has:

# Time complexity: O(n), where n is the number of nodes in the tree, as we visit each node once.
# Space complexity: O(h), where h is the height of the tree, due to the recursion stack. In the worst case of a skewed tree, this could be O(n).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height_of_binary_tree(root):
    if root is None:
        return 0
    
    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)
    
    return max(left_height, right_height) + 1

# Test the function
# Creating a sample binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Height of the binary tree:", height_of_binary_tree(root))