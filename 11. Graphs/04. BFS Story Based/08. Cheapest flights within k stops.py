"""
Problem Statement:
    There are n cities connected by some number of flights. You are given an array flights where 
    flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

    You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
    If there is no such route, return -1.

Time Complexity: O((N + E) * log(N)), where N is the number of cities and E is the number of flights.
                In the worst case, this could be O(N^2 * log(N)) if the graph is dense (i.e., there are flights between every pair of cities).

Space Complexity: O(N + E)
    - O(N) for the distances and stops arrays
    - O(E) for the graph adjacency list
    - O(N) for the priority queue in the worst case

The total space complexity is therefore O(N + E).
"""

from typing import List
from collections import deque, defaultdict
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [math.inf] * n
        
        # Create adjacency list
        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append((v, cost))
        
        queue = deque([(src, 0)])
        distance[src] = 0
        
        level = 0
        
        while queue and level <= k:
            N = len(queue)
            
            for _ in range(N):
                u, d = queue.popleft()
                
                for v, cost in adj[u]:
                    if distance[v] > d + cost:
                        distance[v] = d + cost
                        queue.append((v, d + cost))
            
            level += 1
        
        return distance[dst] if distance[dst] != math.inf else -1

# Test the function
solution = Solution()
print(solution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))  # Output: 700
print(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))  # Output: 200
print(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))  # Output: 500



