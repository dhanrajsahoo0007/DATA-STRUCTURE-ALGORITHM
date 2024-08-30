"""
Problem Statement:
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
* 0 <= digits.length <= 4
* digits[i] is a digit in the range ['2', '9'].

Time Complexity: O(4^N * N), where N is the number of digits in the input.
Space Complexity: O(N) for the recursion stack, O(4^N) for storing all combinations.

Answer Explanation:
    This solution uses a backtracking approach to generate all possible combinations.
    We use a recursive helper function that builds the combinations one character at a time.
    For each digit, we try all possible letters and recursively build the rest of the combination.

Recursive Tree (for input "23"):
                       ""
              /         |         \
             a          b          c
           / | \      / | \      / | \
          ad ae af   bd be bf   cd ce cf

"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        # Mapping of digits to letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(combination, next_digits):
            # If there are no more digits to check
            if len(next_digits) == 0:
                # Add the combination to the result
                result.append(combination)
            else:
                # Iterate over all letters which map the next available digit
                for letter in phone_map[next_digits[0]]:
                    # Append the current letter to the combination and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
        
        result = []
        backtrack("", digits)
        return result


# Example runs
solution = Solution()

# Example 1
print("Example 1:")
print("Input: digits = \"23\"")
print("Output:", solution.letterCombinations("23"))

# Additional Example
print("\nAdditional Example:")
print("Input: digits = \"234\"")
print("Output:", solution.letterCombinations("234"))