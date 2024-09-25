from typing import List
from collections import deque

class Solution:
    def checkBipartiteBFS(self, adj: List[List[int]], curr: int, color: List[int], curr_color: int) -> bool:
        color[curr] = curr_color  # color the current node
        
        que = deque([curr])
        
        while que:
            u = que.popleft()
            
            for v in adj[u]:
                if color[v] == color[u]:
                    return False
                elif color[v] == -1:
                    color[v] = 1 - color[u]
                    que.append(v)
        
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1] * V  # no node colored in the start
        
        # red = 1
        # green = 0
        
        for i in range(V):
            if color[i] == -1:
                if not self.checkBipartiteBFS(graph, i, color, 1):
                    return False
        
        return True

# Test cases
solution = Solution()
print(solution.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))  # Expected output: False
print(solution.isBipartite([[1,3],[0,2],[1,3],[0,2]]))  # Expected output: True