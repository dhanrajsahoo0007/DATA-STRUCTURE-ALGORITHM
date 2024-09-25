"""
**Number of Provinces**

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.
A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.
Return *the total number of **provinces***.
 
**Example 1:**

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

**Example 2:**

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

**Solution:**
"""

from typing import List

def create_graph(V: int, isConnected: List[List[int]]) -> List[List[int]]:
    adj = [[] for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if isConnected[i][j] == 1 and i != j:
                adj[i].append(j)
    print(f"Printing the adjacency list created {adj}")
    return adj

def DFS(adj, u, visited):
    if visited[u] == True:
        return
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            DFS(adj, v, visited)

def findCircleNum(isConnected: List[List[int]]) -> int:
    V = len(isConnected)
    adj = create_graph(V, isConnected)
    visited = [False] * V
    provinces = 0
    
    for i in range(V):
        if not visited[i]:
            DFS(adj, i, visited)
            provinces += 1
    
    return provinces

"""
**Detailed Explanation:**

1. `create_graph` function:
   - Converts the `isConnected` matrix into an adjacency list representation.
   - Creates a list of lists `adj`, where `adj[i]` contains all cities directly connected to city `i`.
   - Iterates through the `isConnected` matrix and adds an edge (j) to `adj[i]` if `isConnected[i][j] == 1` and `i != j`.

2. `DFS` function:
   - Implements depth-first search.
   - Marks the current city `u` as visited.
   - Recursively visits all unvisited neighbors of `u`.

3. `findCircleNum` function:
   - Main function that solves the problem.
   - Creates the adjacency list using `create_graph`.
   - Initializes a `visited` array to keep track of visited cities.
   - Initializes a `provinces` counter to 0.
   - Iterates through all cities:
     - If a city hasn't been visited, starts a DFS from that city.
     - After each DFS, increments the `provinces` counter.
   - The number of times DFS is initiated is equal to the number of provinces.

The key insight is that each DFS traversal will visit all cities in a single province. So, the number of times we need to initiate DFS (on previously unvisited cities) is equal to the number of provinces.

**Time Complexity:** O(V^2), where V is the number of cities.
- Creating the adjacency list takes O(V^2) time.
- The DFS visits each city and each edge once, which takes O(V + E) time. In the worst case (when all cities are connected), E can be V^2.

**Space Complexity:** O(V)
- The adjacency list takes O(V + E) space, which in the worst case is O(V^2).
- The visited array takes O(V) space.
- The recursion stack in DFS can go up to O(V) in the worst case.
- However, we can optimize the space by not creating an explicit adjacency list and using the input matrix directly in DFS, which would reduce the space complexity to O(V).
"""

# Test cases
def test_findCircleNum():
    print("Running test cases for Number of Provinces:")
    print("-------------------------------------------")

    # Test case 1
    isConnected1 = [[1,1,0],[1,1,0],[0,0,1]]
    result1 = findCircleNum(isConnected1)
    print("Test case 1:")
    print(f"Input: {isConnected1}")
    print(f"Number of province : {result1}")
    print()

    # Test case 2
    isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]
    result2 = findCircleNum(isConnected2)
    print("Test case 2:")
    print(f"Input: {isConnected2}")
    print(f"Number of province : {result1}")
    print()

if __name__ == "__main__":
    test_findCircleNum()





from typing import List

def DFS(isConnected: List[List[int]], u: int, visited: List[bool]):
    if visited[u] == True:
        return
    visited[u] = True
    for v in range(len(isConnected)):
        if isConnected[u][v] == 1 and not visited[v]:
            DFS(isConnected, v, visited)

def findCircleNum(isConnected: List[List[int]]) -> int:
    V = len(isConnected)
    visited = [False] * V
    provinces = 0
    
    for i in range(V):
        if not visited[i]:
            DFS(isConnected, i, visited)
            provinces += 1
    
    return provinces
    