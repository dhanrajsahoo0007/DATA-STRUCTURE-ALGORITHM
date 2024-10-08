"""
Problem Statement: Find Eventual Safe States

    There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
    The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, 
    meaning there is an edge from node i to each node in graph[i].
    A node is a terminal node if there are no outgoing edges.
    A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

    Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

    
*** IN THIS PROBLEM WE ARE EXCLUDING ELEMENTS WHICH ARE PATH OF A CYCLE 

Example 1:
    Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    Output: [2,4,5,6]

Example 2:
    Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    Output: [4]

Constraints:
    * n == graph.length
    * 1 <= n <= 10^4
    * 0 <= graph[i].length <= n
    * 0 <= graph[i][j] <= n - 1
    * graph[i] is sorted in a strictly increasing order.
    * The graph may contain self-loops.
    * The number of edges in the graph will be in the range [1, 4 * 10^4].

Time Complexity: O(N + E), where N is the number of nodes and E is the total number of edges in the graph.
Space Complexity: O(N), for the reversed graph, queue, and output list.
"""


def dfs(graph: list[list[int]], u: int, visited: list[bool], in_recursion: list[bool]) -> bool:
    visited[u] = True
    in_recursion[u] = True
    
    for v in graph[u]:
        if not visited[v]:
            if dfs(graph, v, visited, in_recursion):
                return True
        elif in_recursion[v]:
            return True
    
    in_recursion[u] = False
    return False

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V = len(graph)
        visited = [False] * V
        in_recursion = [False] * V
        
        for i in range(V):
            if not visited[i]:
                dfs(graph, i, visited, in_recursion)
        
        # Eliminating all the nodes that are in cycle 
        safe_nodes = [i for i in range(V) if not in_recursion[i]]
        return safe_nodes

# Test the solution
solution = Solution()

# Test case 1
"""
Graph 1 Visualization:

    0 --> 1 --> 2
    |     |     |
    v     |     v
    3     |     5
    ^     |
    |     v
    4 <-- 2     6

"""
graph1 = [[1,2],[2,3],[5],[0],[5],[],[]]
print("Graph 1 Safe Nodes:", solution.eventualSafeNodes(graph1))  # Expected: [2,4,5,6]

# Test case 2
"""
Graph 2 Visualization:

    0 --> 1 --> 2
    |     ^     ^
    |     |     |
    v     v     v
    3 --> 4 <-- 2

"""
graph2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print("Graph 2 Safe Nodes:", solution.eventualSafeNodes(graph2))  # Expected: [4]