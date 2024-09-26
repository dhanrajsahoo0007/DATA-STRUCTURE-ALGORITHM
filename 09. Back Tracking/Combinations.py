"""
Problem: Combinations
    Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
    You may return the answer in any order.

Examples:
    1. Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    2. Input: n = 1, k = 1
    Output: [[1]]

    Constraints:
    * 1 <= n <= 20
    * 1 <= k <= n

Time Complexity: O(n choose k) = O(n! / (k! * (n-k)!))
This is because we generate all possible combinations of k elements from n elements.

Space Complexity: O(k) for the recursion stack, as the maximum depth is k.
The space needed to store the output is not considered in space complexity analysis.

Approach: Backtracking
    1. Use a recursive function to generate combinations.
    2. At each step, decide whether to include the current number or not.
    3. Keep track of the current combination and the next number to consider.
    4. When the combination size reaches k, add it to the result.

Explanation of the backtracking process:

    1. The backtrack function takes two parameters:
    - start: the starting number to consider for the current position
    - current_combination: the combination being built

    2. Base case:
    - If the length of current_combination equals k, we've found a valid combination

    3. Recursive case:
    - We iterate through numbers from 'start' to 'n'
    - For each number, we:
        a. Add it to the current combination
        b. Make a recursive call, moving to the next position (i + 1)
        c. Remove the number (backtrack) to explore other possibilities

    4. The main function initializes the process with start = 1 and an empty combination

    Recursion tree for n = 4, k = 2:

                    []
            /        /      \         \
        [1]          [2]        [3]   [4]
        / | \         / \        |
    [1,2][1,3][1,4] [2,3][2,4]  [3,4]

This tree shows how combinations are built and explored. 
Each leaf node at depth 2 represents a valid combination.
"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(start, current_combination):
            if len(current_combination) == k:
                result.append(current_combination[:])
                return
            
            for i in range(start, n + 1):
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop()
        
        result = []
        backtrack(1, [])
        return result

# Test cases
sol = Solution()
print(sol.combine(4, 2))  # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(sol.combine(1, 1))  # Output: [[1]]
print(sol.combine(5, 4))  # Output: [[1]]


