"""

Problem Statement:
Combination Target Sum II
    You are given an array of integers nums, which may contain duplicates,
    and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
    Each element from nums may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

    You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

        Input: candidates = [9,2,2,4,6,1,5], target = 8

        Output: [
        [1,2,5],
        [2,2,4],
        [2,6]
        ]
        
Example 2:

    Input: candidates = [1,2,3,4,5], target = 7

    Output: [
    [1,2,4],
    [2,5],
    [3,4]
    ]
    Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30


Approach:
    1. Sort the candidates array to handle duplicates and enable pruning.
    2. Use backtracking to explore all possible combinations.
    3. Skip duplicates at the same level of recursion to avoid duplicate combinations.
    4. Use an index to ensure each number is used only once in a combination.

Time Complexity: 
    O(2^n), where n is the number of candidates.
    In the worst case, we might need to explore all possible subsets.

Space Complexity: 
    O(n), where n is the number of candidates.
    This accounts for the recursion stack and the space to store combinations.
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        candidates.sort()  # Sort to handle duplicates and enable pruning
        result = []
        backtrack(0, target, [])
        return result

# Example usage:
solution = Solution()
print(solution.combinationSum2([9,2,2,4,6,1,5], 8))
# print(solution.combinationSum2([1,2,3,4,5], 7))


# Key Points:
# 1. Sorting is crucial for handling duplicates and enabling pruning.
# 2. Skipping duplicates at the same level prevents duplicate combinations.
# 3. Using 'i + 1' in the recursive call ensures each number is used only once.
# 4. Backtracking allows efficient exploration of all possibilities.

# Visualization of the backtracking process for [9,2,2,4,6,1,5], target = 8:
#
#                []
#         /      /       \     \   \
#       [1]     [2]     [4]   [5] [6]
#      /  \      |       |
#   [1,2][1,5]  [2,2]   [2,4]
#     |    |     |
# [1,2,5] [1,6] [2,2,4]
#
# This tree shows how:
# 1. Duplicates (like 2) are handled at each level.
# 2. Paths are pruned when they exceed the target.
# 3. Valid combinations are found at different depths.

# Optimization:
# 1. Early termination when a candidate exceeds the target.
# 2. Skipping duplicates reduces unnecessary exploration.