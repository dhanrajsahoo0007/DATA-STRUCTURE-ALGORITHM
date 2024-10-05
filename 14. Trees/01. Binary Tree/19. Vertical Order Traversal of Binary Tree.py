from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        
        # Use a dictionary to store nodes at each vertical line
        # Key: vertical, Value: list of (level, value) tuples
        verticalTable = defaultdict(list)
        
        def dfs(node, level, vertical):
            if not node:
                return
            
            # Add the node to the vertical table
            verticalTable[vertical].append((level, node.val))
            
            # Traverse left and right children
            dfs(node.left, level + 1, vertical - 1)
            dfs(node.right, level + 1, vertical + 1)
        
        # Start DFS from the root
        dfs(root, 0, 0)
        
        # Sort the vertical table and create the result
        result = []
        for vertical in sorted(verticalTable.keys()):
            # Sort nodes in this vertical line by level and then by value
            verticalLine = [val for level, val in sorted(verticalTable[vertical])]

            # above line or below 
            # nodes = verticalTable[vertical]
            # nodes.sort()  # Sort by level, then by value
            # verticalLine = []
            # for _, val in nodes:
            #     verticalLine.append(val)
            result.append(verticalLine)
        
        return result

# Example usage
def create_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

solution = Solution()
tree = create_tree()
vertical_order = solution.verticalTraversal(tree)
print("Vertical Order Traversal:", vertical_order)