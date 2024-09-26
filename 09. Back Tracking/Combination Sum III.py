"""
Problem Statement:
    Find all valid combinations of k numbers that sum up to n such that:
    1. Only numbers 1 through 9 are used.
    2. Each number is used at most once.
    Return a list of all possible valid combinations.


Example 1:
    Input: k = 3, n = 7
    Output: [[1,2,4]]
    Explanation:
    1 + 2 + 4 = 7
    There are no other valid combinations.
Example 2:
    Input: k = 3, n = 9
    Output: [[1,2,6],[1,3,5],[2,3,4]]
    Explanation:
    1 + 2 + 6 = 9
    1 + 3 + 5 = 9
    2 + 3 + 4 = 9
    There are no other valid combinations.
    Example 3:


Approach:
    1. Use backtracking to generate all possible combinations of k numbers.
    2. Start with numbers from 1 to 9, and for each number, decide whether to include it or not.
    3. Keep track of the current sum and the number of elements selected.
    4. When k numbers are selected, check if their sum equals n.
    5. Use pruning to optimize: stop exploring if sum exceeds n or if we can't reach n.

Time Complexity: O(C(9,k)), where C(9,k) is the binomial coefficient.
In the worst case, we explore all possible combinations of k numbers from 9 choices.

Space Complexity: O(k), where k is the number of elements in each combination.
This accounts for the recursion stack and the space to store each combination.



Key Points:
    1. We only consider numbers from 1 to 9.
    2. Each number is used at most once in a combination.
    3. The backtracking function uses 'start' to ensure numbers are used in ascending order.
    4. Early pruning is applied when the combination size exceeds k or the sum exceeds n.
    5. The solution naturally avoids duplicate combinations due to the ascending order selection.

Visualization of the backtracking process for k=3, n=7:

                 []
        /        |        \
      [1]       [2]       [3]
    /     \    /   \     /   \
 [1,2]  [1,3] [2,3] [2,4] [3,4] [3,5]
  /  \    |     |     |     x     x
[1,2,3] [1,2,4] [1,3,4] [2,3,4]
   x      *       x       x

Legend:
    * - Valid solution
    x - Pruned (sum > n or combination size > k)
    
This tree shows how:
    1. The algorithm explores combinations in ascending order.
    2. Branches are pruned when the sum exceeds 7 or when more than 3 numbers are selected.
    3. [1,2,4] is identified as the only valid solution.

Optimization:
    1. Early termination when the combination size exceeds k or the sum exceeds n.
    2. Starting from 'start' in each recursive call prevents duplicate considerations.

"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        def backtrack(start, combination, current_sum):
            if len(combination) == k and current_sum == n:
                result.append(combination[:])
                return
            
            if len(combination) > k or current_sum > n:
                return
            
            for i in range(start, 10):
                combination.append(i)
                backtrack(i + 1, combination, current_sum + i)
                combination.pop()

        result = []
        backtrack(1, [], 0)
        return result

# Example usage:
solution = Solution()
print(solution.combinationSum3(3, 7))  # Output: [[1,2,4]]
print(solution.combinationSum3(3, 9))  # Output: [[1,2,6],[1,3,5],[2,3,4]]
print(solution.combinationSum3(2, 9))  # Output: []