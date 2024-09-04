"""
Diameter of Binary Tree

Problem Statement:
    Given the root of a binary tree, return the length of the diameter of the tree.
    
Explanation:
    1. We use a depth-first search (DFS) approach to traverse the tree.
    2. For each node, we calculate:
    a) The height of its left subtree
    b) The height of its right subtree
    3. The potential diameter through this node is the sum of these heights.
    4. We keep track of the maximum diameter seen so far.
    5. We return the height of the current subtree to the parent call.

Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case of a skewed tree, it can be O(n).

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update the diameter if the path through this node is longer
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the longest path starting from this node
            return max(left_height, right_height) + 1
        
        dfs(root)
        return self.diameter



# Helper function to create a binary tree from a list
def create_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1: [1,2,3,4,5]
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root1 = create_tree([1,2,3,4,5])
    print("Example 1:")
    print("Diameter:", solution.diameterOfBinaryTree(root1))  # Expected output: 3

    # Example 2: [1,2]
    #     1
    #    /
    #   2
    root2 = create_tree([1,2])
    print("\nExample 2:")
    print("Diameter:", solution.diameterOfBinaryTree(root2))  # Expected output: 1

    # Example 3: [1,2,3,4,5,None,None,8,9,None,None,11,12]
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    #   / \   \
    #  8   9   11
    #           \
    #           12
    root3 = create_tree([1,2,3,4,5,None,None,8,9,None,None,11,12])
    print("\nExample 3:")
    print("Diameter:", solution.diameterOfBinaryTree(root3))  # Expected output: 6