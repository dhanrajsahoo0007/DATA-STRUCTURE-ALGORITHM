"""

Problem Statement:
    Given an array of distinct positive integers (candidates) and a target integer,
    find all unique combinations of candidates where the chosen numbers sum to the target.
    Each number in candidates may be used an unlimited number of times.

Approach:
    We use a backtracking algorithm to explore all possible combinations.
    1. Sort the candidates array (optional, but can help with pruning).
    2. Use a recursive function to build combinations:
    a. If the current sum equals the target, add the current combination to the result.
    b. If the current sum exceeds the target, return (backtrack).
    c. For each candidate, add it to the current combination and recursively call the function.
    3. Start the recursion with an empty combination and a sum of 0.

Time Complexity: O(N^(T/M)), where N is the number of candidates,
    T is the target value, and M is the minimum value among the candidates.
    - In the worst case, we explore all possible combinations.
    - The maximum depth of recursion is T/M (using the smallest candidate repeatedly).
    - At each level, we have up to N choices.

Space Complexity: O(T/M)
    - The main space usage comes from the recursion stack.
    - The maximum depth of recursion is T/M.
    - Each recursive call stores a constant amount of data.

Example walkthrough (candidates [2,3,6,7], target 7):
    1. Start with empty combination: []
    2. Choose 2: [2], remaining target: 5
    3. Choose 2 again: [2,2], remaining target: 3
    4. Choose 3: [2,2,3], remaining target: 0 (Solution found)
    5. Backtrack to [2,2], choose 6 (exceeds target, backtrack)
    6. Backtrack to [2], choose 3: [2,3], remaining target: 2
    7. Continue this process...
    8. Eventually, we'll also find the solution [7]
    Final output: [[2,2,3], [7]]

Optimization or Variations:
    1. Early termination: Break the loop when a candidate exceeds the remaining target.
    2. Memoization: Could be used for problems with repeated subproblems.
    3. Iterative approach: Could be implemented to avoid recursion overhead.

Key Points:
    1. Backtracking is crucial: It allows efficient exploration of all possibilities.
    2. Sorting can optimize: Allows for early termination in some cases.
    3. Avoiding duplicates: Achieved by our choice of starting index in recursive calls.
    4. Unbounded knapsack nature: Each number can be used multiple times.
"""

def combinationSum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()

    candidates.sort()  # Optional, but can help with pruning
    result = []
    backtrack(0, target, [])
    return result

# Example usage
print(combinationSum([2,3,6,7], 7))


def backtrack(candidates, target, start, path, result):
    if target == 0:
        result.append(path[:])
        return
    for i in range(start, len(candidates)):
        if candidates[i] > target:
            break  # Optimization: early termination if candidates are sorted
        path.append(candidates[i])
        backtrack(candidates, target - candidates[i], i, path, result)
        path.pop()  # Backtrack by removing the last added candidate

def combination_sum(candidates, target):
    candidates.sort()  # Optional, but can help with pruning
    result = []
    backtrack(candidates, target, 0, [], result)
    return result
# Example usage:
print(combination_sum([2,3,6,7], 7))