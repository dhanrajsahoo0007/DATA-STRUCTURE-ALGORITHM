# Problem Statement:
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# Explanation:
# 1. We use a backtracking approach to generate all possible partitions.
# 2. The 'is_palindrome' function checks if a substring is a palindrome.
# 3. The 'backtrack' function:
#    - If we've reached the end of the string, we've found a valid partition.
#    - Otherwise, we try to extend the current partition with new palindromes.
# 4. We explore all possible end points for the current substring.
# 5. If a palindrome is found, we add it to the path and recurse on the rest of the string.
# 6. After exploring a path, we backtrack by removing the last added palindrome.

# Time Complexity: O(N * 2^N)
# - There are 2^N possible substrings in the worst case.
# - For each substring, we spend O(N) time to check if it's a palindrome.

# Space Complexity: O(N)
# - The recursion stack can go up to depth N in the worst case.
# - We also store the current path, which can be at most N long.

# Recursion Tree (for string "aab"):
#
#                  ""
#                  |
#                 "a"
#               /     \
#            "a|a"    "a"
#             |        |
#           "a|a|b"   "a|ab"
#
# Note: Each node represents a state in the backtracking process.
# The | symbol denotes partition points in the string.

# Optimization Note:
# We can optimize the palindrome checking by pre-computing all palindrome substrings
# using dynamic programming. This would reduce the time complexity to O(2^N).


class Solution:
    def partition(self, s: str):
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start:end+1])
                    backtrack(end + 1, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result

# Example usage
solution = Solution()
s = "aab"
partitions = solution.partition(s)

print(f"Palindromic partitions of '{s}':")
for i, partition in enumerate(partitions, 1):
    print(f"{i}. {partition}")

