"""
39. Combination Sum
Solved
Medium
Topics
Companies
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time Complexity: O(n^target/min(candidates)). In the worst case, the state-space tree has n branches and the depth of the tree is at most target divided by the smallest number in candidates.
        """
        results : List[List[int]] = []
        n = len(candidates)
        def dfs(starting_index, curr_sum: int, target: int, path: List):
            if curr_sum == target:
                results.append(path[::])
                return
            for index in range(starting_index, n):
                num = candidates[index]
                new_sum = curr_sum + num
                if new_sum > target:
                    continue
                dfs(index, new_sum, target, path+[num])
            return
        candidates.sort()
        dfs(starting_index=0, curr_sum=0, target=target, path=[])
        return results
