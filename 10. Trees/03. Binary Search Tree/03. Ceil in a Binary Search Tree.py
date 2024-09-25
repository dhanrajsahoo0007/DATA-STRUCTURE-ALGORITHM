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