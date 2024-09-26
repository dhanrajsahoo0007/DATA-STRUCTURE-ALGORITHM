from typing import List
from collections import defaultdict

# The problem is same as detecting cycle in a graph 


class Solution:
    def isCycleDFS(self, adj: dict, u: int, visited: List[bool], inRecursion: List[bool]) -> bool:
        visited[u] = True
        inRecursion[u] = True
        
        for v in adj[u]:
            # if not visited, then we check for cycle in DFS
            if not visited[v] and self.isCycleDFS(adj, v, visited, inRecursion):
                return True
            elif inRecursion[v]:
                return True
        
        inRecursion[u] = False
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = [False] * numCourses
        inRecursion = [False] * numCourses
        
        for a, b in prerequisites:
            # b ---> a
            adj[b].append(a)
        
        for i in range(numCourses):
            if not visited[i] and self.isCycleDFS(adj, i, visited, inRecursion):
                # If there is a cycle that means we can't complete all the cycles 
                # so return False 
                return False
        
        return True

# Test cases
solution = Solution()
print(solution.canFinish(2, [[1,0]]))  # Should return True
print(solution.canFinish(2, [[1,0],[0,1]]))  # Should return False