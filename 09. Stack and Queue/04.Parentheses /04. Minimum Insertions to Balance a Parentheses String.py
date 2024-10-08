"""
Problem: Minimum Add to Make Parentheses Valid

    A parentheses string is valid if and only if:
        - It is the empty string,
        - It can be written as AB (A concatenated with B), where A and B are valid strings, or
        - It can be written as (A), where A is a valid string.

    You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
    For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

    Return the minimum number of moves required to make s valid.

Example 1:
    Input: s = "())"
    Output: 1

Example 2:
    Input: s = "((("
    Output: 3

Constraints:
    1 <= s.length <= 1000
    s[i] is either '(' or ')'.

Explanation of the solution:

    1. We use two counters:
        - open_count: keeps track of unmatched opening parentheses
        - additions: counts the number of parentheses we need to add

    2. We iterate through the string once:
        - For each '(', we increment open_count
        - For each ')', we check:
            - If there's an unmatched '(' (open_count > 0), we decrement open_count
            - Otherwise, we need to add a '(', so we increment additions

    3. After the iteration:
        - additions represents the number of '(' we needed to add
        - open_count represents the number of ')' we need to add to close all parentheses

    4. The total minimum additions is the sum of additions and open_count


Time Complexity: O(n), where n is the length of the input string.
Space Complexity: O(1), as we only use a constant amount of extra space.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Initialize counters
        open_count = 0  # Count of unmatched opening parentheses
        additions = 0   # Count of necessary additions

        # Iterate through the string
        for char in s:
            if char == '(':
                # Increment open_count for each opening parenthesis
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    # Match a closing parenthesis with an open one
                    open_count -= 1
                else:
                    # No matching open parenthesis, need to add one
                    additions += 1

        # Any remaining unmatched open parentheses need closing
        return additions + open_count

# Test cases
solution = Solution()

# Test case 1
print(solution.minAddToMakeValid("())"))  # Expected: 1

# Test case 2
print(solution.minAddToMakeValid("((("))  # Expected: 3

# Test case 3
print(solution.minAddToMakeValid("()"))   # Expected: 0

# Test case 4
print(solution.minAddToMakeValid("()))(("))  # Expected: 4

# Test case 5
print(solution.minAddToMakeValid("))"))   # Expected: 2

