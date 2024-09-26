from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_dfs(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_dfs(root.left, val)
    elif val > root.val:
        root.right = insert_dfs(root.right, val)
    return root

def insert_bfs(root, val):
    if not root:
        return TreeNode(val)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if val < node.val:
            if node.left:
                queue.append(node.left)
            else:
                node.left = TreeNode(val)
                break
        elif val > node.val:
            if node.right:
                queue.append(node.right)
            else:
                node.right = TreeNode(val)
                break
        else:
            break
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def construct_and_print_bst(insert_function, values):
    root = None
    for value in values:
        root = insert_function(root, value)
    print("Inorder traversal of the constructed BST:")
    inorder(root)
    print()  # For a new line after inorder traversal

# Example usage
values = [5, 3, 7, 1, 4, 6, 8]

print("Using DFS (recursive) approach:")
construct_and_print_bst(insert_dfs, values)

print("\nUsing BFS approach:")
construct_and_print_bst(insert_bfs, values)