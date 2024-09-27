"""
Problem Statement:
    Given a maze of size N x N, find all possible paths that a rat can take to reach
    from the source (0, 0) to the destination (N-1, N-1).
    The rat can move only in two directions: forward and down. 
    In the maze matrix, 0 means the cell is a dead and
    end and 1 means the cell can be used in the path from source to destination.


    Visualization of the maze (1 represents open path, 0 represents blocked)

    [1, 0, 0, 0]
    [1, 1, 0, 1]
    [0, 1, 0, 0]
    [1, 1, 1, 1]

    Start: (0, 0)
    End: (3, 3)

Explanation:
    1. We use a backtracking approach to explore all possible paths.
    2. The rat can move only right or down, represented by the 'moves' list.
    3. We keep track of visited cells to avoid loops and ensure we don't revisit cells.
    4. When we reach the destination (bottom-right corner), we add the current path to our list of paths.
    5. After exploring a path, we backtrack by marking the cell as unvisited and removing it from the current path.

Time Complexity: O(2^(n^2))
    In the worst case, we might have to explore every possible path in the maze.
    Each cell has two choices (right or down), and there are n^2 cells.

Space Complexity: O(n^2)
    We use a visited array of size n x n, and the recursion stack can go up to n^2 in the worst case.

Recursion Tree (simplified for a 2x2 maze):

               (0,0)
              /     \
           (0,1)    (1,0)
            |         |
          (1,1)     (1,1)

Note: The actual recursion tree for a 4x4 maze would be much larger.

"""


def is_safe(maze, x, y, n):
    """Check if (x, y) is a valid and open position in the maze."""
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

def find_paths(maze):
    n = len(maze)
    # To keep track of visited cells
    visited = [[False for _ in range(n)] for _ in range(n)]
    #visited = [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]]
    
    paths = []
    current_path = []
    
    def backtrack(x, y):
        # If we've reached the destination , end of the matrix from the bottom right 
        if x == n - 1 and y == n - 1:
            paths.append(current_path[:])
            return
        
        # Possible moves: right and down
        moves = [(0, 1), (1, 0)]
        
        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            if is_safe(maze, next_x, next_y, n) and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                current_path.append((next_x, next_y))
                
                backtrack(next_x, next_y)
                
                # Backtrack
                visited[next_x][next_y] = False
                current_path.pop()
    
    # Start from (0, 0) if it's a valid position
    if maze[0][0] == 1:
        visited[0][0] = True
        current_path.append((0, 0))
        backtrack(0, 0)
    
    return paths

# Example usage
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

paths = find_paths(maze)
print(f"Number of paths found: {len(paths)}")
for i, path in enumerate(paths, 1):
    print(f"Path {i}: {path}")


