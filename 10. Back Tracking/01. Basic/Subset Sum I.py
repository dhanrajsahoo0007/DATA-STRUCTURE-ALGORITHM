"""
Problem Statement:
    Given an integer array nums of unique elements, return all possible subsets(the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    Example 1:
        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    Example 2:
        Input: nums = [0]
        Output: [[],[0]]
        
Explanation:

1. Approach:
   - This solution uses Depth-First Search (DFS) to generate all subsets.
   - For each element, we make two decisions: include it or not include it.

2. Implementation Details:
   - res: Stores all generated subsets.
   - subset: Represents the current subset being built.
   - dfs(i): Recursive function that builds subsets.
     * Base case: When i >= len(nums), we've made decisions for all elements.
     * Recursive cases: 
       1. Include nums[i] and recurse.
       2. Don't include nums[i] (by popping) and recurse.

3. Time Complexity: O(2^n)
   - We make 2 recursive calls for each element, leading to 2^n calls.

4. Space Complexity: O(n)
   - The recursion depth can go up to n (the length of nums).
   - The 'subset' list can contain at most n elements.

5. Visualization of the DFS process for nums = [1,2,3]:

                    []
                /         \
              [1]          []                -> include or exclude 1
            /     \      /    \
          [1,2]   [1]   [2]    []           -> include or exclude 2
         /  \    /  \   / \    / \
     [1,2,3][1,2][1,3][1][2,3][2][3][]      -> include or exclude 3

   Each leaf node represents a subset added to the result.

6. Key Points:
   - The DFS approach naturally generates all subsets.
   - By making two recursive calls (include/don't include), we explore all possibilities.
   - subset.copy() is crucial to avoid adding references to the same list.
   - This method generates subsets in a different order compared to the iterative approach.

7. Comparison with Previous Solution:
   - This DFS approach is more intuitive in terms of decision making for each element.
   - It doesn't require sorting the input array.
   - The previous solution added subsets at each step, while this one adds only at the leaves of the recursion tree.

8. Constraints Handling:
   - Works for 1 <= nums.length <= 10
   - Handles both positive and negative integers
   - Assumes uniqueness of elements in nums
"""

class Solution2:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

# Example usage:
solution = Solution2()
print(solution.subsets([1,2,3]))
print(solution.subsets([0]))



"""
Approach:
    We'll use a backtracking approach to generate all subsets.
    1. Start with an empty subset.
    2. For each element, we have two choices: include it in the current subset or not.
    3. Recursively generate subsets for the remaining elements.
    4. Add each generated subset to the result.

Time Complexity: O(2^n), where n is the number of elements in nums.
We have two choices (include or not) for each element, leading to 2^n subsets.

Space Complexity: O(n), where n is the number of elements in nums.
This accounts for the recursion stack. The space to store all subsets is not counted as auxiliary space.
    

Key Points:
    1. Every subset is valid, including the empty set and the full set.
    2. The order of elements in each subset doesn't matter, but we maintain a specific order to avoid duplicates.
    3. We add each subset to the result immediately, before making recursive calls.
    4. Backtracking ensures we explore all possibilities efficiently.

Visualization of the backtracking process for [1,2,3]:

                      []
           /          |          \
         [1]         [2]         [3]
       /     \        |
    [1,2]   [1,3]    [2,3]
      |
   [1,2,3]

This tree shows:
    1. How subsets are built incrementally.
    2. Each node represents a valid subset (added to the result).
    3. The leaves aren't the only valid subsets; every node is a valid subset.

Optimization:
    1. Adding subsets immediately to the result avoids the need for a separate check.
    2. Using 'start' in the loop prevents generating duplicate subsets and maintains order.
"""

class Solution1:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, current):
            # Add the current subset to the result
            result.append(current[:])
            
            # Generate subsets by including elements from start to end
            for i in range(start, len(nums)):
                # Include the current element
                current.append(nums[i])
                # Recursively generate subsets for the remaining elements
                backtrack(i + 1, current)
                # Backtrack: remove the last added element
                current.pop()

        result = []
        backtrack(0, [])
        return result

# Example usage:
solution = Solution1()
print(solution.subsets([1,2,3]))
print(solution.subsets([0]))
input = "abc"
print(solution.subsets(list(input)))

