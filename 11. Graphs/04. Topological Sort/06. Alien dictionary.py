"""
Problem Statement: Alien Dictionary

    There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.
    You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are
    sorted lexicographically by the rules of this new language.

    If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".
    Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

Example 1:
    Input: words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

Example 2:
    Input: words = ["z","x"]
    Output: "zx"

Example 3:
    Input: words = ["z","x","z"]
    Output: ""
    Explanation: The order is invalid, so return "".

Constraints:
    * 1 <= words.length <= 100
    * 1 <= words[i].length <= 100
    * words[i] consists of only lowercase English letters.

Time Complexity: O(C), where C is the total length of all words in the input list.
Space Complexity: O(1), since there are at most 26 lowercase English letters.
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Build the graph
        adj = defaultdict(list)
        chars = set(''.join(words))
        V = len(chars)
        char_to_index = {c: i for i, c in enumerate(chars)}
        print(f"char_to_index -> {char_to_index}")
        index_to_char = {i: c for c, i in char_to_index.items()}
        print(f"index_to_char -> {index_to_char}")


        # Compare adjacent words to build the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]  # Get adjacent pairs of words
            min_len = min(len(w1), len(w2))  # Find the length of the shorter word
            
            # Check if a longer word comes before its prefix (invalid case)
            # For example, "apple" should not come before "app"
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""  # This is an invalid ordering, so return an empty string
            
            # Compare characters of w1 and w2
            for j in range(min_len):
                if w1[j] != w2[j]:  # Find the first differing character
                    # Convert characters to their corresponding indices
                    u, v = char_to_index[w1[j]], char_to_index[w2[j]]
                    
                    # Add this ordering information to the graph
                    # This means character w1[j] comes before w2[j] in the alien alphabet
                    if v not in adj[u]:
                        adj[u].append(v)
                    
                    # We've found the first difference, so we can stop comparing these words
                    break
        print(f"adj -> {adj}")

        # Topological sort using Kahn's algorithm
        # Calculate in-degree for each vertex
        in_degree = [0] * V
        for u in range(V):
            for v in adj[u]:
                in_degree[v] += 1

        # Initialize queue with vertices having 0 in-degree
        queue = deque()
        for u in range(V):
            if in_degree[u] == 0:
                queue.append(u)

        topological_order = []

        # Process vertices in topological order
        while queue:
            u = queue.popleft()
            topological_order.append(u)

            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # Check if topological sort is possible (no cycle)
        if len(topological_order) == V:
            return ''.join(index_to_char[i] for i in topological_order)
        else:
            return ""  # Graph has at least one cycle

# Test cases
solution = Solution()
print("===========================")
print(solution.alienOrder(["wrt","wrf","er","ett","rftt"]))  # Expected output: "wertf"
print("===========================")
print(solution.alienOrder(["z","x"]))  # Expected output: "zx"
print("===========================")
print(solution.alienOrder(["z","x","z"]))  # Expected output: ""