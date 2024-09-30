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


from typing import List
from collections import deque

from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        adj = [[] for _ in range(V)]
        
        que = deque()
        indegree = [0] * V
        
        # 1. Build reversed adjacency list and calculate indegree
        for u in range(V):
            for v in graph[u]:
                adj[v].append(u)
                indegree[u] += 1
        
        # 2. Fill queue with nodes having indegree 0
        for i in range(V):
            if indegree[i] == 0:
                que.append(i)
        
        # 3. BFS
        safe = [False] * V
        while que:
            u = que.popleft()
            safe[u] = True
            
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    que.append(v)
        
        # 4. Collect and return safe nodes
        return [i for i in range(V) if safe[i]]

# Test the solution
solution = Solution()

# Test case 1
"""
Graph 1 Visualization:

    1 <--> 2
    ^      |
    |      v
    0 <--- 3
    ^
    |
    4 ---> 5 --> 6

"""
graph1 = [[1,2],[2,3],[5],[0],[5],[],[]]
print(f"Printing the Graph - > {graph1}")
print(solution.eventualSafeNodes(graph1))  # Expected output: [2,4,5,6]

# Test case 2
"""
Graph 2 Visualization:

    0 <--> 1 <--> 2
    ^      ^      ^
    |      |      |
    v      v      v
    3 <--> 4

"""
graph2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(f"Printing the Graph - > {graph2}")
print(solution.eventualSafeNodes(graph2))  # Expected output: [4]