"""
Problem Statement: Remove All Adjacent Duplicates In String

    You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
    We repeatedly make duplicate removals on s until we no longer can.
    Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Examples:
1. Input: s = "abbaca"
   Output: "ca"
   Explanation: 
   - In "abbaca" we remove "bb" since the letters are adjacent and equal.
   - The result is "aaca", of which only "aa" is possible to remove.
   - The final string is "ca".

2. Input: s = "azxxzy"
   Output: "ay"

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

def removeDuplicates(s: str) -> str:
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)

# Test the function
test_cases = ["abbaca", "azxxzy", "aaaaaa", "abcde", "aabbcc"]

for test in test_cases:
    result = removeDuplicates(test)
    print(f"Input: {test}")
    print(f"Output: {result}")
    print()

"""
Explanation of the solution:

1. We use a stack to keep track of characters as we iterate through the string.
2. For each character in the input string:
   - If the stack is not empty and the top of the stack matches the current character,
     we pop the top element from the stack (removing the adjacent duplicate).
   - Otherwise, we push the current character onto the stack.
3. After processing all characters, the stack contains the characters of the final string.
4. We join the characters in the stack to form the result string.

Time Complexity: O(n), where n is the length of the input string.
- We iterate through each character in the string once.
- Each character is pushed and popped at most once.

Space Complexity: O(n) in the worst case.
- In the worst case (no duplicates), we might store all characters in the stack.

This stack-based approach allows us to efficiently remove adjacent duplicates in a single pass
through the string, without the need for multiple iterations or string manipulations.
"""